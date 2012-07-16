from django import template
from coltrane.models import Entry

def do_latest_entries(parser, token):
		return LatestEntriesNode()

class LatestEntriesNode(template.Node):
		def render(self, context):
				context['latest_entries'] = Entry.live.all()[:5]
				return ''

register = template.library()
register.tag('get_latest_entries', do_latest_entries)
