from collective.grok import gs
from sinarngo.resource import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.resource', 
    title=_('sinarngo.resource import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.resource.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
