from datetime import time
from django.shortcuts import get_object_or_404
from calculator_app.models import (
    Rate,
    City
)
from index_app.models import Const


def city_by_name(city_name: str) -> City | None:
    try:
        city = get_object_or_404(City, name=city_name)
    except City.DoesNotExist:
        city = None
    return city


def rate_by_cities(city_from: City, city_to: City) -> Rate | None:
    try:
        # rate = get_object_or_404(Rate, city_from=city_from, city_to=city_to)
        rate = Rate.objects.filter(city_from=city_from, city_to=city_to).first()
    except Rate.DoesNotExist:
        rate = None
    return rate


def calculate_cost_by_weight(rate: Rate, weight: float) -> float:
    if not rate:
        return 0
    cost_by_weight = 0
    if 0 < weight <= float(rate.cost_by_weight_0_25):
        cost_by_weight = float(rate.cost_by_weight_0_25)

    if float(rate.cost_by_weight_0_25) < weight <= float(rate.cost_by_weight_25_50):
        cost_by_weight = float(rate.cost_by_weight_25_50)

    if float(rate.cost_by_weight_25_50) < weight <= float(rate.cost_by_weight_50_150):
        cost_by_weight = float(rate.cost_by_weight_50_150) * weight

    if float(rate.cost_by_weight_50_150) < weight <= float(rate.cost_by_weight_150_300):
        cost_by_weight = float(rate.cost_by_weight_150_300) * weight

    if float(rate.cost_by_weight_150_300) < weight <= float(rate.cost_by_weight_300_500):
        cost_by_weight = float(rate.cost_by_weight_300_500) * weight

    if float(rate.cost_by_weight_300_500) < weight <= float(rate.cost_by_weight_500_1000):
        cost_by_weight = float(rate.cost_by_weight_500_1000) * weight

    if float(rate.cost_by_weight_500_1000) < weight <= float(rate.cost_by_weight_1000_1500):
        cost_by_weight = float(rate.cost_by_weight_1000_1500) * weight

    if float(rate.cost_by_weight_1000_1500) < weight <= float(rate.cost_by_weight_1500_2000):
        cost_by_weight = float(rate.cost_by_weight_1500_2000) * weight

    if float(rate.cost_by_weight_1500_2000) < weight <= float(rate.cost_by_weight_2000_3000):
        cost_by_weight = float(rate.cost_by_weight_2000_3000) * weight

    if float(rate.cost_by_weight_2000_3000) < weight <= float(rate.cost_by_weight_3000_5000):
        cost_by_weight = float(rate.cost_by_weight_3000_5000) * weight

    if float(rate.cost_by_weight_3000_5000) < weight\
            <= float(rate.cost_by_weight_5000_10000):
        cost_by_weight = float(rate.cost_by_weight_5000_10000) * weight

    if weight > float(rate.cost_by_weight_10000_inf):
        cost_by_weight = float(rate.cost_by_weight_10000_inf) * weight
    return cost_by_weight


def calculate_cost_by_volume(rate: Rate, volume: float) -> float:
    if not rate:
        return 0
    cost_by_volume = 0
    if 0 < volume <= float(rate.cost_by_volume_0_01):
        cost_by_volume = float(rate.cost_by_volume_0_01) * volume

    if float(rate.cost_by_volume_0_01) < volume <= float(rate.cost_by_volume_01_02):
        cost_by_volume = float(rate.cost_by_volume_01_02) * volume

    if float(rate.cost_by_volume_01_02) < volume <= float(rate.cost_by_volume_02_06):
        cost_by_volume = float(rate.cost_by_volume_02_06) * volume

    if float(rate.cost_by_volume_02_06) < volume <= float(rate.cost_by_volume_06_12):
        cost_by_volume = float(rate.cost_by_volume_06_12) * volume

    if float(rate.cost_by_volume_06_12) < volume <= float(rate.cost_by_volume_12_20):
        cost_by_volume = float(rate.cost_by_volume_12_20) * volume

    if float(rate.cost_by_volume_12_20) < volume <= float(rate.cost_by_volume_20_40):
        cost_by_volume = float(rate.cost_by_volume_20_40) * volume

    if float(rate.cost_by_volume_20_40) < volume <= float(rate.cost_by_volume_40_60):
        cost_by_volume = float(rate.cost_by_volume_40_60) * volume

    if float(rate.cost_by_volume_40_60) < volume <= float(rate.cost_by_volume_60_80):
        cost_by_volume = float(rate.cost_by_volume_60_80) * volume

    if float(rate.cost_by_volume_60_80) < volume <= float(rate.cost_by_volume_80_120):
        cost_by_volume = float(rate.cost_by_volume_80_120) * volume

    if float(rate.cost_by_volume_80_120) < volume <= float(rate.cost_by_volume_120_200):
        cost_by_volume = float(rate.cost_by_volume_120_200) * volume

    if float(rate.cost_by_volume_120_200) < volume <= float(rate.cost_by_volume_200_400):
        cost_by_volume = float(rate.cost_by_volume_200_400) * volume

    if volume > float(rate.cost_by_volume_400_inf):
        cost_by_volume = float(rate.cost_by_volume_400_inf) * volume
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


