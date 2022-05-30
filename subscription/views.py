# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import (authenticate,
                                 login,
                                 logout
                                )
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.views import *
from accounts.models import *   ###REFERRAL INFO
from tasks.models import *
from .forms import *
from .take_tasks import random_link,random_task 
from django.conf import settings
import datetime
from datetime import datetime as dt 
from datetime import  timedelta
import json
import requests

today = datetime.date.today()



def index(request):



    return render(request,"index.html")


def need_register(request):

    return render(request,"need_register.html")



def  privacy(request):

    return render(request,"privacy.html")



def dashboard(request):
    user = request.user.username
    user_membership = UserMembership.objects.get(user=request.user)
    subs = Subscription.objects.filter(user_membership=user_membership).exists()
    referral_link = Referral.objects.filter(user__username=user).values('code').first()['code']
    ref = Referral.objects.get(user=request.user)
    if subs == False:
        return redirect('need_register')
    else:
        subscription = Subscription.objects.filter(user_membership=user_membership).last()
        subs_check = subscription.check_sub()
        ref_nos = ref.get_recommended_profile()
        if subs_check == "Free":
            return redirect('free_sub')
        else:   
            link1 = random_link()
            link2 = random_link()
            link3 = random_link()
            task1 = random_task()
            task2 = random_task()
            task3 = random_task()
            task_existed = Task.objects.filter(subscription=subscription,task_date=today).exists()
            if task_existed == False:
               Task.objects.create(subscription=subscription,youtube_task1=task1,youtube_task2=task2,youtube_task3=task3,youtube_link1=link1,youtube_link2=link2,youtube_link3=link3)
            tasks = Task.objects.filter(subscription=subscription,task_date=today)
            wallets = UserWallet.objects.filter(subscription=subscription,entered_date=today)
            if request.method == "POST":
               form = PaymentForm(request.POST,request.FILES)
               if form.is_valid():
                    post = form.save(commit=False)
                    post.user = request.user
                    post.save()
                    messages.error(request, 'Your task will be confirmed')
                    return redirect('dashboard')
            else:
                form = TaskForm()
        context = {"tasks":tasks,"wallets":wallets,"subs_check":subs_check,"ref_nos":ref_nos,"ref":referral_link,"form":form}
        return render(request,"dashboard.html",context)


def free_sub(request):
    user = request.user.username
    user_membership = UserMembership.objects.get(user=request.user)
    subs = Subscription.objects.filter(user_membership=user_membership).exists()
    referral_link = Referral.objects.filter(user__username=user).values('code').first()['code']
    ref = Referral.objects.get(user=request.user)
    if subs == False:
        return redirect('need_register')
    else:
        subscription = Subscription.objects.filter(user_membership=user_membership).last()
        subs_check = subscription.check_sub()
        ref_nos = ref.get_recommended_profile()
        if subs_check == "Free":
            link1 = random_link()
            link2 = random_link()
            link3 = random_link()
            task1 = random_task()
            task2 = random_task()
            task3 = random_task()
            task_existed = Task.objects.filter(subscription=subscription,task_date=today).exists()
            if task_existed == False:
               Task.objects.create(subscription=subscription,youtube_task1=task1,youtube_task2=task2,youtube_task3=task3,youtube_link1=link1,youtube_link2=link2,youtube_link3=link3)
            tasks = Task.objects.filter(subscription=subscription,task_date=today)
            wallets = UserWallet.objects.filter(subscription=subscription,entered_date=today)
            if request.method == "POST":
               form = PaymentForm(request.POST,request.FILES)
               if form.is_valid():
                    post = form.save(commit=False)
                    post.user = request.user
                    post.save()
                    messages.error(request, 'Your task will be confirmed')
                    return redirect('free_sub')
            else:
                form = TaskForm()
            context = {"tasks":tasks,"wallets":wallets,"subs_check":subs_check,"ref_nos":ref_nos,"ref":referral_link,"form":form}
            return render(request, "free_dashboard.html", context)




       

def about(request):


    return render(request,"about.html")



def subscription(request):


    return render(request,"subscription.html")



@login_required
def package(request):
    plan = request.GET.get('sub_plan')
    fetch_membership = Membership.objects.filter(membership_type=plan).exists()
    if fetch_membership == False:  ##APPORVED
        return redirect('sub_void')
    membership = Membership.objects.get(membership_type=plan)
    membership_price = membership.price
    if request.method == "POST":
        form = PaymentForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.error(request, 'Your transaction will be confirmed within few minutes...then proceed to login again')
            return redirect('package')
    else:
        form = PaymentForm()

    
    context = {"form":form,"price":membership_price}
    return render(request,"package.html",context)


  
    
    











