from django.shortcuts import render
from projects.models import Project
from blog.models import Post

def home(request):
	recent_posts = Post.objects.order_by('-date_posted')[:6]
	number_of_posts = Post.objects.all().count()
	completed_projects = Project.objects.all().count()
	featured_projects = Project.objects.filter(featured=True)

	context = {
		'featured_projects': featured_projects,
		'recent_posts': recent_posts,
		'number_of_posts': number_of_posts,
		'completed_projects': completed_projects,
	}
	return render(request, 'main/home.html', context)

def services(request):
	return render(request, 'main/services.html')

def error_404_view(request, exception):
	return render(request, 'main/404.html', status=404)