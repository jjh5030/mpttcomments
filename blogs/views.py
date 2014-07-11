from django.shortcuts import render
from .models import Post

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect, get_object_or_404

# Create your views here.

def home(request):
	last_posts = Post.objects.all().order_by('-added')[:3]
	context_dict = {'last_posts':last_posts}
	return render(request, 'home.html', context_dict)