from django.shortcuts import get_object_or_404
from calculator_app.models import (
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


def calculate_cost_by_weight(rate: Rate, weight: float) -> float:
    if not rate:
        return 0
    cost_by_weight = 0
    if 0 < weight <= rate.cost_by_weight_0_25:
        cost_by_weight = rate.cost_by_weight_0_25

    if rate.cost_by_weight_0_25 < weight <= rate.cost_by_weight_25_50:
        cost_by_weight = rate.cost_by_weight_25_50

    if rate.cost_by_weight_25_50 < weight <= rate.cost_by_weight_50_150:
        cost_by_weight = rate.cost_by_weight_50_150 * weight

    if rate.cost_by_weight_50_150 < weight <= rate.cost_by_weight_150_300:
        cost_by_weight = rate.cost_by_weight_150_300 * weight

    if rate.cost_by_weight_150_300 < weight <= rate.cost_by_weight_300_500:
        cost_by_weight = rate.cost_by_weight_300_500 * weight

    if rate.cost_by_weight_300_500 < weight <= rate.cost_by_weight_500_1000:
        cost_by_weight = rate.cost_by_weight_500_1000 * weight

    if rate.cost_by_weight_500_1000 < weight <= rate.cost_by_weight_1000_1500:
        cost_by_weight = rate.cost_by_weight_1000_1500 * weight

    if rate.cost_by_weight_1000_1500 < weight <= rate.cost_by_weight_1500_2000:
        cost_by_weight = rate.cost_by_weight_1500_2000 * weight

    if rate.cost_by_weight_1500_2000 < weight <= rate.cost_by_weight_2000_3000:
        cost_by_weight = rate.cost_by_weight_2000_3000 * weight

    if rate.cost_by_weight_2000_3000 < weight <= rate.cost_by_weight_3000_5000:
        cost_by_weight = rate.cost_by_weight_3000_5000 * weight

    if rate.cost_by_weight_3000_5000 < weight\
            <= rate.cost_by_weight_5000_10000:
        cost_by_weight = rate.cost_by_weight_5000_10000 * weight

    if weight > rate.cost_by_weight_10000_inf:
        cost_by_weight = rate.cost_by_weight_10000_inf * weight
    return cost_by_weight


def calculate_cost_by_volume(rate: Rate, volume: float) -> float:
    if not rate:
        return 0
    cost_by_volume = 0
    if 0 < volume <= rate.cost_by_volume_0_01:
        cost_by_volume = rate.cost_by_volume_0_01 * volume

    if rate.cost_by_volume_0_01 < volume <= rate.cost_by_volume_01_02:
        cost_by_volume = rate.cost_by_volume_01_02 * volume

    if rate.cost_by_volume_01_02 < volume <= rate.cost_by_volume_02_06:
        cost_by_volume = rate.cost_by_volume_02_06 * volume

    if rate.cost_by_volume_02_06 < volume <= rate.cost_by_volume_06_12:
        cost_by_volume = rate.cost_by_volume_06_12 * volume

    if rate.cost_by_volume_06_12 < volume <= rate.cost_by_volume_12_20:
        cost_by_volume = rate.cost_by_volume_12_20 * volume

    if rate.cost_by_volume_12_20 < volume <= rate.cost_by_volume_20_40:
        cost_by_volume = rate.cost_by_volume_20_40 * volume

    if rate.cost_by_volume_20_40 < volume <= rate.cost_by_volume_40_60:
        cost_by_volume = rate.cost_by_volume_40_60 * volume

    if rate.cost_by_volume_40_60 < volume <= rate.cost_by_volume_60_80:
        cost_by_volume = rate.cost_by_volume_60_80 * volume

    if rate.cost_by_volume_60_80 < volume <= rate.cost_by_volume_80_120:
        cost_by_volume = rate.cost_by_volume_80_120 * volume

    if rate.cost_by_volume_80_120 < volume <= rate.cost_by_volume_120_200:
        cost_by_volume = rate.cost_by_volume_120_200 * volume

    if rate.cost_by_volume_120_200 < volume <= rate.cost_by_volume_200_400:
        cost_by_volume = rate.cost_by_volume_200_400 * volume

    if volume > rate.cost_by_volume_400_inf:
        cost_by_volume = rate.cost_by_volume_400_inf * volume
    return cost_by_volume


def calculate_delivery_cost_by_rate(
        rate: Rate,
        weight: float = 0, volume: float = 0) -> float:

    cost_by_weight = calculate_cost_by_weight(rate, weight)
    cost_by_volume = calculate_cost_by_volume(rate, volume)

    return max(cost_by_weight, cost_by_volume)


def calculate_delivery_cost(
        city_from_name: str,
        city_to_name: str,
        weight: float = 0, volume: float = 0) -> float:

    city_from = city_by_name(city_name=city_from_name)
    city_to = city_by_name(city_name=city_to_name)
    rate = rate_by_cities(city_from=city_from, city_to=city_to)

    cost_by_weight = calculate_cost_by_weight(rate, weight)
    cost_by_volume = calculate_cost_by_volume(rate, volume)

    return max(cost_by_weight, cost_by_volume)
