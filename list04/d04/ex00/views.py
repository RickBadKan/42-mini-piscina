from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('ex00/index.html')
    return HttpResponse(template.render(request=request))