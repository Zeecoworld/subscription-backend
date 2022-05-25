from django.db import models
from django.conf import settings
import secrets
import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import datetime as dt 
from datetime import  timedelta
# Create your models h
# ere
# .

today = datetime.date.today()

User = settings.AUTH_USER_MODEL



class Membership(models.Model):

    MEMBERSHIP_CHOICES = (
            ('Free','Free'),
            ('Jasper','Jasper'),
            ('Onynx','Onynx'),
            ('Obsidian','Obsidian'),
            ('Pearl','Pearl'),
            ('Ruby','Ruby'),
            ('Sapphire','Sapphire'),
            ('Topaz','Topaz'),
            ('Opal','Opal'),
            ('Bronze','Bronze'),
            ('Silver','Silver'),
            ('Diamond','Diamond')
        )
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True,blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default="Free", max_length=40)
    duration = models.PositiveIntegerField(default=30)
    duration_period = models.DateField(default=dt.now().date() + timedelta(days=30))
    price = models.IntegerField()
    interest_rate = models.IntegerField()
    start_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.membership_type}"

    
    def member_price(self):
        return self.price * 100



class  UserMembership(models.Model):
    user = models.OneToOneField(User, related_name='user_membership',on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership,related_name='user_membership',on_delete=models.SET_NULL,null=True)
    verified = models.BooleanField(default=False)
    date_added = models.DateField(auto_now=True)



    def __str__(self):
        return f"{self.user.username} - {self.membership.membership_type}"



@receiver(post_save, sender=UserMembership)
def create_subscription(sender, instance, created, *args, **kwargs):
    if created:
        Subscription.objects.create(user_membership=instance, expires_in=dt.now().date() + timedelta(days=instance.membership.duration))


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership,related_name='subscription',on_delete=models.CASCADE)
    expires_in = models.DateField(null=True,blank=True)
    active = models.BooleanField(default=True)

    
    def __str__(self):

        return f"{self.user_membership.membership.membership_type} - {self.user_membership.user}"

    
    def check_sub(self):
        return self.user_membership.membership.membership_type



@receiver(post_save, sender=Subscription)
def delete_subscription(sender, instance, *args, **kwargs):
    if instance.expires_in < today:
        subscription = Subscription.objects.get(id=instance.id)
        subscription.delete()




class PaymentScreenshot(models.Model):
    images = models.ImageField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.images} - by {self.user}"



class TaskResult(models.Model):
    result = models.ImageField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.result} - by {self.user}"

    
    
    

     