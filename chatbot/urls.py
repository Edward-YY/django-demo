from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_api, name='chat_api'),  # 定义了 /chat/ 路径
    path('chattest/', views.chat_test, name='chat_test'),  # 定义了 /chat/ 路径
]
