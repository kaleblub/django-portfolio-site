from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView
)

from .models import Post, Tag

class BlogHome(ListView):
	model = Post
	template_name = 'blog/blog.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 10
	# return render(request, 'blog/blog.html')

def BlogDetailView(DetailView):
	return render()