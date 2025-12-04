from django.urls import path
from .views import *




urlpatterns = [
    path('users/',UserApi.as_view()),
    path('users/<int:user_id>/', UserApi.as_view()),
    path('orders/',OrderApi.as_view()),
    path('orders/<int:order_id>',OrderApi.as_view()),
    path('product/',ProductApi.as_view()),
    path('product/<int:id>',ProductApi.as_view())
]
