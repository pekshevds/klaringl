from django.test import TestCase
from order_app.services import fetch_order_status_by_number, fetch_customer_orders


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

    def test_fetch_customer_orders(self):
        self.assertEqual(
            fetch_customer_orders(
                customer_id="0323abb1-851e-11ee-a0dc-b06ebf81cc50",
                date_from="2024-05-01",
                date_to="2024-07-30",
            )
            is not None,
            True,
        )
