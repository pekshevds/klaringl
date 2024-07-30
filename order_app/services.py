import requests
import config
from requests.auth import HTTPBasicAuth
from decimal import Decimal
from django.db.models import Model
from calculator_app.services import rate_by_cities, calculate_delivery_cost_by_rate


def ganerate_new_number(model: Model) -> int:
    """Вычисляет максимальный (последний) номер документа для модели model
    и возвращает следующий. Если последний номер 345, то вернет 346.
    """
    last_order = model.objects.all().order_by("number").last()
    if last_order:
        return last_order.number + 1
    return 1


def calculate_order_cost(order: Model) -> Decimal:
    decimal_0 = Decimal("0")
    rate = rate_by_cities(order.city_from, order.city_to)
    if not rate:
        return decimal_0
    weight = decimal_0
    volume = decimal_0
    for item in order.items.all():
        weight += item.cargo.weight
        volume += item.cargo.volume
    return calculate_delivery_cost_by_rate(rate, weight, volume)


def fetch_order_status_by_number(order_number: str) -> str:
    url = f"http://{config.ENTERPRISE_HOST}:{config.ENTERPRISE_PORT}/OLK/hs/orders/check-status/?num={order_number}"
    headers = {"content-type": "application/json; charset=utf8"}
    basic = HTTPBasicAuth(config.ENTERPRISE_USER, config.ENTERPRISE_PASSWORD)
    responce = requests.get(url=url, headers=headers, auth=basic)
    status = "неопределен, проверьте правильность введеного номера"
    if responce.ok:
        data = responce.json()
        status = data.get("status") if data.get("status") != "" else status
    return status


def fetch_customer_orders(
    customer_id: str, date_from: str, date_to: str
) -> dict | None:
    url = f"http://{config.ENTERPRISE_HOST}:{config.ENTERPRISE_PORT}/OLK/hs/orders/orders/?id={customer_id}&from=\
        {date_from}&to={date_to}"
    headers = {"content-type": "application/json; charset=utf8"}
    basic = HTTPBasicAuth(config.ENTERPRISE_USER, config.ENTERPRISE_PASSWORD)
    responce = requests.get(url=url, headers=headers, auth=basic)
    data = None
    if responce.ok:
        data = responce.json()
    return data
