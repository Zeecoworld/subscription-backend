# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .utils import generate_ref_code
from django.urls import reverse

# Create your models here.
# USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
# NAME_REGEX = '^[a-zA-Z]*$'


class User(AbstractUser):
    username = models.CharField(max_length=256, unique=True, blank=False)
    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(unique=True, blank=False)
    wallet_address = models.CharField(max_length=256, unique=True, blank=False)
    # bank_name = models.CharField(max_length=256, unique=True, blank=False)
    # account_name = models.CharField(max_length=256, unique=True, blank=False)
    # account_number = models.PositiveIntegerField(unique=True, blank=False)

    def __unicode__(self):
        return self.username


    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse("user_profile", kwargs={"username": self.username})

    



class Referral(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='referred_by')
    created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"

    
    def get_recommended_profile(self):   ## TOTAL NUMBER OF REFERRALS!!!
        qs = Referral.objects.all()
        my_ref_count = []
        for profile in qs:
            if profile.recommended_by == self.user:
                my_ref_count.append(profile)
        
        return len(my_ref_count)


    def save(self,*args,**kwargs):
        if self.code == "":
           code = generate_ref_code()
           self.code = code  
        super().save(*args,**kwargs)


    
    
