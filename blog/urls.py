from django.conf.urls import url
from blog import views
from django.urls import path


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^start/$', views.index, name='index'),
    path('<int:id>/', views.single, name='single'),
    url(r'add_like/$', views.add_like, name='add_like'),

   # url(r'^r/add_likes/(?P<post_id>[0-9]+)/$', views.add_like, name='post')

]