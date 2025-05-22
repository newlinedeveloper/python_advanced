Absolutely! Let’s Dockerize both the Django backend and React frontend and connect them using docker-compose.

🧱 Project Structure (Summary)

Here's how your folders should be structured:

vehicle-platform/
├── backend/ (Django project here)
├── frontend/ (React app here)
├── docker-compose.yml
├── .env (optional)

---

✅ 1. Dockerize the Django Backend

🔧 backend/Dockerfile

```dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "vehicle_platform.wsgi:application", "--bind", "0.0.0.0:8000"]
```

🔧 backend/requirements.txt

Make sure it includes:

```
Django>=4.2
djangorestframework
gunicorn
psycopg2-binary
django-cors-headers
```

🔧 backend/settings.py additions

Allow DB and frontend from docker network:

```python
ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://frontend:3000'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vehicle_db',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

---

✅ 2. Dockerize the React Frontend

🔧 frontend/Dockerfile

```dockerfile
FROM node:18

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD ["npm", "start"]
```

🔧 frontend/package.json update

Change "start" script to use 0.0.0.0:

```json
"scripts": {
  "start": "react-scripts start --host 0.0.0.0",
  ...
}
```

🔧 frontend/src/api.js

Update base URL to use backend service name:

```js
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://backend:8000/api/',
});

export default API;
```

---

✅ 3. Create docker-compose.yml at the root

📄 docker-compose.yml

```yaml
version: '3.8'

services:
  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_DB: vehicle_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    command: gunicorn vehicle_platform.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db

  frontend:
    build: ./frontend
    volumes:
      - ./frontend:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    depends_on:
      - backend

volumes:
  pgdata:
```

---

✅ 4. Build and Run Everything

From your root directory:

```bash
docker-compose build
docker-compose up
```

🎉 Your setup will now be available at:

* Django API: [http://localhost:8000/api/](http://localhost:8000/api/)
* React App: [http://localhost:3000/](http://localhost:3000/)

---

✅ 5. Optional: Initial DB Setup (First Run Only)

Run migrations and create superuser:

```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```

---

Would you like help setting up:

* Static files serving in production?
* Nginx reverse proxy?
* CI/CD (GitHub Actions) for auto builds?

Let me know how you’d like to evolve this setup!
