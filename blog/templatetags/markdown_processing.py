from django import template
from django.template.defaultfilters import stringfilter

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

register = template.Library()

@register.filter()
@stringfilter
def markdown_to_html(value):
	md = markdown.Markdown(
		extensions=[
			'markdown.extensions.fenced_code',
			CodeHiliteExtension(css_class='highlight', linenums=True),
		]
	)
	return md.convert(value)

class TargetBlankExtension(markdown.Extension):
	def extendMarkdown(self, md, md_globals):
		# Add target_blank pattern to Markdown instance
		md.treeprocessors.add('target_blank', TargetBlankTreeprocessor(md), '_end')

class TargetBlankTreeprocessor(markdown.treeprocessors.Treeprocessor):
	def run(self, root):
		# Add target="_blank" attribute to all links
		for element in root.iter('a'):
			element.set('target', '_blank')

def makeExtension(**kwargs):
	return TargetBlankExtension(**kwargs)