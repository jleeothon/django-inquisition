from __future__ import unicode_literals

from django.test import TestCase

from .models import BikeSparePart


class TestBikeSparePart(TestCase):

    def setUp(self):
        self.bike1 = BikeSparePart.create("Llanta 24")
        self.bike2 = BikeSparePart.create("Llanta 24 1 3/8")
        self.bike3 = BikeSparePart.create("Tubo 20 A/V")
        self.bike4 = BikeSparePart.create("Tubo 20 E/V")
        self.bike5 = BikeSparePart.create("Tubo 20 E/V")