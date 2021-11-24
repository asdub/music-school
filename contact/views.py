from django.db import models
from django.shortcuts import render, redirect
from wagtail.core.models import Page

# Create your views here.

def new_message(request):
    """ Set session var form_page_success to false """
     
    source_page = request.session['source-page']

    request.session['form_page_success'] = False
    return redirect(source_page  + '#contact-us', permanent=False)
