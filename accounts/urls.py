from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .import views as accounts_views
app_name='accounts'

urlpatterns = [
	url(r'^$',accounts_views.home,name='home'),
	url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
	url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
	url(r'^signup/$',accounts_views.signup,name='signup'),
	url(r'^settings/change_password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/change_password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    url(r'^reset/$', auth_views.password_reset,{'template_name':'password_reset.html',
    	'email_template_name' : 'password_reset_email.html',
        'subject_template_name' : 'password_reset_subject.txt',
    	'post_reset_redirect':'accounts:password_reset_done',
    	}, name='password_reset'),
    url(r'^reset/done/$', auth_views.password_reset_done,{'template_name':'password_reset_done.html'}, 
    	name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, 
        {
        'template_name':'password_reset_confirm.html',
        'post_reset_redirect':'accounts:password_reset_complete'
        },
        name='password_reset_confirm'),
    url(r'^reset/complete/$', auth_views.password_reset_complete,{'template_name':'password_reset_complete.html'} ,name='password_reset_complete'),


	
]