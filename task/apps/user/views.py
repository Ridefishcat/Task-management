from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import reverse

class LoginView(View):
    """登录"""
    def get(self,request):
        #显示登录页面
        return render(request,'login.html')

    def post(self,request):
        #接受数据
        username=request.POST.get('username')
        password=request.POST.get('pwd')

        #校验数据
        if not all([username,password]):
            return render(request,'login.html',{'errmsg':'数据不完整'})
        #登录校验
        user = authenticate(request,username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            #return redirect(reverse('index.html'))
            return redirect(reverse('mission:index'))
        else:
        # No backend authenticated the credentials
            return render(request,'login.html',{'errmsg':'用户名或密码错误'})


