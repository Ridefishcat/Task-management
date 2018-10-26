from django.conf.urls import url
from django.urls import path
from . import views
from .views import NewMission
urlpatterns = [

    path('index',views.index,name='index'), # 主页
    path('newmission',NewMission.as_view(),name='newmission'),#添加任务页

]



