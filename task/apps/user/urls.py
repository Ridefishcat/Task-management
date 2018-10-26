from django.conf.urls import url
from .views import LoginView
from django.urls import path
urlpatterns = [

    path('login',LoginView.as_view(),name='login'), # 登录

]
