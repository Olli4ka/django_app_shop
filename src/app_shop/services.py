from django.db.models import Sum, Avg, Count
from django.db.models import F, Q
from .models import User, ShoppingCart, Product, Order
from .seed_data import USERS_DATA, PRODUCTS_DATA



# Create users with login and password
def seed_users():
    users = []

    for username, password in USERS_DATA:
        user, created = User.objects.get_or_create(login=username)
        if created:
            user.password = password
            user.save()
        users.append(user)

    return users


# Create carts and link each cart to a user (OneToOne)
def seed_carts(users):
    carts = []

    for user in users:
        cart, _ = ShoppingCart.objects.get_or_create(owner=user)
        carts.append(cart)

    return carts


# Create products (avoid duplicates)
def seed_products():
    existing = set(Product.objects.values_list('name', flat=True))

    products_to_create = [
        Product(name=name, price=price)
        for name, price in PRODUCTS_DATA
        if name not in existing
    ]

    Product.objects.bulk_create(products_to_create)


# Get all products
def list_products():
    return Product.objects.all()


# Direct relation: from cart to user
def get_cart_owner_login(cart):
    return cart.owner.login


# Reverse relation: from user to cart
def get_user_cart(user):
    return user.cart


# Add products to carts using add()
def seed_cart_products(carts):
    products = list(Product.objects.all())

    if not products:
        return carts  # защита

    for i, cart in enumerate(carts):
        selected_products = [
            products[i % len(products)],
            products[(i + 1) % len(products)]
        ]

        cart.products.add(*selected_products)

    return carts


# set(): replace all products in a cart
def set_products_for_cart(cart_id, product_names):
    cart = ShoppingCart.objects.get(id=cart_id)

    products = Product.objects.filter(name__in=product_names)

    cart.products.set(products)

    return cart


# remove(): remove specific products from cart
def remove_products_from_cart(cart_id, product_names):
    cart = ShoppingCart.objects.get(id=cart_id)

    products = Product.objects.filter(name__in=product_names)

    cart.products.remove(*products)

    return cart


# clear(): remove ALL products from cart
def clear_cart(cart_id):
    cart = ShoppingCart.objects.get(id=cart_id)
    cart.products.clear()
    return cart


# Create orders and link them to users (ForeignKey)
def create_orders(users):
    orders = []

    for user in users:
        order = Order.objects.create(owner=user)
        orders.append(order)

    return orders


# select_related(): optimize Order → User
def show_orders_with_users():
    orders = Order.objects.select_related('owner')

    for order in orders:
        print(f"# {order.id} | Owner: {order.owner.login}")


# prefetch_related(): optimize ShoppingCart → Products
def show_carts_with_products():
    carts = ShoppingCart.objects.prefetch_related('products').select_related('owner')

    for cart in carts:
        print(f"{cart.owner.login} | products: {[p.name for p in cart.products.all()]}")


# Aggregate: total, average and count of products
def get_products_stats():
    stats = Product.objects.aggregate(
        total_price=Sum('price'),
        avg_price=Avg('price'),
        total_products=Count('id')
    )

    print(stats)
    return stats


# Annotate: number of products in each cart
def annotate_carts_with_product_count():
    carts = ShoppingCart.objects.annotate(
        products_count=Count('products')
    )

    for cart in carts:
        print(f"{cart.owner.login} | products: {cart.products_count}")

    return carts


# Annotate: number of orders per user
def annotate_users_with_orders_count():
    users = User.objects.annotate(
        orders_count=Count('orders')
    )

    for user in users:
        print(f"{user.login} | orders: {user.orders_count}")

    return users


# F expression: increase all prices by 10%
def increase_prices():
    Product.objects.update(price=F('price') * 1.1)

    print("Prices updated")


# Q objects: complex filtering
def filter_products():
    products = Product.objects.filter(
        Q(price__gt=300) | Q(name__icontains='phone')
    )

    for p in products:
        print(p)

    return products


# Run full seeding process
def seed_all():
    users = seed_users()
    seed_products()
    carts = seed_carts(users)
    seed_cart_products(carts)
    create_orders(users)

    print("Seeding completed.")


def run_demo_queries():
    print("\n--- Aggregation ---")
    get_products_stats()

    print("\n--- Annotation (carts) ---")
    annotate_carts_with_product_count()

    print("\n--- Annotation (users) ---")
    annotate_users_with_orders_count()

    print("\n--- Q objects ---")
    filter_products()

    print("\n--- F expressions ---")
    increase_prices()

    print("Demo queries completed.")