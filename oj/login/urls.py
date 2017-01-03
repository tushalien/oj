
from django.conf.urls import url

from login import views

urlpatterns = [
  url(r'^home/',views.home,name='home'),
  url(r'^problems/submit',views.submit,name='submit'),
  url(r'^problems/',views.problems,name='problems'),
  url(r'^$', views.index, name='index'),
  
  
]

