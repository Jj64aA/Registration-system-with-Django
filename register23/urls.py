from django.urls import path
from . import views
urlpatterns = [
    path('register-records/',views.index,name='register-records'),
    path('my-register/', views.register, name='register'),
    path('confirm/', views.confirm, name='confirm'),
    path('certificate/<str:pk>', views.certificate, name='cert'),
    path('certificate/', views.page_not_found, name='pagenotfound'),
    path('dash/', views.dash, name='dash'),
    path('card/<str:pk>', views.card, name='card'),
    path('card/', views.page_not_found, name='pagenotfound'),
    path('khamedmohammedtaha-cnticclub/', views.userlogin, name='login'),
    path('logout/',views.userlogout,name="logout"),
    path('404/',views.page_not_found,name="404"),
]