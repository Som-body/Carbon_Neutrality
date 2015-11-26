from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index') ,
    
    url(r'^login/$', 'Main.views.login'),
    url(r'^logout$', 'Main.views.logout'),
    url(r'^signup$', views.SignUpView.as_view(), name = 'signup'),
]