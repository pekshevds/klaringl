from django.shortcuts import get_object_or_404
from order_app.models import (
    Rate,
    City
)


def city_by_name(city_name: str) -> City | None:
    try:
        city = get_object_or_404(City, name=city_name)
    except City.DoesNotExist:
        city = None
    return city


def rate_by_cities(city_from: City, city_to: City) -> Rate | None:
    try:
        rate = get_object_or_404(Rate, city_from=city_from, city_to=city_to)
    except City.DoesNotExist:
        rate = None
    return rate


def calculate_delivery_cost(
        rate: Rate,
        weight: float = 0, volume: float = 0) -> float:

    cost_by_weight = 0
    if weight > rate.cost_by_weight_10000_inf:
        cost_by_weight = rate.cost_by_weight_10000_inf

    if weight > 0 and weight <= rate.cost_by_weight_0_25:
        cost_by_weight = rate.cost_by_weight_0_25

    if weight > rate.cost_by_weight_0_25 and\
            weight <= rate.cost_by_weight_25_50:
        cost_by_weight = rate.cost_by_weight_25_50

    if weight > rate.cost_by_weight_25_50 and\
            weight <= rate.cost_by_weight_50_150:
        cost_by_weight = rate.cost_by_weight_50_150

    if weight > rate.cost_by_weight_50_150 and\
            weight <= rate.cost_by_weight_150_300:
        cost_by_weight = rate.cost_by_weight_150_300

    if weight > rate.cost_by_weight_150_300 and\
            weight <= rate.cost_by_weight_300_500:
        cost_by_weight = rate.cost_by_weight_300_500

    if weight > rate.cost_by_weight_300_500 and\
            weight <= rate.cost_by_weight_500_1000:
        cost_by_weight = rate.cost_by_weight_500_1000

    if weight > rate.cost_by_weight_500_1000 and\
            weight <= rate.cost_by_weight_1000_1500:
        cost_by_weight = rate.cost_by_weight_1000_1500

    if weight > rate.cost_by_weight_1000_1500 and\
            weight <= rate.cost_by_weight_1500_2000:
        cost_by_weight = rate.cost_by_weight_1500_2000

    if weight > rate.cost_by_weight_1500_2000 and\
            weight <= rate.cost_by_weight_2000_3000:
        cost_by_weight = rate.cost_by_weight_2000_3000

    if weight > rate.cost_by_weight_2000_3000 and\
            weight <= rate.cost_by_weight_3000_5000:
        cost_by_weight = rate.cost_by_weight_3000_5000

    if weight > rate.cost_by_weight_3000_5000 and\
            weight <= rate.cost_by_weight_5000_10000:
        cost_by_weight = rate.cost_by_weight_5000_10000

    cost_by_volume = 0

    return max(cost_by_weight, cost_by_volume)
