from django.urls import path, include
from rest_framework import routers
from . import views
from .api import FeedbackViewSet


router = routers.DefaultRouter() #Маршрутизатор который включает марштруты для стандартного набора действий, DefaultRouter дополнительно включает корневое представление API
router.register('/feedback', FeedbackViewSet) #Метод регистрации включающий префикс URL /feedback, а также класс набора представлений viewset

urlpatterns = [
    path('', views.send, name='send-form'),
    path('api', include(router.urls)),
    path('read-form', views.read, name='read-form'),
]
