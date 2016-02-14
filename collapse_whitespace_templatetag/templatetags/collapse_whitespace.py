from django import template
from django.utils.text import normalize_newlines

register = template.Library()

@register.tag
def collapsewhitespace(parser, token):
    """
    Usage::

      {% collapsewhitespace %}

        One


        Two



        Three

      {% endcollapsewhitespace %}

    Will result in "One\nTwo\nThree".
    """

    childnodes = parser.parse('endcollapsewhitespace')

    parser.next_token()

    return CollapseNewlinesNode(childnodes)

class CollapseNewlinesNode(template.Node):
    def __init__(self, childnodes):
        self.childnodes = childnodes

    def render(self, context):
        val = normalize_newlines(self.childnodes.render(context))

        return u'\n'.join(x for x in val.splitlines(False) if x)
