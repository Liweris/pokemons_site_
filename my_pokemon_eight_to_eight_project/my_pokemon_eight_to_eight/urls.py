"""my_pokemon_eight_to_eight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name='signupuser'),
    path('signout/', views.signoutuser, name='signoutuser'),
    path('signin/', views.signinuser, name='signinuser'),
    path('current/', views.currentmyapp, name='currentmyapp'),
    path('profile/', views.profileuser, name='profileuser'),
    path('profileupdate', views.profileupdateuser, name='profileupdateuser'),
    path('news/', views.newsstud, name='newsstud'),
    path('latter/', views.lattertorector, name='lattertorector'),
    path('createlatter', views.createlattertorector, name='createlattertorector'),
    path('somenews', views.somenewsbig, name='somenewsbig'),
    path('', views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)