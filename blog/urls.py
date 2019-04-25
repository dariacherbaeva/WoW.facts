from django.conf.urls import url
from blog import views
from django.urls import path


urlpatterns = [
    url(r'^r/$', views.home, name='home'),
    url(r'^d/$', views.index, name = 'index'),
    path('<int:id>/', views.single, name='single'),

]