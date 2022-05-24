from django.contrib import admin
from .models import Task, UserWallet
# Register your models here.


admin.site.register(UserWallet)
admin.site.register(Task)
