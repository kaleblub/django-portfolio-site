"""
URL configuration for kaleblub_portfolio_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main import views as main_views
from about import views as about_views
from blog import views as blog_views
from contact import views as contact_views
from projects import views as projects_views
# from services import views as services_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('about/', about_views.about, name='about'),
    path('portfolio/', projects_views.PortfolioHome.as_view(), name='portfolio'),
    path('blog/', blog_views.BlogHome.as_view(), name='blog'),
    path('services/', main_views.services, name='services'),
    path('contact/', contact_views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)