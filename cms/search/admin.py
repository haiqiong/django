from django.contrib import admin
#from django.contrib.flatpages.admin import FlatPageAdmin
#from django.contrib.flatpages.models import FlatPage

from search.models import SearchKeyword

class SearchKeywordAdmin(admin.ModelAdmin):
		pass

admin.site.register(SearchKeyword, SearchKeywordAdmin)

"""
class SearchKeywordInline(admin.StackedInline):
		model = SearchKeyword

class FlatPageAdminWithKeywords(FlatPageAdmin):
		inline = [SearchKeywordInline]

admin.site.unregister(FlatPage)
#admin.site.register(SearchKeyword, SearchKeywordAdmin)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)
"""
