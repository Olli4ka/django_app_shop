# 🛒 Django ORM Shop Demo

A training Django project that demonstrates working with:

* Django ORM
* Database relationships
* Query optimization
* Aggregation and annotation
* Q and F objects
* Service layer architecture

This project was created as a practice backend application to explore advanced Django ORM features using a simple shop system.

---

# ✨ Features

## 🔗 Models and Relationships

The project demonstrates:

* **One-to-One** relationship (`User ↔ ShoppingCart`)
* **ForeignKey** relationship (`User → Order`)
* **Many-to-Many** relationship (`ShoppingCart ↔ Product`, `Order ↔ Product`)

---

## ⚙️ ORM Operations

The project includes examples of:

* `create()`
* `get_or_create()`
* `add()`
* `set()`
* `remove()`
* `clear()`
* `all()`
* `filter()`
* `update()`

---

## 🚀 Query Optimization

Examples of:

* `select_related()`
* `prefetch_related()`

---

## 🧠 Advanced ORM Features

### 📊 Aggregation

* `Sum`
* `Avg`
* `Count`

### 🏷️ Annotation

* Product count per cart
* Order count per user

### 🔍 Q Objects

Complex filtering with logical conditions.

### 🧮 F Expressions

Database-side field updates.

---

# 🛠️ Technologies

* Python 3.12
* Django 5.1
* SQLite

---

# 📁 Project Structure

```text
src/
├── app_shop/
│   ├── migrations/
│   ├── models.py
│   ├── services.py
│   ├── seed_data.py
│   ├── views.py
│   └── ...
├── config/
├── manage.py
└── ...
```

---

# 🗃️ Models

## 👤 User

Stores user login and password.

## 🛒 ShoppingCart

Each user has one cart.

## 📦 Product

Represents products available in the shop.

## 📋 Order

Stores user orders and related products.

---

# 🧩 Service Layer

Business logic is separated into `services.py`.

Examples include:

* database seeding
* cart operations
* ORM query demonstrations
* aggregation and annotation examples
* query optimization examples

---

# 🌱 Database Seeding

The project uses a dedicated `seed_data.py` file for demo data.

### Seed database

Run Django shell:

```python
from app_shop.services import seed_all

seed_all()
```

---

# 🧪 ORM Query Demonstrations

Run:

```python
from app_shop.services import run_demo_queries

run_demo_queries()
```

This demonstrates:

* aggregation
* annotation
* Q objects
* F expressions

---

# 💻 Examples

## Add products to cart

```python
cart.products.add(product1, product2)
```

## Replace products in cart

```python
cart.products.set(products)
```

## Remove products

```python
cart.products.remove(product)
```

## Clear cart

```python
cart.products.clear()
```

---

# 🎯 Learning Goals

This project was created to practice:

* Django ORM
* model relationships
* efficient database queries
* backend architecture organization
* working with relational databases

---

# 🚧 Future Improvements

Possible future improvements:

* Django templates and views
* Bootstrap UI
* Django Admin customization
* REST API with Django REST Framework
* authentication system
* order total calculations

---

# 👩‍💻 Author

Created as a Django ORM practice project.
