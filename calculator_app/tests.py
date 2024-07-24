from decimal import Decimal
from django.test import TestCase
from index_app.models import Const
from calculator_app.models import City, Rate, ExpeditionRate
from calculator_app.services import (
    city_by_name,
    calculate_delivery_cost_by_rate,
    calculate_delivery_cost,
    rate_by_cities,
    calculate_delevery_on_time,
    calculate_expedition_cost_by_rate,
)
from datetime import time


class RateTestCase(TestCase):
    def setUp(self) -> None:
        self.moskow = City.objects.create(name="Москва")
        self.belgorod = City.objects.create(name="Белгород")
        self.rate = Rate.objects.create(
            city_from=self.moskow,
            city_to=self.belgorod,
            cost_by_weight_0_25=Decimal("900"),
        )
        self.expedition_rate = ExpeditionRate.objects.create(
            city_to=self.belgorod,
            cost_by_weight_0_25=Decimal("1000"),
            cost_by_weight_25_50=Decimal("1400"),
            cost_by_weight_50_150=Decimal("1500"),
            cost_by_weight_150_300=Decimal("1800"),
            cost_by_weight_300_500=Decimal("2000"),
        )
        Const.objects.create(nigth_deliver_cost=Decimal("1000"))

    def test_find_moskow(self):
        moskow = city_by_name("Москва")
        self.assertEqual(moskow, self.moskow)

    def test_find_rate(self):
        rate = rate_by_cities(self.moskow, self.belgorod)
        self.assertEqual(rate, self.rate)

    def test_calculate_delivery_cost_by_rate(self):
        # Москва-Белгород
        self.assertEqual(
            calculate_delivery_cost_by_rate(self.rate, weight=Decimal("15")),
            Decimal("900"),
        )

    def test_calculate_expedition_cost_by_rate(self):
        # Москва-Белгород
        self.assertEqual(
            calculate_expedition_cost_by_rate(
                self.expedition_rate, weight=Decimal("15")
            ),
            Decimal("1000"),
        )
        self.assertEqual(
            calculate_expedition_cost_by_rate(
                self.expedition_rate, weight=Decimal("38")
            ),
            Decimal("1400"),
        )

    def test_calculate_delivery_cost(self):
        # Москва-Белгород
        self.assertEqual(
            calculate_delivery_cost(
                self.moskow.id, self.belgorod.id, weight=Decimal("15")
            ),
            Decimal("900"),
        )

    def test_calculate_delevery_on_time(self):
        self.assertEqual(
            calculate_delevery_on_time(deliver_time=time(22, 0, 0)), Decimal("1000")
        )
