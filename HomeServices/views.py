from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render


def home(request):
    return  render_to_response('HomeServices/home.html')
    #return HttpResponse('<h1>Blog Home</h1>')
def login(request):
    return  render_to_response('users/login.html')
def castcertificate(request):
    return  render_to_response('HomeServices/castcertificate.html')
def regofmrg(request):
    return  render_to_response('HomeServices/regofmrg.html')
def transferown(request):
    return  render_to_response('HomeServices/transferown.html')
def lernlic(request):
    return  render_to_response('HomeServices/lernlic.html')
def inccer(request):
    return  render_to_response('HomeServices/inccer.html')
def menu(request):
    return  render_to_response('HomeServices/menu.html')
def requestform(request):
    return  render_to_response('HomeServices/RequestFormTemplet.html')


