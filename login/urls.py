"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^login/', include('login.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

urlpatterns = [
    url(r'^admin2/', include(admin.site.urls)),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^contests/', include('contests.urls', namespace='contests')),


    url(r'^editproblem/', include('problem.urls', namespace='editproblem')),
    url(r'^submit/', include('submission.urls', namespace='code_editor')),

]

