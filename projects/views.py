from django.shortcuts import render
from django.views.generic import (
	ListView
)
from .models import Language, Project

class PortfolioHome(ListView):
	model = Project
	template_name = 'projects/portfolio.html'
	context_object_name = 'projects'
	ordering = ['-date_posted']
	paginate_by = 10
	# return render(request, 'blog/blog.html')

	def get_queryset(self):
		return Project.objects.prefetch_related('languages_used').all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['languages'] = Language.objects.all()
		return context


# def portfolio(request):
# 	return render(request, 'projects/portfolio.html')