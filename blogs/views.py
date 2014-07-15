from django.shortcuts import render
from .models import Post, Comment

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect, get_object_or_404, RequestContext

# Create your views here.

def home(request):
	last_posts = Post.objects.all().order_by('-added')[:3]
	context_dict = {'last_posts': last_posts}
	return render(request, 'home.html', context_dict)

def single_post(request, post_id):
	single_post = Post.objects.filter(id=post_id)
	context_dict = {'single_post': single_post}
	context_dict['post_id'] = post_id

	comments = Comment.objects.filter(post=single_post)

	#return render(request, 'post.html', context_dict)
	return render_to_response('post.html', locals(), context_instance=RequestContext(request))

def add_comment(request):
	comment = Comment(comment=request.POST['comment'], ) 
	# if this is a reply to a comment, not to a post 
	if form.cleaned_data['parent_id'] != '': 
		comment.parent = Comment.objects.get(id=request.POST['parent_id']) 
		comment.save()