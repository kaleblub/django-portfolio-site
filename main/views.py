from django.shortcuts import render
from projects.models import Project
from blog.models import Post
import requests, dotenv, os
from datetime import datetime

from requests.exceptions import HTTPError # new


dotenv.load_dotenv()

def home(request):
	recent_posts = Post.objects.order_by('-date_posted')[:6]
	featured_projects = Project.objects.filter(featured=True)

	context = build_common_context()
	context['featured_projects'] = featured_projects
	context['recent_posts'] = recent_posts

	return render(request, 'main/home.html', context)

def services(request):
	return render(request, 'main/services.html')

def error_404_view(request, exception):
	return render(request, 'main/404.html', status=404)



def build_common_context():
	number_of_posts = Post.objects.all().count()
	completed_projects = Project.objects.all().count()
	commit_count = get_commit_estimate()

	common_context = {
		'number_of_posts': number_of_posts,
		'commit_count': commit_count,
		'completed_projects': completed_projects,
	}
	return common_context

def get_commit_estimate():
	last_commit_total = 310
	last_commit_date = datetime.strptime('2023-12-6', '%Y-%m-%d').date()
	current_date = datetime.now().date()
	day_difference = (current_date - last_commit_date).days
	count_increase = day_difference // 2
	return last_commit_total + count_increase