
from django.conf.urls import url

from login import views

urlpatterns = [
  url(r'^home/problems/submit',views.submit,name='submit'),
  url(r'^home/problems/',views.problems,name='problems'),
  url(r'^home/',views.home,name='home'),
  url(r'^$', views.index, name='index'),
  
  
]