# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers                    
from todoReact import views                           

router = routers.DefaultRouter()                      # add this
router.register(r'todos', views.TodoView, 'todo')     # add this

urlpatterns = [
    path('admin/', admin.site.urls),         path('api/', include(router.urls))                # add this
]