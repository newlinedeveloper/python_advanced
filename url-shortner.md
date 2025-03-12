Designing a **URL shortener like Bit.ly** in **Django** using **Django REST Framework (DRF)** involves:  
- **Generating unique short URLs**  
- **Storing them in a database**  
- **Redirecting users from short URLs to the original long URLs**  

---

### **📌 Steps to Build the URL Shortener in Django**
1. **Set up Django & Django REST Framework**  
2. **Create a Django App (e.g., `shortener`)**  
3. **Define the URL model (`ShortURL`)**  
4. **Generate a short URL key using a hashing algorithm**  
5. **Create API endpoints to:**
   - **Shorten a URL**
   - **Retrieve the original URL using the short code**
   - **Redirect users to the original URL**
6. **Test using Django's built-in server & API clients like Postman**

---

### **📌 Let's Code: Django URL Shortener**
#### **1. Install Dependencies**
```bash
pip install django djangorestframework
```

#### **2. Create Django Project & App**
```bash
django-admin startproject urlshortener
cd urlshortener
python manage.py startapp shortener
```

#### **3. Add `shortener` & `rest_framework` to `settings.py`**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'shortener',  # Our app
]
```

---

### **4. Create the URL Model**
Inside `shortener/models.py`, define the model to store **long URLs and short codes**.

```python
import string
import random
from django.db import models

def generate_short_code():
    """Generate a unique 6-character short code"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortURL(models.Model):
    long_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.long_url}"
```

- `long_url`: Stores the original URL  
- `short_code`: A unique 6-character identifier  
- `created_at`: Timestamp for tracking  

---

### **5. Create Serializers for the API**
Inside `shortener/serializers.py`:
```python
from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['id', 'long_url', 'short_code', 'created_at']
```

---

### **6. Create Views (API Logic)**
Inside `shortener/views.py`, implement logic for:
- **Shortening a URL**
- **Retrieving a URL by short code**
- **Redirecting to the original URL**

```python
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortURL
from .serializers import ShortURLSerializer

class ShortenURLView(generics.CreateAPIView):
    """API to shorten a URL"""
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

class RetrieveURLView(APIView):
    """API to retrieve the original URL from a short code"""
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return Response({"long_url": short_url.long_url})

class RedirectURLView(APIView):
    """Redirect a short URL to its original long URL"""
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return redirect(short_url.long_url)
```

---

### **7. Define API Routes**
Inside `shortener/urls.py`:
```python
from django.urls import path
from .views import ShortenURLView, RetrieveURLView, RedirectURLView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten-url'),
    path('<str:short_code>/', RetrieveURLView.as_view(), name='retrieve-url'),
    path('go/<str:short_code>/', RedirectURLView.as_view(), name='redirect-url'),
]
```

- `POST /shorten/` → **Create a short URL**
- `GET /<short_code>/` → **Retrieve the long URL**
- `GET /go/<short_code>/` → **Redirect to the long URL**

---

### **8. Register Routes in Main `urls.py`**
Modify `urlshortener/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shortener.urls')),  # Include shortener API routes
]
```

---

### **9. Run Migrations & Start the Server**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## **📌 Testing the API**
### **1. Shorten a URL**
**Endpoint:**  
```http
POST http://127.0.0.1:8000/api/shorten/
```
**Request Body:**
```json
{
    "long_url": "https://example.com/some-long-url"
}
```
**Response:**
```json
{
    "id": 1,
    "long_url": "https://example.com/some-long-url",
    "short_code": "aB3xYz",
    "created_at": "2025-03-11T12:00:00Z"
}
```

---

### **2. Retrieve the Long URL**
**Endpoint:**  
```http
GET http://127.0.0.1:8000/api/aB3xYz/
```
**Response:**
```json
{
    "long_url": "https://example.com/some-long-url"
}
```

---

### **3. Redirect to the Long URL**
**Endpoint:**  
```http
GET http://127.0.0.1:8000/api/go/aB3xYz/
```
- **Expected Result:** The browser will redirect to `https://example.com/some-long-url`.

---

## **📌 Enhancements (For Production)**
- **Use Base62 Encoding** instead of random strings for better uniqueness.
- **Cache Lookups** using Redis for faster redirects.
- **Rate Limiting** to prevent abuse.
- **Custom Domains** for shortened links (e.g., `bit.ly/custom123`).
- **Expiration & Analytics** for link tracking.

---

## **📌 Summary**
| Feature | Status |
|---------|--------|
| Shorten URLs | ✅ |
| Retrieve Long URL | ✅ |
| Redirect Users | ✅ |
| REST API with Django DRF | ✅ |
| Unique Short Codes | ✅ |

---


Sure! Below is the **folder structure** for your Django-based **URL Shortener** application using Django REST Framework (DRF).  

---

## **📌 Django Project Folder Structure**
```
urlshortener/                # Root Django project
│── shortener/               # Django app for URL shortening
│   │── migrations/          # Database migrations
│   │── __init__.py          # Makes it a package
│   │── admin.py             # Django Admin configuration
│   │── apps.py              # App configuration
│   │── models.py            # Database models (ShortURL model)
│   │── serializers.py       # DRF serializers for API
│   │── views.py             # API logic (Shorten, Retrieve, Redirect URLs)
│   │── urls.py              # API routes for the shortener app
│   │── tests.py             # Unit tests for the app
│
│── urlshortener/            # Main Django project settings
│   │── __init__.py
│   │── asgi.py              # ASGI config
│   │── settings.py          # Project settings
│   │── urls.py              # Root URL configuration (includes `shortener.urls`)
│   │── wsgi.py              # WSGI config
│
│── manage.py                # Django management script
│── db.sqlite3               # SQLite database (auto-created after migrations)
│── requirements.txt         # Python dependencies (Django, DRF, etc.)
│── venv/                    # Virtual environment (optional)
```

---

## **📌 Explanation of Key Files**
| File/Folder | Purpose |
|-------------|---------|
| **`shortener/models.py`** | Defines the **ShortURL model** to store long & short URLs. |
| **`shortener/views.py`** | Implements API logic for **shortening, retrieving, and redirecting URLs**. |
| **`shortener/serializers.py`** | Serializes data for the **REST API**. |
| **`shortener/urls.py`** | Maps **API routes** to views. |
| **`urlshortener/settings.py`** | Configures the Django **project settings**. |
| **`manage.py`** | Runs Django commands (`runserver`, `migrate`, etc.). |
| **`db.sqlite3`** | Default SQLite database (you can switch to PostgreSQL/MySQL in production). |

---

## **📌 Sample API Endpoints**
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/shorten/` | `POST` | Shortens a long URL |
| `/api/<short_code>/` | `GET` | Retrieves the original long URL |
| `/api/go/<short_code>/` | `GET` | Redirects to the original URL |

---
