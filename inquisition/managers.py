from functools import reduce
from operator import and_
from operator import or_

from django.db import models
from django.db.models import Q


__all__ = [
    'LookupManager',
    'LookupManagerMixin',
    'OrderedSearchManager',
    'OrderedSearchManagerMixin',
    'SearchManager',
    'SearchManagerMixin',
]


class OrderedSearchManagerMixin(object):

    search_fields_order = tuple()

    def __init__(self, *args, **kwargs):
        search_fields_order = kwargs.pop('search_order_fields', None)
        if search_fields_order:
            self.search_fields_order = search_fields_order
        super(OrderedSearchManagerMixin, self).__init__(*args, **kwargs)

    def search(self, queryset=None):
        queryset = queryset or self.get_queryset()
        if self.search_fields_order:
            queryset = queryset.order_by(*self.search_fields_order)
        return queryset


class OrderedSearchManager(OrderedSearchManagerMixin, models.Manager):
    pass


class LookupManagerMixin(object):

    search_fields = tuple()

    def __init__(self, *args, **kwargs):
        search_fields = kwargs.pop('search_fields', None)
        if search_fields:
            self.search_fields = search_fields
        super(LookupManagerMixin, self).__init__(*args, **kwargs)

    def search(self, *args, **kwargs):
        """Search for anything in args and in search_fields

        In summary, produces the queryset of all results that each arg from
        args at least once in any of the fields in "search_fields"

        For every word, produces a "factor" the the form:
            Q(field1__icontains:word1) | Q(field2__icontains:word1) | ...
        And reduces factors like:
            factor1 & factor2 & ...
        """
        queryset = kwargs.pop('queryset', self.get_queryset())
        query_keys = ["%s__icontains" % field for field in self.search_fields]
        query_factors = []
        for word in args:
            query_pairs = [{k: word} for k in query_keys]
            query_objects = [Q(**qp) for qp in query_pairs]
            query_factor = reduce(or_, query_objects)
            query_factors.append(query_factor)
        query_product = reduce(and_, query_factors)
        queryset = queryset.filter(query_product)
        return queryset


class LookupManager(LookupManagerMixin, models.Manager):
    pass


class SearchManagerMixin(LookupManagerMixin, OrderedSearchManagerMixin):
    pass


class SearchManager(SearchManagerMixin, models.Manager):
    pass
