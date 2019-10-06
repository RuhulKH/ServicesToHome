from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Home'),
    path('home/', views.menu, name='Home'),
    #path('login/', views.login, name='Login'),
    #path('register/', views.register, name='Register'),
    #path('services/', views.services, name='Services'),
    #path('castcertificate/', views.castcertificate, name='Cast certificate'),
    #path('regofmrg/', views.regofmrg, name='Registration of Marriage'),
    #path('transferown/', views.transferown, name='Transfer of Owner'),
    #path('lernlic/', views.lernlic, name='Learner Licence'),
    #path('inccer/', views.inccer, name='Income Certificate'),
    path('menu/', views.menu, name='Menu'),
    path('onsubmit/', views.onsubmit, name='Onsubmit'),
    path('requestform/', views.requestform, name='RequestForm'),
]