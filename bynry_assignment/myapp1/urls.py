from django.urls import path
from . import views

urlpatterns = [
    path('',views.handlelogin , name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.handlelogout, name='logout'),
    path('submit/', views.submit_request, name='submit_request'),
    path('index/', views.track_request, name='track_request'),

    ]
