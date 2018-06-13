# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
# def post_list(request):
#      return render(request, 'www/post_list.html', {})

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    ppl = Post.objects.all();
    #posts = Post.objects
    return render(request, 'www/post_list.html', {'posty': posts, 'ppl': ppl})
