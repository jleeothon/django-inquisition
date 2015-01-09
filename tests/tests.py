from __future__ import unicode_literals

from django.test import TestCase

from .models import BikeSparePart


class TestBikeSparePart(TestCase):

    def setUp(self):
        self.bike1 = BikeSparePart.objects.create(name="Llanta 24", coo='CHN')
        self.bike2 = BikeSparePart.objects.create(name="Llanta 24 1 3/8", coo='JPN')
        self.bike3 = BikeSparePart.objects.create(name="Tubo 20 A/V", coo='TWN')
        self.bike4 = BikeSparePart.objects.create(name="Tubo 20 E/V", coo='VNM')
        self.bike5 = BikeSparePart.objects.create(name="Tubo 24 A/V", coo='CHN')
        self.bike6 = BikeSparePart.objects.create(name="Tubo 24 E/V", coo='JPN')
        self.bike7 = BikeSparePart.objects.create(name="Tubo 24 1 1/8 A/V", coo='TWN')
        self.bike8 = BikeSparePart.objects.create(name="Tubo 24 1 1/8 E/V", coo='JPN')

    def test_search_1_field(self):
        llantas = BikeSparePart.objects1.search("Llanta")
        self.assertEquals(llantas.count(), 2)
        tubos = BikeSparePart.objects1.search("tubO")
        self.assertEquals(tubos.count(), 6)
        tubos24 = BikeSparePart.objects1.search("tubo", "24")
        self.assertEqual(tubos24.count(), 4)

    def test_search_2_fields(self):
        llantas = BikeSparePart.objects2.search("Llanta")
        self.assertEquals(llantas.count(), 2)
        tubos = BikeSparePart.objects2.search("tubO")
        self.assertEquals(tubos.count(), 6)
        tubos24 = BikeSparePart.objects2.search("tubo", "24")
        self.assertEqual(tubos24.count(), 4)
        llantas = BikeSparePart.objects2.search("llanta", 'CHN')
        self.assertEquals(llantas.count(), 1)
        tubos = BikeSparePart.objects2.search("tubO", 'CHN')
        self.assertEquals(tubos.count(), 1)
        tubos24 = BikeSparePart.objects2.search("tubo", 'JPN')
        self.assertEqual(tubos24.count(), 2)
