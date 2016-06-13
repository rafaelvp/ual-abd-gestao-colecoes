"""GestaoColecoes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

from colecoes import views
from home import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^colecoes/', include('colecoes.urls', namespace = "colecoes")),
    url(r'^home/', include('home.urls', namespace = "home")),
    url(r'^.*sign_up/?$', views.sign_up, name='sign_up'),
    url(r'^.*login/?$', views.logging_in, name='login'),
    url(r'^.*user_details/?$', views.user_details, name='user_details'),
    url(r'^.*user_logout/?$', views.user_logout, name='user_logout'),
    url(r'^.*/?', include('home.urls', namespace="home")),
]
