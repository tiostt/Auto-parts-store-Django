from django.urls import path

from users import views

app_name='user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('basket/', views.basket, name='basket'),
    path('logout/', views.logout, name='logout'),
]