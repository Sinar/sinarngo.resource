from five import grok
from plone.directives import dexterity, form
from sinarngo.resource.content.resource import IResource
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')

class Index(grok.View):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.template('resource_faceted_listing')
    grok.name('resource_faceted_listing')

