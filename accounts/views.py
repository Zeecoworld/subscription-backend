# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import (authenticate,
                                 login,
                                 logout
                                )
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User, Referral
from subscription.models import *
from subscription.urls import *
from subscription.views import *

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_membership = UserMembership.objects.get(user=request.user)
            sub = Subscription.objects.filter(user_membership=user_membership).exists()
            subs = Subscription.objects.filter(user_membership=user_membership).last()
            reg = subs.check_sub()
            if sub == True:
                if reg == "Free":
                    return redirect('sub_void')
                else:
                    return redirect('dashboard')
            else:
                return redirect('need_register')
        else:
            messages.error(request, "Login details not valid")
            return redirect('login')

    return render(request,"login.html")


def register_view(request):
    profile_id = request.session.get('ref_profile')
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if profile_id is not None:
                recommended_by_ref = Referral.objects.get(id=profile_id)
                password = form.cleaned_data.get("password1")
                instance.set_password(password)
                instance = form.save()
                registered_user = User.objects.get(id=instance.id)
                registered_profile = Referral.objects.get(user=registered_user)
                registered_profile.recommended_by = recommended_by_ref.user
                registered_profile.save()  
                get_membership =  Membership.objects.get(membership_type='Free')
                inst = UserMembership.objects.create(user=instance,membership=get_membership)
                authenticate(request, username=instance.username, password=instance.password)
                login(request, instance)
                return redirect('sub_void')
            else:
                user = form.save(commit=False)
                username = user.username.lower()
                password = form.cleaned_data.get("password1")
                user.set_password(password)
                user.save()  
                get_membership =  Membership.objects.get(membership_type='Free')
                inst = UserMembership.objects.create(user=user,membership=get_membership)
                authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('sub_void')
                
                   
        

    return render(request, 'register.html', {'form': form})



def logout_view(request): # logs out the logged in users
    logout(request)
    return redirect('index')




def subscribe_none(request):


    return render(request,"sub_void.html")






def referrals(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        referral = Referral.objects.get(code=code)
        request.session['ref_profile'] = referral.id
    except:
        pass
    return render(request,'dashboard.html')

