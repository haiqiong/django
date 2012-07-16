from django.conf.urls import patterns, include, url
from search.views import search

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

"""
from coltrane.models import Entry
entry_info_dict = { 'queryset': Entry.objects.all(), 'date_field': 'pub_date', }
"""
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
		url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
				{'document_root': '/Users/haiqiongyao/Documents/djcode/tinymce/jscripts/tiny_mce'}),
		url(r'^search/$', search),
		url(r'^weblog/', include('coltrane.urls')),
		url(r'^comments/', include('django.contrib.comments.urls')),
		#url(r'^weblog/$', 'coltrane.views.entries_index'),
		#url(r'^weblog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', \
				#'coltrane.views.entry_detail'),
		#url(r'^weblog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', \
		#		'django.views.generic.date_based.object_detail', entry_info_dict),
		url(r'', include('django.contrib.flatpages.urls')),
		
		
)
