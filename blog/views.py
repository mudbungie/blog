from django.shortcuts import render, get_object_or_404

from .models import Post, Category

def index(request):
	data = {'categories':Category.objects.all(),
					'posts':Post.objects.all(),
					}
	return render(request, 'blog/index.html', data)

def view_post(request, slug):
	data = {'post':get_object_or_404(Post, slug=slug)}
	return render(request, 'blog/view_post.html', data)

def view_category(request, slug):
	category = get_object_or_404(category, slug=slug)
	data = {'category': category,
					'posts':Post.objects.filter(category=category)}
	return render(request, 'blog/view_category.html', data)


