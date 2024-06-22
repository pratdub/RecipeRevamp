from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    peoples=[
        {'name':'Prateek','age':'22'},
        {'name':'Naman','age':'24'},
        {'name':'Abhinav','age':'56'},
        {'name':'Swaraj','age':'34'}
    ]



    return render(request, "home/index.html", context={'peoples':peoples})


def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')

def success_page(request):
    return HttpResponse("<h1>Wow! you successfully routed to this page</h1>")