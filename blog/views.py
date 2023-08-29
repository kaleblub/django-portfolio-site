from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView
)
from itertools import groupby
from operator import attrgetter

from .models import Post, Tag

class BlogHome(ListView):
	model = Post
	template_name = 'blog/blog.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 1

	def get_posts_by_year(self):
		posts = self.get_queryset()
		grouped_posts = {year: list(group) for year, group in groupby(posts, key=lambda post: post.date_posted.year)}
		return grouped_posts

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['grouped_posts'] = self.get_posts_by_year()
		return context

class PostView(DetailView):
	model = Post
	template_name = 'blog/blog-details.html'