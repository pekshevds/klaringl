from django.test import TestCase
from order_app.services import fetch_order_status_by_number


class TestOrder(TestCase):
    def setUp(self):
        pass

    def test_fetch_order_status_by_number1(self):
        self.assertEqual(
            fetch_order_status_by_number("24/00004872") == "Груз передан на маршрут",
            True,
        )

    def test_fetch_order_status_by_number2(self):
        self.assertEqual(
            fetch_order_status_by_number("24/00004824") != "Груз передан на маршрут",
            True,
        )
