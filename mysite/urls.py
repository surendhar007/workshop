"""mysite URL Configuration

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
from registration.views import  *
from registration import urls as reg_urls
from django.contrib.auth import views as auth_views

from mysite.views import anonymous_required

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'register/', include(reg_urls)),
    url(r'^user/login/$',anonymous_required(auth_views.login),{'template_name': 'register/in.html'},name='in'),
    url(r'^user/logout/$',auth_views.logout,{'template_name': 'logout.html'},name='logout'),
    url(r'^chocolate/add/', AddChocolateView.as_view(),name="addchocolate")
]
