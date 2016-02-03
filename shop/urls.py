from django.conf.urls import url

from . import views

app_name = 'shop'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^profile/', views.profile_view, name='profile_view'),
	url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^activate/(?P<id>[0-9]+)/(?P<hash>[0-9A-Za-z]+)/$', views.activation_view, name='activate')
]