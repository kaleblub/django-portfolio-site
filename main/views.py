from django.shortcuts import render

def home(request):
	return render(request, 'main/home.html')

def about(request):
	return render(request, 'main/about.html', {'title': 'About'})

def portfolio(request):
	return render(request, 'main/portfolio.html')

def blog(request):
	return render(request, 'main/blog.html')

def services(request):
	return render(request, 'main/services.html')

def contact(request):
	return render(request, 'main/contact.html')