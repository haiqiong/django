from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from coltrane.models import Entry, Link
entry_info_dict = { 'queryset': Entry.objects.all(), 'date_field': 'pub_date', }
link_info_dict = {'queryset': Link.objects.all(), 'date_field': 'pub_date', }


urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
		url(r'^$', 'coltrane.views.entries_index'),
		url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 
				'coltrane.views.entry_detail'),
		#url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 
		#		'coltrane.views.entry_detail', 'coltrane_entry_detail'),
		#url(r'^weblog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', \
		#		'django.views.generic.date_based.object_detail', entry_info_dict),
		url(r'^links$/', 'django.views.generic.date_based.archive_index', link_info_dict,
				'coltran_link_archive_index'),
		url(r'^links/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
				'django.views.generic.date_based.object_detail', link_info_dict, 
				'coltran_link_detial'),
)
