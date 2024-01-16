from django.shortcuts import render

from django.http import HttpResponse


def index(request):

    context = {'weather': "Welcome my Request"}

    return render(request, 'request/index.html',context)

# Create your views here.
