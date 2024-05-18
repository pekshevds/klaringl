from django.db.models import Model
from calculator_app.services import rate_by_cities, calculate_delivery_cost


def ganerate_new_number(model: Model) -> int:
    """Вычисляет максимальный (последний) номер документа для модели model
    и возвращает следующий. Если последний номер 345, то вернет 346.
    """
    last_order = model.objects.all().order_by("number").last()
    if last_order:
        return last_order.number + 1
    return 1


def calculate_order_cost(order: Model) -> float:
    rate = rate_by_cities(order.city_from, order.city_to)
    if not rate:
        return 0
    weight = 0
    volume = 0
    for item in order.items.all():
        weight += item.cargo.weight
        volume += item.cargo.volume
    return calculate_delivery_cost(rate, weight, volume)
