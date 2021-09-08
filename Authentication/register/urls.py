from django.urls import path
from .views import registerview, logoutview, loginview,home_view,resultview

urlpatterns = [
    path('register/', registerview, name='register'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('',home_view,name='home'),
    path('result/',resultview,name='result')

]
