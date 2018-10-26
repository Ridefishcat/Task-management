from django.shortcuts import render,redirect
from django.views.generic import View
from .models import mission
from django.shortcuts import reverse
from user.models import User

def index(request):
    '''首页'''
    return render(request, 'index.html')

class NewMission(View):
    def get(self,request):
        """添加任务页面显示"""
        return render(request,'newmission.html')

    def post(self,request):
        """添加任务到数据库"""
        # 获取登录用户对应User对象
        user = request.user
        #接收数据
        startdate=request.POST.get('startdate')
        enddate=request.POST.get('enddate')
        category=request.POST.get('category')
        priority=request.POST.get('priority')
        duration=request.POST.get('duration')
        content=request.POST.get('content')
        name=User.objects.get(id=user.id)
        #校验数据

        if not all([startdate,enddate,category,priority,duration,content,name]):
            return render(request,'newmission.html',{'errmsg':'数据不完整'})

        #业务处理
        mission.objects.create(startdate=startdate,
                               enddate=enddate,
                               category=category,
                               priority=priority,
                               duration=duration,
                               content=content,
                               name=name,
                               )
        #返回应答
        return  redirect(reverse('mission:newmission'))




"""
普通用户：
用户名：putongyonghu
密码：12345678
超级用户：
用户名：zz
密码：19980330a

"""