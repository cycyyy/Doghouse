from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from Doghouse.myblog.views import index,articles,tag,cdt,about
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        (r"^css/(?P<path>.*)$","django.views.static.serve",{"document_root":settings.CSS_DIR}),
    # Examples:
    # url(r'^$', 'Doghouse.views.home', name='home'),
    # url(r'^Doghouse/', include('Doghouse.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$',index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^(\d)/$',articles),
    url(r'^tag/([^/]+)/$',tag),
    url(r'^time/([^/]+)/$',cdt),
    url(r'^about/$',about),
    url(r'^index/([^/]+)/$',index),
    url(r'^tag/([^/]+)/([^/]+)/$',tag),
    url(r'^time/([^/]+)/([^/]+)/$',cdt),
)
