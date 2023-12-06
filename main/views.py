from django.shortcuts import render
from projects.models import Project
from blog.models import Post
import requests, dotenv, os

from requests.exceptions import HTTPError # new


dotenv.load_dotenv()

def home(request):
	recent_posts = Post.objects.order_by('-date_posted')[:6]
	number_of_posts = Post.objects.all().count()
	completed_projects = Project.objects.all().count()
	commit_count = get_github_commit_count(os.getenv('GITHUB_USERNAME'), os.getenv('GITHUB_TOKEN'))
	featured_projects = Project.objects.filter(featured=True)

	context = {
		'featured_projects': featured_projects,
		'recent_posts': recent_posts,
		'number_of_posts': number_of_posts,
		'commit_count': commit_count,
		'completed_projects': completed_projects,
	}
	return render(request, 'main/home.html', context)

def services(request):
	return render(request, 'main/services.html')

def error_404_view(request, exception):
	return render(request, 'main/404.html', status=404)

def get_github_commit_count(username, token):
    access_token = token
    api_url = f'https://api.github.com/users/{username}/repos'
    
    headers = {'Authorization': f'token {access_token}'}

    response = requests.get(api_url, headers=headers)
    repos = response.json()

    total_commits = 0

    for repo in repos:
        repo_name = repo['name']
        commits = count_commits(username, repo_name, token)
        total_commits += commits

    return total_commits

def count_commits(username, repo_name, token):
    access_token = token
    api_url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
    
    headers = {'Authorization': f'token {access_token}'}
    params = {'since': '2000-01-01T00:00:00Z'}  # Adjust the start date as needed

    response = requests.get(api_url, headers=headers, params=params)
    commits = response.json()

    return len(commits)