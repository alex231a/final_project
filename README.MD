# 🧱 Django E-commerce with Real-Time Chat & Notification Microservice

This is a **Dockerized Django-based e-commerce application** with:

- 🎯 Django Oscar for core shop functionality  
- 💬 Real-Time Chat using Django Channels & WebSockets  
- 🔔 Flask-based Notification Microservice  
- 🧩 Modular microservices communicating over Redis  

---

## 🛍 Features

- 🧾 Product catalog with categories  
- 🛒 Shopping cart and checkout  
- 💵 PayPal integration  
- 👥 Custom user management  
- 📈 Admin dashboard and analytics  
- 📬 Email notifications with Celery  
- 🔁 Periodic tasks with Celery Beat  
- 🌐 REST API using Django REST Framework  
- 📦 Dockerized setup with PostgreSQL, Redis, RabbitMQ  
- 📊 Flower for task monitoring  
- 💬 Real-Time Chat with WebSockets  
- 🔔 Flask Notification Microservice via Redis pub/sub  

---

## 🚀 Getting Started

### 1. Clone & Prepare

Ensure the following structure exists:

final_project/
├── docker-compose.yml
├── .env
├── django-docker/
├── notification_service/


### 2. Configure environment

Place your `.env` file in the **root** (`final_project/`) directory. Example keys:

```env
POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_pass
CELERY_BROKER_REDIS=redis://redis:6379/0


3. Build & Run
bash
docker-compose up --build

🔗 Available URLs
Service	URL
🌐 Django Site	http://localhost:8000
🌼 Flower	http://localhost:5555
💬 Chat	http://localhost:8000/chat/testroom/


🚀 Technologies Used
Python 3.10+
Django 4.2+
Django Oscar 3.2.5
PostgreSQL
Redis
Celery & Celery Beat
RabbitMQ
Docker & Docker Compose
PayPal REST API
Django Channels
Django REST Framework
Flask
Pytest

💬 Chat Application
This project includes a real-time chat app built with Django Channels and WebSockets.
Features:
WebSocket support via Redis channel layer
Async consumers for real-time updates
Dynamic chat rooms via URL
Location: django-docker/chat/

🔔 Notification Microservice (Flask)
A standalone Flask microservice that:
Subscribes to Redis notifications channel
Logs messages published by Django or other services
How it works:
Django (via Channels or views) publishes events:

redis_conn.publish("notifications", "New user registered")

Flask receives and logs:
[Redis Notification] New user registered
Directory: notification_service/
Dockerfile & requirements.txt: contained within the same folder.

📬 Celery Tasks
Email Notification: On user registration, a background Celery task sends a confirmation email.
User Count Logger: Celery Beat runs a task every 10 minutes to log the number of users in the database.

📬 Celery Tasks
Email Notification: On user registration, a background Celery task sends a confirmation email.
User Count Logger: Celery Beat runs a task every 10 minutes to log the number of users in the database.

🧪 Testing
Run tests inside the Django container:
docker exec -it django pytest

📦 Project Structure
final_project/
├── django-docker/              # Django project with Oscar, REST API, Chat
├── notification_service/       # Flask microservice
├── docker-compose.yml          # Orchestrates all services
├── .env                        # Environment variables

