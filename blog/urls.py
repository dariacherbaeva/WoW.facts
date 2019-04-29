from django.conf.urls import url
from blog import views
from django.urls import path


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^start/$', views.index, name='index'),
    path('<int:id>/', views.single, name='single'),
    url(r'^home/\d+/add_like$', views.add_like, name='add_like'),
    path('content/new/', views.post_new, name='single_new'),
    path('user_content/<int:id>', views.show_user, name='user_list'),

    # path('home/<int:pk>/add_like', views.add_like, name='add_like'),

    # url(r'^r/add_likes/(?P<post_id>[0-9]+)/$', views.add_like, name='post')

]