import functools

from django.db import models
from django.db.models import Q


__all__ = [
    'SearchManagerMixin',
    'SearchManager',
    'SimpleQSearchManagerMixin',
    'SimpleQSearchManager',
]


class SearchManagerMixin(object):
    """
    Provides an interface to search objects based on `args` and `kwargs`.
    """

    order_fields = tuple()

    def search(self, queryset=None, *args, **kwargs):
        queryset = queryset or self.get_queryset()
        if self.order_fields:
            queryset = queryset.order_by(*self.order_fields)
        return queryset


class SearchManager(SearchManagerMixin, models.Manager):
    """
    Provides an interface to search objects based on `args` and `kwargs`.
    """


class SimpleQSearchManagerMixin(SearchManagerMixin):    
    """
    Provides a search method that performs icontains queries on each field
    provided in `search_fields`. Only CharField will be accepted.
    Related fields can be also queryied upon.
    """

    search_fields = tuple()
    should_split_q = True

    def search(self, queryset=None, *args, **kwargs):
        """
        
        """
        queryset = queryset or self.get_queryset()
        q = kwargs.get('q', None)
        if self.should_split_q:
            words = q.split()
            return self.split_search(queryset, *words)
        lookups = ["%s__icontains" % field for field in self.search_fields]
        query_objects = [{lookup: q} for lookup in self.lookups]
        query_objects = [Q(**qo) for qo in query_objects]
        query_objects = functools.reduce(lambda x, y: x | y, query_objects)
        queryset = queryset.filter(query_objects).distinct()
        return super().search(queryset)
        
    def split_search(self, queryset=None, *args, **kwargs):
        """
        The items to search upon are `args`.
        """
        queryset = queryset or self.get_queryset()
        lookups = ["%s__icontains" % field for field in self.search_fields]
        results = list()
        for word in args:
            query_objects = [{lookup: word} for lookup in lookups]
            query_objects = [Q(**qo) for qo in query_objects]
            query_objects = functools.reduce(lambda x, y: x | y, query_objects)
            results.append(self.filter(query_objects))
        objects = set(results[0])
        for result in results[1:]:
            objects = objects.intersection(result)
        queryset = self.filter(pk__in=[o.pk for o in objects])
        return queryset


class SimpleQSearchManager(SimpleQSearchManagerMixin, models.Manager):
    """
    """
