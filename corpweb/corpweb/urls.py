"""
URL configuration for corpweb project.

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
from django.urls import include, path
from .views import  GoogleVerification, download_brochure, home_view, HomeView, Robots
from django.conf import settings
from django.conf.urls.static import static
from .sitemaps import *
from django.contrib.sitemaps.views import sitemap

sitemaps={ 'static': StaticSitemap,}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('company/',include('company.urls')),
    path('product/',include('product.urls')),
    path('inquiry/',include('inquiry.urls')),
    path('notice/',include('notice.urls')),
    path('download_brochure/',download_brochure, name="download_brochure"),
    path('robots.txt',Robots.as_view(), name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='sitemap' ),
    path('googlec16d523d61391181.html',GoogleVerification.as_view(), name='googleverification')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
