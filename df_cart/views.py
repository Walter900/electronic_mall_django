# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from islogin import islogin
from models import Cartinfo
from django.http import JsonResponse
# Create your views here.
@islogin
def cart(request):
    uid = request.session['user_id']
    carts = Cartinfo.objects.filter(user_id=uid)
    context={
             'title':'购物车',
             'page_number':'1',
             'carts':carts
            }
    return render(request,'df_cart/cart.html',context)

@islogin
def add(request,gid,count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    carts = Cartinfo.objects.filter(user_id="uid",good_id="gid")
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = Cartinfo()
        cart.user_id = uid
        cart.goods = gid
        cart.count = count
    cart.save()

    if request.is_ajax():
        count = Cartinfo.objects.filter(user_id=request.session['user_id'])
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')

@islogin
def edit(request, cart_id, count):
    try:
        cart=Cartinfo.objects.get(pk=int(cart_id))
        count1=cart.count=int(count)
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)

@islogin
def delete(request,cart_id):
    try:
        cart = Cartinfo.objects.get(pk=int(cart_id))
        cart.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)