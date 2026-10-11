"""
URL configuration for myfirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def is_admin(user):
    return user.is_superuser or user.groups.filter(name='Admin').exists()

urlpatterns = [
     path('my-secret-panel-123/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/',include('accounts.urls')),
]
