from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index') ,
    url(r'^user/(?P<username>\w+)/$', views.AccountView, name='accountview'),
    url(r'^login/$', 'Main.views.login'),
    url(r'^logout/$', 'Main.views.logout'),
    url(r'^finish_sign_up/$', 'Main.views.finish_sign_up'),
    url(r'^signup/$', views.SignUpView.as_view(), name = 'signup'),
]