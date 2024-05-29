from django.test import TestCase
from index_app.models import Const
from calculator_app.models import (
    City,
    Rate
)
from calculator_app.services import (
    city_by_name,
    calculate_delivery_cost_by_rate,
    calculate_delivery_cost,
    rate_by_cities,
    calculate_nigth_delevery
)
from datetime import time


class RateTestCase(TestCase):

    def setUp(self) -> None:
        self.moskow = City.objects.create(name="Москва")
        self.belgorod = City.objects.create(name="Белгород")
        self.rate = Rate.objects.create(
            city_from=self.moskow, city_to=self.belgorod,
            cost_by_weight_0_25=900)
        Const.objects.create(nigth_deliver_cost=1000)

    def test_find_moskow(self):
        moskow = city_by_name("Москва")
        self.assertEqual(moskow, self.moskow)

    def test_find_rate(self):
        rate = rate_by_cities(self.moskow, self.belgorod)
        self.assertEqual(rate, self.rate)

    def test_calculate_delivery_cost_by_rate(self):
        # Москва-Белгород
        self.assertEqual(calculate_delivery_cost_by_rate(
            self.rate,
            weight=15), 900)

    def test_calculate_delivery_cost(self):
        # Москва-Белгород
        self.assertEqual(calculate_delivery_cost(
            self.moskow.name,
            self.belgorod.name,
            weight=15), 900)

    def test_calculate_nigth_delevery(self):
        self.assertEqual(calculate_nigth_delevery(
            deliver_time=time(20, 0, 0)
            ), 1000)
