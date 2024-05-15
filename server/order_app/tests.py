from django.test import TestCase
from order_app.services import (
    city_by_name,
    calculate_delivery_cost,
    rate_by_cities
)


class RateTestCase(TestCase):

    def setUp(self) -> None:
        pass

    def test_find_moskow(self):
        moskow = city_by_name("Москва")
        self.assertEqual(moskow, not None)

    def test_calculate_delivery_cost(self):

        # Москва-Белгород
        moskow = city_by_name("Москва")
        belgorod = city_by_name("Белгород")
        rate = rate_by_cities(moskow, belgorod)

        self.assertEqual(calculate_delivery_cost(rate, 15), 900)
