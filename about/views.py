from django.shortcuts import render
from main.views import build_common_context

def about(request):
	context = build_common_context()
	context['title'] = 'About'

	return render(request, 'about/about.html', context)
