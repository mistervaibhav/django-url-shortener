from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Url


def index(request):
    return render(request,'shortener/index.html')


def create(request):

    if request.POST:
        link = request.POST['url']

        url = Url.objects.create(link=link)
 
        response = {
            "data" : url.id
        }
    
    return JsonResponse(response)


def go(request, pk):
    url = Url.objects.get(id=pk)
    return redirect(url.link)
