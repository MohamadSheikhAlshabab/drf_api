# Steps of Create Django REST Framework & Docker

-----(To start a project)------#

## in the terminal

- 1 - Prepare your environment for the project :

    - mkdir 'some folder name'
    - cd 'some folder name '
    - poetry init -n
    - poetry add django djangorestframework
    - poetry add --dev black
    - poetry shell
    - django-admin startproject 'project_name_project' .  (don't forget the dot)
    - python manage.py startapp 'app_name'
    - python manage.py createsuperuser
    - python manage.py makemigrations "app_name"
    - python manage.py migrate
    - python manage.py runserver

---

## in VS Code

- 2 - project.settings :

        # name_project/settings.py
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',                        # NEW
        'rubik_cube.apps.RubikCubeConfig',       # NEW
        ]


        REST_FRAMEWORK = {
            'DEFAULT_PERMISSION_CLASS': [
                'rest_framework.permissions.AllowAny',
            ]
        }

        ALLOWED_HOSTS = ['0.0.0.0',]

---

- 3 - app.model :

        # name_app/models.py

        from django.db import models
        from django.contrib.auth import get_user_model

        # Create your models here.

        class Cube(models.Model):
            solver = models.ForeignKey(get_user_model,on_delete=models.CASCADE)
            size = models.PositiveIntegerField()
            best_time = models.TimeField()
            worst_time = models.TimeField()
            total_solve = models.Sum()

            def __str__(self):
                return self.cuber

---

- python manage.py makemigrations "name"

- python manage.py migrate

- 4 - project.urls:

        # name_project/urls.py

        from django.contrib import admin
        from django.urls import path,include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('api/v1/',include('rubik_cube.urls')),

        ]

---

- 5 - app.urls:

        # name_app/urls.py

        from django.urls import path
        from .views import CubeList , CubeDetails

        urlpatterns = [
            path('cube',CubeList.as_view(), name='cube_list'),
            path('cube/<int:pk>',CubeDetails.as_view(), name='cube_details'),
        ]

---

- 6 - create app/serializer.py to convert data to json:

            from rest_framework import serializers
            from .models import Cube

            class CubeSerializer(serializers.ModelSerializer):
                class Meta:
                    fields = ('solver','size','best_time','worst_time')
                    model = Cube

---

- 7 - app.views:

            from django.shortcuts import render
            from rest_framework import generics
            from .models import Cube
            from .serializer import CubeSerializer

            class CubeList(generics.ListCreateAPIView):
                queryset = Cube.objects.all()
                serializer_class = CubeSerializer

            class CubeDetails(generics.RetrieveUpdateDestroyAPIView):
                queryset = Cube.objects.all()
                serializer_class = CubeSerializer

---

- python manage.py runserver

- in root create Dockerfile inside it write:

        FROM python:3
        ENV PYTHONDONTWRITEBYTECODE 1
        ENV PYTHONUNBUFFERED 1
        RUN mkdir /code
        WORKDIR /code
        COPY requirements.txt /code/
        RUN pip install -r requirements.txt
        COPY . /code/

---

- in root create docker-compose.yml inside it write:

        version: '3'

        services:
        web:
            build: .
            command: python manage.py runserver 0.0.0.0:8000
            volumes:
            - .:/code
            ports:
            - "8000:8000"

---

- poetry export -f requirements.txt -o requirements.txt

- open docker

- docker-compose up

- open docker-->dashboard --->start--->open in window settings#ALLOWED_HOSTS = ['0.0.0.0','localhost','127.0.0.1']

- or try:
    - docker-compose down
    - docker-compose build
    - docker-compose up