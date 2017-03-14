from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Create your views here.

def mainpage(request):

    template = get_template('mainpage.html')

    variables = Context( {
        'appname': "APP NAME",
        'titlepage': "LES WAIFUS DEL BONET - COMING SOON",
        'author': "ADRIA BONET"
    })

def dashboard(user)):
    try:
        User.object.get(username=user)
    except:
        raise Http404


    page = template.render(variables)
    return HttpResponse(page)
