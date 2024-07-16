from rest_framework import serializers
from server.base_serializers import (
    DirectorySerializer,
    ItemSerializer,
    DocumentSerializer,
)
from order_app.models import Cargo, Order, ItemOrder
from calculator_app.models import City


class CargorSerializer(DirectorySerializer):
    weight = serializers.DecimalField(max_digits=15, decimal_places=2)
    length = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    width = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    height = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    volume = serializers.DecimalField(max_digits=15, decimal_places=5, required=False)

    def create(self, validated_data):
        return Cargo.objects.create(**validated_data)


class ItemOrderSerializer(ItemSerializer):
    cargo = CargorSerializer()
    hard_packaging = serializers.BooleanField(required=False)
    soft_packaging = serializers.BooleanField(required=False)
    palletizing = serializers.BooleanField(required=False)
    prr_from = serializers.BooleanField(required=False)
    prr_to = serializers.BooleanField(required=False)


class OrderSerializer(DocumentSerializer):
    # Отправитель
    city_from_id = serializers.UUIDField(
        format="hex_verbose", required=True
    )  # Город-отправитель

    from_address = serializers.BooleanField(required=False)  # Забор по адресу
    address_from = serializers.CharField(
        max_length=1024, required=False
    )  # Адрес забора
    date_from = serializers.DateField(required=False)  # Дата забора
    from_time = serializers.BooleanField(required=False)  # Забор по времени
    time_from = serializers.TimeField(required=False)  # Время забора
    form_from = serializers.CharField(
        max_length=2, required=True
    )  # Форма собственности
    name_from = serializers.CharField(max_length=255, required=True)  # Имя отправителя
    face_from = serializers.CharField(max_length=255, required=False)  # Контактное лицо
    tel_from = serializers.CharField(max_length=25, required=False)  # Телефон
    email_from = serializers.EmailField(max_length=25, required=False)  # Почта

    # Получатель
    city_to_id = serializers.UUIDField(
        format="hex_verbose", required=True
    )  # Город-получатель
    to_address = serializers.BooleanField(required=False)  # Доставка по адресу
    address_to = serializers.CharField(
        max_length=1024, required=False
    )  # Адрес доставки
    date_to = serializers.DateField(required=False)  # Дата доставки
    to_time = serializers.BooleanField(required=False)  # Доставка по времени
    time_to = serializers.TimeField(required=False)  # Время доставки
    form_to = serializers.CharField(max_length=2, required=True)  # Форма собственности
    name_to = serializers.CharField(max_length=255, required=True)  # Имя получателя
    face_to = serializers.CharField(max_length=255, required=False)  # Контактное лицо
    tel_to = serializers.CharField(max_length=25, required=False)  # Телефон
    email_to = serializers.EmailField(max_length=25, required=False)  # Почта

    payer = serializers.CharField(max_length=2, required=True)  # Плательщик
    form_payer = serializers.CharField(max_length=2, required=False)
    name_payer = serializers.CharField(max_length=255, required=False)
    face_payer = serializers.CharField(max_length=255, required=False)
    tel_payer = serializers.CharField(max_length=25, required=False)
    email_payer = serializers.EmailField(max_length=25, required=False)

    insurance = serializers.BooleanField(required=False)
    return_docs = serializers.BooleanField(required=False)
    declared_cost = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=True
    )
    cost = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    items = ItemOrderSerializer(many=True, required=False)

    def __fill_order(self, validated_data: dict) -> Order:
        order = Order()
        for key, value in validated_data.items():
            if key == "id":
                order = Order.objects.get(id=value)
                continue
            if key == "items":
                continue
            if key == "city_from_id":
                setattr(order, "city_from", City.find_by_id(id=value))
                continue
            if key == "city_to_id":
                setattr(order, "city_to", City.find_by_id(id=value))
                continue
            setattr(order, key, value)
        order.save()
        return order

    def __fill_cargo(self, validated_data: dict) -> Cargo:
        cargo = Cargo()
        for key, value in validated_data.items():
            setattr(cargo, key, value)
        cargo.save()
        return cargo

    def __fill_item_order(
        self, order: Order, cargo: Cargo, validated_data: dict
    ) -> ItemOrder:
        item_cargo = ItemOrder(order=order, cargo=cargo)
        for key, value in validated_data.items():
            if key == "cargo":
                continue
            setattr(item_cargo, key, value)
        item_cargo.save()
        return item_cargo

    def create(self, validated_data: dict) -> Order:
        order = self.__fill_order(validated_data)
        for item in validated_data["items"]:
            cargo = self.__fill_cargo(item["cargo"])
            self.__fill_item_order(order, cargo, item)
        return order
