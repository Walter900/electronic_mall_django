# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponseRedirect
from models import *
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect
from .islogin import islogin
# Create your views here.


def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    if upwd != upwd2:
        return redirect('/user/register/')

    s1=sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    return redirect('/user/login/')


def register_exist(request):
    uname = request.GET.get('uname')
    count = exist(uname)
    return JsonResponse({'count': count})

#check the existence of the username
def exist(uname):
    users = UserInfo.objects.filter(uname=uname)
    if len(users) != 0:
        return 1
    else:
        return 0

def logout(request):
    request.session.flush()
    return redirect('/user/login')

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'User Login','error_name':0,'error_pwd':0,'uname':uname}
    return render(request, 'df_user/login.html',context)



def login_handle(request):
    get = request.POST
    uname = get.get('username')
    upwd = get.get('pwd')
    jizhu = get.get('jizhu',0)
    users = UserInfo.objects.filter(uname=uname)

    if len(users)==1:
        s1=sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwd:
            print "success"
            red = HttpResponseRedirect('/user/info')

            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            print "passwd incorrect"
            context = {'title':'User Login','error_name':0,'error_pwd':1,'uname':uname, 'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title': 'User Login','error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request,'df_user/login.html',context)


@islogin
def info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).uemail
    context = {'title':'User Center',
               'user_email':user_email,
               'user_name':request.session['user_name']}
    return render(request,'df_user/user_center_info.html',context)


@islogin
def order(request):
    context = {'title':'User Center'}
    return render(request,'df_user/user_center_order.html',context)


@islogin
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
       post=request.POST
       user.ushou = post.get('ushou')
       user.uaddress= post.get('uaddress')
       user.uyoubian = post.get('uyoubian')
       user.uphone = post.get('uphone')
       user.save()
    context={'title':'User Center','user':user}
    return render(request, 'df_user/user_center_site.html',context)






