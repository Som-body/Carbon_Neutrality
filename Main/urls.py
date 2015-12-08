from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index') ,
    url(r'^user/(?P<username>\w+)/$', views.AccountView, name = 'accountview'),
    url(r'^login/$', 'Main.views.login'),
    url(r'^logout/$', 'Main.views.logout'),
    url(r'^finish_sign_up/$', 'Main.views.finish_sign_up'),
    url(r'^signup/$', views.SignUpView.as_view(), name = 'signup'),
    url(r'^add_tree$', views.TreeView.as_view(), name = 'tree_form'),
    url(r'^edit_profile/$', 'Main.views.edit_profile'),
    url(r'^change_password/$', 'Main.views.change_password'),
    url(r'^friend_user/$', 'Main.views.friend_user'),
    url(r'^unfriend_user/$', 'Main.views.unfriend_user'),
    url(r'^find_friend/$', 'Main.views.find_friend'),
    url(r'^carbon_emissions/$', 'Main.views.carbon_emissions'),
    url(r'^about/$', 'Main.views.about'),
    url(r'^tree/(?P<pk>[0-9]+)/$', 'Main.views.tree_detail'),
    url(r'^tree/(?P<pk>[0-9]+)/edit$', 'Main.views.tree_edit'),
]