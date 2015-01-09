from django.db import models

from inquisition.managers import SearchManagerMixin,
                                 SearchManager,
                                 SimpleQSearchManagerMixin,
                                 SimpleQSearchManager


class SearchableModelMixin(object):

    objects = SearchManager()


class SimpleQSearchModelMixin(object):

    objects = SimpleQSearchManager()
