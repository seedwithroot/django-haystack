from django.conf.urls.defaults import *
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView
from decimal import *

sqs = SearchQuerySet().facet('tags').facet('domain_authority').facet('page_rank')
sqs_advanced = SearchQuerySet().all() #.facet('tags').facet('domain_authority').facet('page_rank')
sqs_advanced.filter(domain_authority__in=['%.2f' % (x/100.00) for x in range(80, 100)]) #=Decimal('80')) #, prices__lt=Decimal('20.00'))
#sqs_advanced.filter(domain_authority__gt=Decimal('80')) #, prices__lt=Decimal('20.00'))
sqs_advanced.order_by('-domain_authority')

urlpatterns = patterns('haystack.views', 
        url(r'^advanced/$', FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs_advanced), name='haystack_search_advanced'),
        #url(r'^$', FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs), name='haystack_search'),

        )
