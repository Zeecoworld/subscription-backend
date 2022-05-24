import random
from tasks.models import *
from subscription.models import *


my_file = open("subscription/tasks.txt", "r")

data = my_file.read()

YOUTUBE_LINKS = data.split("\n")



# YOUTUBE_LINKS = ["link1","link2","link3"]

YOUTUBE_TASK = ["like/subscribe","comment"]



def random_link():
    result = random.choice(YOUTUBE_LINKS)
    return result

my_file.close()


def random_task():
    task = random.choice(YOUTUBE_TASK)
    return task


def task_exist(request):
    tasks = None
    link1 = random_link()
    link2 = random_link()
    link3 = random_link()
    task1 = random_task()
    task2 = random_task()
    task3 = random_task()
    user_membership = UserMembership.objects.get(user=request.user)
    subscription = Subscription.objects.filter(user_membership=user_membership).last()
    task_existed = Task.objects.filter(subscription=subscription,task_date=today).exists()
    if task_existed == False:
        tasks = Task.objects.create(subscription=subscription,youtube_task1=task1,youtube_task2=task2,youtube_task3=task3,youtube_link1=link1,youtube_link2=link2,youtube_link3=link3)
    else:
        pass
    return tasks
    
