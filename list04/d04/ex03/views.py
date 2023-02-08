from django.template import loader
from django.shortcuts import render

def index(request):
    shade = 0
    step = 255 / 50
    shades = []
    while shade < 50:
        shades.append("{:02X}".format(int(shade * step)))
        shade += 1

    context = {
        "shades": shades
    }
    
    return render(request, 'ex03/index.html', context)