# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return render(request, 'index.html', {})

def service_list(request):
	pass

# Create your views here.
