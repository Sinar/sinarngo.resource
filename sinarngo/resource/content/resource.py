from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent

from collective import dexteritytextindexer

from sinarngo.resource import MessageFactory as _


# Interface class; used to define content-type schema.

class IResource(form.Schema, IImageScaleTraversable):
    """
    Publications, Training Materials, Videos and more
    """

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(title=u'Name', 
                         description=u'Name of resource.')

    dexteritytextindexer.searchable('description')
    description = schema.Text(title=u'Description',
                                  description=u'Brief description '
                                  'of resource.'
                                  )
    resource_type= schema.Choice(
        title=_(u'Type'),
        vocabulary = "sinarngo.resource.types"
    )

    dexteritytextindexer.searchable('details')
    form.widget(details="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    details = schema.Text(
        title=_(u"Details"),
        required=False,
    )


    attachment_1 = NamedFile(
        title=_(u'Attachment 1'),
        required=True
    )

    attachment_2 = NamedFile(
        title=_(u'Attachment 2'),
        required=False
    )

    attachment_3 = NamedFile(
        title=_(u'Attachment 2'),
        required=False
    )

    url = schema.TextLine(
        title=_(u'URL'),
        required=False
    )
