from django.db import models


class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.login


class ShoppingCart(models.Model):
    # One-to-One: one cart → one user
    # related_name='cart' → user.cart (for feedback)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    # Many-to-Many: cart contains many products
    # related_name='carts' → product.carts (for feedback)
    products = models.ManyToManyField('Product', blank=True, related_name='carts')

    def __str__(self):
        return f"Cart of {self.owner.login}"


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.price}$)"


class Order(models.Model):
    # Many-to-One: many orders → one user
    # related_name='orders' → user.orders (for feedback)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    # Many-to-Many: one order contains many products
    # related_name='orders' → product.orders (for feedback)
    products = models.ManyToManyField(Product, blank=True, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order # {self.id} by {self.owner.login}"

