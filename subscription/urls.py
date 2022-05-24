from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name="index"),
    path('privacy/', views.privacy, name="privacy"),
    path('about/', views.about, name="about"),
    path('need_register/', views.need_register, name="need_register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('sub-package/', views.subscription, name="subscription"),
    path('package/', views.package , name="package"),    ### INIT PAYSTACK PAYMENT BUTTON???
    # path('payment/', views.callback_url , name="payment")   ### CALL-BACK URL TO PAYSTACK SUBMISSION????

]