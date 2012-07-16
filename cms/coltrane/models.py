from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from tagging.fields import TagField
from markdown import markdown
import datetime

class Category(models.Model):
		title = models.CharField(max_length=250, help_text="Maximum 250 characters.")
		slug = models.SlugField(unique=True, help_text=
				"Suggested value automatically generated from title. Must be unique.")
		description = models.TextField()

		class Meta:
				ordering = ['title']
				verbose_name_plural = "Categories"

		def __unicode__(self):
				return self.title

		def get_absolute_url(self):
				return "/categories/%s/" % self.slug

class Entry(models.Model):
		LIVE_STATUS = 1
		DRAFT_STATUS = 2
		HIDDEN_STATUS = 3
		STATUS_CHOICES = (
				(LIVE_STATUS, 'Live'),
				(DRAFT_STATUS, 'Draft'),
				(HIDDEN_STATUS, 'Hidden'),
		)

		# Core fields
		title = models.CharField(max_length=250)
		excerpt = models.TextField(blank=True, help_text=" \
			A short summary of the entry. Optional.")
		body = models.TextField()

		# Fields to store generated HTML
		excerpt_html = models.TextField(editable=False, blank=True)
		body_html = models.TextField(editable=False, blank=True)

		#Metadata
		pub_date = models.DateTimeField(default=datetime.datetime.now)
		slug = models.SlugField(unique_for_date='pub_date')
		author = models.ForeignKey(User)
		enable_comments = models.BooleanField(default=True)
		featured = models.BooleanField(default=False)
		status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS, \
				help_text = "Only entries with live status wil be publicly displayed.")
		
		# Categorization
		categoris = models.ManyToManyField(Category)
		tags = TagField(help_text="Separate tags with spaces.")

		class Meta:
				ordering = ['-pub_date']
				verbose_name_plural = "Entries"

		def save(self, force_insert=False, force_update=False):
				self.body_html = markdown(self.body)
				if self.excerpt:
						self.excerpt_html = markdown(self.excerpt)
				super(Entry, self).save(force_insert, force_update)

		def __unicode__(self):
				return self.title

		def get_absolute_url(self):
				return "/weblog/%s/%s/" % \
				(self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)
				#return ('coltrane_entry_detail', (), 
				#		{'year': self.pub_date.strftime("%Y"),
				#		 'month': self.pub_date.strftime("%m"),
				#		 'day': self.pub_date.strftime("%d"),
				#		 'slug': self.slug})
		
		#get_absolute_url = models.permalink(get_absolute_url)

class Link(models.Model):
		# core fields.
		title = models.CharField(max_length=250)
		description = models.TextField(blank=True)
		description_html = models.TextField(editable=False, blank=True)
		url = models.URLField('URL', unique=True)

		# metadata.
		posted_by = models.ForeignKey(User)
		pub_date = models.DateTimeField(default=datetime.datetime.now)
		slug = models.SlugField(unique_for_date='pub_date')
		
		# categories.
		tags = TagField()
		enable_comments = models.BooleanField(default=True)
		# whether to post the link to an external service.
		post_elsewhere = models.BooleanField('Post to Delicious', default=True)

		via_name = models.CharField('Via', max_length=250, blank=True, 
				help_text='The name of the person whose site you spotted the link on. Optional.')
		via_url = models.URLField('Via URL', verify_exists=False, blank=True, 
				help_text='The URL of the site where you spotted the link. Optional.')

		class Meta:
				ordering = ['-pub_date']

		def __unicode__(self):
				return self.title

		def save(self):
				if self.description:
						self.description_html = markdown(self.description)
				if not self.id and self.post_elsewhere:
						import pydelicious
						from django.utils.encoding import smart_str
						pydelicious.add(settings.DELICIOUS_USER, settings.DELICIOUS_PASSWORD,
								smart_str(self.url), smart_str(self.title), smart_str(self.tags))
				super(Link, self).save()

		def get_absolute_url(self):
				#return "/weblog/%s/%s/" % \
				#(self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)
				return ('coltrane_entry_detail', (), 
						{'year': self.pub_date.strftime("%Y"),
						 'month': self.pub_date.strftime("%m"),
						 'day': self.pub_date.strftime("%d"),
						 'slug': self.slug})
		
		get_absolute_url = models.permalink(get_absolute_url)
