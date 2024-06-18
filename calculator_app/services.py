from decimal import Decimal
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
        rate = Rate.objects.filter(
            city_from=city_from, city_to=city_to
        ).first()
    except Rate.DoesNotExist:
        rate = None
    return rate


def calculate_cost_by_weight(rate: Rate, weight: Decimal) -> Decimal:
    docimal_0 = Decimal("0")
    if not rate:
        return docimal_0
    cost_by_weight = docimal_0
    if docimal_0 < weight <= rate.cost_by_weight_0_25:
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


def calculate_cost_by_volume(rate: Rate, volume: Decimal) -> Decimal:
    docimal_0 = Decimal("0")
    if not rate:
        return docimal_0
    cost_by_volume = docimal_0
    if docimal_0 < volume <= rate.cost_by_volume_0_01:
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
        weight: Decimal = 0,
        volume: Decimal = 0) -> Decimal:

    cost_by_weight = calculate_cost_by_weight(rate, weight)
    cost_by_volume = calculate_cost_by_volume(rate, volume)
    return max(cost_by_weight, cost_by_volume)


def calculate_delivery_cost(
        city_from_name: str,
        city_to_name: str,
        weight: Decimal = 0,
        volume: Decimal = 0) -> Decimal:

    city_from = city_by_name(city_name=city_from_name)
    city_to = city_by_name(city_name=city_to_name)
    rate = rate_by_cities(city_from=city_from, city_to=city_to)

    cost_by_weight = calculate_cost_by_weight(rate, weight)
    cost_by_volume = calculate_cost_by_volume(rate, volume)

    return max(cost_by_weight, cost_by_volume)


def calculate_delevery_on_time(deliver_time: time) -> Decimal:
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


def calculate_warehouse_process(volume: Decimal) -> Decimal:
    """
    Складская обработка грузов при местной (областной) доставке тогда
    {const.warehouse_process_cost} руб./куб. м. Минимальная стоимость
    тогда {const.min_warehouse_process_cost} руб."""
    const = Const.info()
    cost = const.warehouse_process_cost * volume
    if cost < const.min_warehouse_process_cost:
        cost = const.min_warehouse_process_cost
    return cost


def calculate_return_docs() -> Decimal:
    """
    Расчет стоимости возврата документов"""
    const = Const.info()
    return const.return_docs_cost


def calculate_insurance(declared_cost: Decimal) -> Decimal:
    """
    Расчет стоимости трахования груза"""
    const = Const.info()
    return declared_cost * (const.insurance_cost / 100)


def calculate_prr(weight: Decimal) -> Decimal:
    """
    Услуга ПРР"""
    const = Const.info()
    return weight * const.prr_cost


def calculate_hard_packaging(volume: Decimal) -> Decimal:
    """
    Расчет стоимости жесткой упаковки/обрешетки"""
    const = Const.info()
    cost = (volume * Decimal("1.3")) * const.hard_packaging_cost
    if cost < const.hard_packaging_min_cost:
        cost = const.hard_packaging_min_cost
    return cost


def calculate_soft_packaging(volume: Decimal) -> Decimal:
    """
    Расчет стоимости мягкой упаковки/пупырки"""
    const = Const.info()
    cost = (volume * Decimal("1.3")) * const.soft_packaging_cost
    if cost < const.soft_packaging_min_cost:
        cost = const.soft_packaging_min_cost
    return cost


def calculate_palletizing(volume: Decimal) -> Decimal:
    """
    Расчет стоимости паллетирования"""
    const = Const.info()
    cost = (volume * Decimal("1.3")) * const.palletizing_cost
    if cost < const.palletizing_min_cost:
        cost = const.palletizing_min_cost
    return cost


def calculate_base_cost(order: dict) -> Decimal:
    total_weight = (sum([item.get("weight", 0) for item in order["items"]]))
    total_volume = (sum([item.get("volume", 0) for item in order["items"]]))
    city_from = City.find_by_id(order.get("city_from_id"))
    city_to = City.find_by_id(order.get("city_to_id"))
    rate = rate_by_cities(city_from, city_to)
    return calculate_delivery_cost_by_rate(rate, total_weight, total_volume)


def calculate_order(order: dict) -> Decimal:
    """
    Расчет стоимсоти перевозки"""

    # Константа - полдень
    noon = time(12, 0, 0)
    # Расчет базовой стоимости по общему весу, объему и тарифам
    base_cost = calculate_base_cost(order)
    cost = base_cost
    # Расчет стоимсоти забора у двери по времени
    if order.get("from_address", False) and order.get("by_time_from", False):
        cost += calculate_delevery_on_time(order.get("time_from", noon))
    if order.get("to_address", False) and order.get("by_time_to", False):
        cost += calculate_delevery_on_time(order.get("time_to", noon))
    if order.get("return_docs", False):
        cost += calculate_return_docs()
    if order.get("insurance", False):
        cost += calculate_insurance((order.get("declared_cost", 0)))
    k_oversize = Decimal("1")
    for item in order["items"]:
        if item.get("prr_from", False) and\
            item.get("weight", 0) < Decimal("35") and\
                item.get("volume", 0) < Decimal("0.3"):
            cost += calculate_prr((item.get("weight", 0)))
        if item.get("prr_to", False) and\
            item.get("weight", 0) < Decimal("35") and\
                item.get("volume", 0) < Decimal("0.3"):
            cost += calculate_prr((item.get("weight", 0)))
        if item.get("hard_packaging", False):
            cost += calculate_hard_packaging((item.get("volume", 0)))
        if item.get("soft_packaging", False):
            cost += calculate_soft_packaging((item.get("volume", 0)))
        if item.get("palletizing", False):
            cost += calculate_palletizing((item.get("volume", 0)))
        k_oversize = max(k_oversize, calclulate_k_oversize(item))
    cost += base_cost * k_oversize
    return cost


def calclulate_k_oversize(item_order: dict) -> Decimal:
    k_oversize = Decimal("1")
    if condition_10(item_order):
        k_oversize = Decimal("1.1")
    if condition_20(item_order):
        k_oversize = Decimal("1.2")
    if condition_30(item_order):
        k_oversize = Decimal("1.3")
    if condition_50(item_order):
        k_oversize = Decimal("1.5")
    return k_oversize


def condition_10(item_order: dict) -> bool:
    return item_order.get("weight", 0) > 500 or\
        item_order.get("volume", 0) > 2 or\
        item_order.get("length", 0) > 3 or\
        item_order.get("width", 0) > 3 or\
        item_order.get("height", 0) > 3


def condition_20(item_order: dict) -> bool:
    return item_order.get("weight", 0) > 700 or\
        item_order.get("volume", 0) > 3 or\
        item_order.get("length", 0) > 4 or\
        item_order.get("width", 0) > 4 or\
        item_order.get("height", 0) > 4


def condition_30(item_order: dict) -> bool:
    return item_order.get("weight", 0) > 1000 or\
        item_order.get("volume", 0) > 4 or\
        item_order.get("length", 0) > 5 or\
        item_order.get("width", 0) > 5 or\
        item_order.get("height", 0) > 5


def condition_50(item_order: dict) -> bool:
    return item_order.get("weight", 0) > 1500 or\
        item_order.get("volume", 0) > 5 or\
        item_order.get("length", 0) > 7 or\
        item_order.get("width", 0) > 7 or\
        item_order.get("height", 0) > 7


def calculate_item_order(item_order: dict) -> Decimal:
    pass
