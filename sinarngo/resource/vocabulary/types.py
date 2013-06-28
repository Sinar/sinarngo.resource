from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class Types(grok.GlobalUtility):
    grok.name('sinarngo.resource.types')
    grok.implements(IVocabularyFactory)

    _terms = [
        dict( value = 'policy',
          title = u'Policy, Strategy, Plan',
        ),
        dict( 
            value = 'legislation',
            title = u'Legislation, Regulation',
        ),
        dict(
            value = 'training',
            title = u'Training, Guide'
        ),
        dict(
             value = 'project',
             title = u'Project',
         ),
        dict(
            value = 'data',
            title = u'Data, Survey'
            ),
        dict(   value = 'application',
            title = 'Application, Product, Portal'),
    ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
