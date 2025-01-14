Let's break down the core functionalities of Flask and Django, two popular Python web frameworks, focusing on routing, middleware, ORM, and building RESTful APIs.

### **Flask**

Flask is a lightweight, micro web framework that is simple to use and extend. It provides the essentials to build web applications without the overhead of a full-stack framework like Django.

#### **1. Core Functionalities**

- **Routing**: Maps URLs to functions.
- **Middleware**: Functions that process requests before they reach your route handlers or responses before they are sent to the client.
- **ORM**: Flask doesn't come with a built-in ORM, but you can use extensions like SQLAlchemy.
- **RESTful APIs**: Flask makes it easy to build RESTful APIs with minimal setup.

#### **Example: Building a Simple RESTful API with Flask**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
books = [{"id": 1, "title": "1984", "author": "George Orwell"}]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)
```

### **Django**

Django is a full-stack web framework with built-in functionalities for database management, routing, and authentication. It follows the Model-View-Template (MVT) architecture.

#### **1. Core Functionalities**

- **Routing**: URL routing via URL configuration (urls.py).
- **Middleware**: Middleware functions are used for processing requests/responses globally.
- **ORM**: Django has a powerful built-in ORM to interact with databases.
- **RESTful APIs**: Can be built using Django REST framework, which provides tools for creating APIs efficiently.

#### **Example: Building a Simple RESTful API with Django**

**Step 1: Set up Django Project and App**
```bash
django-admin startproject myproject
cd myproject
django-admin startapp myapp
```

**Step 2: Define a Model (models.py)**
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```

**Step 3: Create a Serializer (serializers.py)**
```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

**Step 4: Create Views (views.py)**
```python
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

**Step 5: Define URL Patterns (urls.py)**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

**Step 6: Add REST Framework to Installed Apps and Run the Server**
```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapp',
]

# Run migrations and start the server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### **Key Concepts**

- **Routing**: Flask uses decorators (`@app.route`) while Django uses URL configurations in `urls.py`.
- **Middleware**: Both frameworks support middleware, but Django has a more built-in robust system.
- **ORM**: Django has a built-in ORM, while Flask relies on third-party libraries like SQLAlchemy.
- **RESTful APIs**: Flask allows building APIs with minimal overhead, and Django REST framework extends Django's functionality to build RESTful APIs easily.

These examples should help you understand how to work with Flask and Django for building web applications and RESTful APIs.
