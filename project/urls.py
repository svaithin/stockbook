from django.conf.urls import include, url
from django.contrib import admin
from stockbook.views import register, index, user_logout, user_login

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', register, name='register'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$',user_logout, name='logout'),
    url(r'^index/$', index, name='index'),
]
