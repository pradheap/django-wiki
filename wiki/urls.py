from django.conf.urls.defaults import *

from templatetags.wiki import WIKI_WORD


urlpatterns = patterns('wiki.views',
    (r'^$', 'index'),
    ('(?P<name>%s)/$' % WIKI_WORD, 'view'),
    ('(?P<name>%s)/edit/$' % WIKI_WORD, 'edit'),
    (r'^account/', include('django_authopenid.urls')),
)
