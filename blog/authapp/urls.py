from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/',views.sign_up,name='sign_up'),
    path('log_in/',views.log_in,name='log_in'),
    path('log_out/',views.log_out,name='log_out'),
    path('profile/',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('update_profile_pic/',views.update_profile_pic,name='update_profile_pic'),



]
