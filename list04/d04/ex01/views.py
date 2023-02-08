from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def django_page(request):
    template = loader.get_template('ex01/django.html')
    return HttpResponse(template.render(request=request))

def display_page(request):
    template = loader.get_template('ex01/display.html')
    return HttpResponse(template.render(request=request))

def templates_page(request):
    template = loader.get_template('ex01/templates.html')
    return HttpResponse(template.render(request=request))




# Title: "Ex01: Display process of a static page."
# URL: /ex01/display
# Description: In this page, describe the process causing the display of a static web
# page from a simple template going through a view, from the request to the
# answer.

# Title: "Ex01: Template engine."
# URL: /ex01/templates
# Description: In this page, describe the functioning of Django’s default template
# engine as well as the functioning of:
# ◦ Blocks.
# ◦ Loopsfor ... in.
# ◦ if control structures.
# ◦ The display of the passing context variables.