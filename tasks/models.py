from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from subscription.models import *
from accounts.models import *
# Create your models here.




class UserWallet(models.Model):
    subscription = models.ForeignKey(Subscription, related_name='wallet',on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    withdrawal_amount = models.IntegerField(default=0)
    entered_date = models.DateField(auto_now=True)


    def __str__(self):
         return f"{self.subscription.user_membership.user.username} - ${self.amount} - {self.entered_date}"

    @property
    def amount_deposited(self):
        return self.subscription.user_membership.membership.price




class Task(models.Model):
    subscription = models.ForeignKey(Subscription, related_name='task',on_delete=models.CASCADE)
    youtube_task1 = models.CharField(max_length=250, null=True)
    youtube_task2 = models.CharField(max_length=250, null=True)
    youtube_task3 = models.CharField(max_length=250, null=True)
    youtube_link1 = models.CharField(max_length=250, null=True)
    youtube_link2 = models.CharField(max_length=250, null=True)
    youtube_link3 = models.CharField(max_length=250, null=True)
    task_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.subscription.user_membership.user.username}- {self.subscription.user_membership.membership.membership_type} - {self.task_date}"
    
    
    

    






       