def calculate_delevery_on_time(deliver_time: time) -> float:
    """
    Расчет необходимости и стоимости надбавки за ночную/вечернюю доставку"""
    const = Const.info()
    time_21 = time(21, 0, 0)
    time_09 = time(9, 0, 0)
    if deliver_time >= time_21:
        return const.nigth_deliver_cost
    if deliver_time < time_09:
        return const.nigth_deliver_cost
    return const.time_deliver_cost


def calculate_warehouse_process(volume: float) -> float:
    """
    Складская обработка грузов при местной (областной) доставке тогда
    {const.warehouse_process_cost} руб./куб. м. Минимальная стоимость
    тогда {const.min_warehouse_process_cost} руб."""
    const = Const.info()
    cost = const.warehouse_process_cost * volume
    if cost < const.min_warehouse_process_cost:
        cost = const.min_warehouse_process_cost
    return cost


def calculate_return_docs() -> float:
    """
    Расчет стоимости возврата документов"""
    const = Const.info()
    return const.return_docs_cost


def calculate_insurance(declared_cost: float) -> float:
    """
    Расчет стоимости трахования груза"""
    const = Const.info()
    return declared_cost * (const.insurance_cost / 100)


def calculate_prr(weight: float) -> float:
    """
    Услуга ПРР"""
    const = Const.info()
    return weight * const.prr_cost


def calculate_hard_packaging(volume: float) -> float:
    """
    Расчет стоимости жесткой упаковки/обрешетки"""
    const = Const.info()
    cost = (volume * 1.3) * const.hard_packaging_cost
    if cost < const.hard_packaging_min_cost:
        cost = const.hard_packaging_min_cost
    return cost


def calculate_base_cost(order: dict) -> float:
    total_weight = float(sum([item.get("weight", 0) for item in order["items"]]))
    total_volume = float(sum([item.get("volume", 0) for item in order["items"]]))
    city_from = City.find_by_id(order.get("city_from_id"))
    city_to = City.find_by_id(order.get("city_to_id"))
    rate = rate_by_cities(city_from, city_to)
    return calculate_delivery_cost_by_rate(rate, total_weight, total_volume)


def calculate_order(order: dict) -> float:
    noon = time(12, 0, 0)
    cost = calculate_base_cost(order)
    if order.get("from_address", False):
        cost += calculate_delevery_on_time(order.get("time_from", noon))
    if order.get("to_address", False):
        cost += calculate_delevery_on_time(order.get("time_to", noon))
    if order.get("return_docs", False):
        cost += calculate_return_docs()
    if order.get("insurance", False):
        cost += calculate_insurance(float(order.get("declared_cost", 0)))
    for item in order["items"]:
        if item.get("prr_from", False):
            cost += calculate_prr(float(item.get("weight", 0)))
    for item in order["items"]:
        if item.get("prr_to", False):
            cost += calculate_prr(float(item.get("weight", 0)))
        if item.get("hard_packaging", False):
            cost += calculate_hard_packaging(float(item.get("volume", 0)))
    return cost


def calculate_item_order(item_order: dict) -> float:
    pass