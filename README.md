# Feedback Application
A very simple feedback submission application made with Django. 

The primary purpose for this application was to understand the process of running tasks asynchronously with Celery and Redis.

Inspired from [Real Python](https://realpython.com/asynchronous-tasks-with-django-and-celery/#reader-comments).

I recreated the application in my style and have added Celery and Redis to send Email asynchronously. 

We have added `time.sleep(10)` to simulate time intensive tasks. 

## Setup

### Virtual Env and Dependencies
Create a virtual env and install dependencies from `requirements.txt`
### Django

Setup your Email Configuration in `.env` file under the `feedback_proj` directory. 

Example `.env` file:
```text
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=***************
```

Then, run the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Redis - Message Broker

Start the redis server
```bash
redis-server
```

### Celery
Start running Celery server with:
```bash
python -m celery -A feedback_proj worker -l info
```

## Application Demonstration
![Screenshot 2024-03-06 at 4 45 19 PM](https://github.com/Mukilan-Krishnakumar/feedback-app/assets/71809485/8362e52a-dda1-4d02-8ae3-e6f38a68be82)

![Screenshot 2024-03-06 at 4 45 30 PM](https://github.com/Mukilan-Krishnakumar/feedback-app/assets/71809485/3e609e44-2ddf-4bda-9ddd-045e1473c5ca)

![Screenshot 2024-03-06 at 4 50 50 PM](https://github.com/Mukilan-Krishnakumar/feedback-app/assets/71809485/2d9a94d3-c2fb-44d5-a0bf-1b96ceaa422b)

Stay Hydrated 🌊

