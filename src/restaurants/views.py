# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.http import HttpResponse
from django.shortcuts import render

# rendering HTML string
# def home(request):
#    html_var = 'whatever'
#    html_ = f"""
#    <!DOCTYPE html>
#    <html lang=en>
#      <head>
#
#      </head>
#      <body>
#        <h1>Hello World!</h1>
#        <p>This is {html_var} coming through</p>
#      </body>
#    </html>
#    """
#    return HttpResponse(html_)

#Creating templates
def home(request):
    num = None
    some_list = [
        random.randint(0, 10000000), random.randint(0, 10000000), random.randint(0, 10000000)
    ]
    condition_bool_item = True
    if condition_bool_item:
        num = random.randint(0, 10000000)
    context = {
        "num": num,
        "some_list": some_list
    }
    return render(request, "base.html", context)

def home2(request):
    context = {
    }
    return render(request, "home2.html", context)

def home3(request):
    context = {
    }
    return render(request, "home3.html", context)
