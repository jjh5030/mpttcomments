from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mpttcommentstest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'blogs.views.home', name='home'),
	url(r'^post/(?P<post_id>\w+)/$', 'blogs.views.single_post', name="single_post"),
)
