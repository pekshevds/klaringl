from rest_framework import serializers
from server.base_serializers import (
    DirectorySerializer,
    ItemSerializer,
    DocumentSerializer
)
from order_app.models import (
    Cargo,
    Order
)


class CargorSerializer(DirectorySerializer):
    weight = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    length = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    width = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    height = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    volume = serializers.DecimalField(
        max_digits=15, decimal_places=5)
    seats = serializers.IntegerField()

    def create(self, validated_data):
        return Cargo.objects.create(**validated_data)


class OrderSerializer(DocumentSerializer):
    city_from_id = serializers.UUIDField()
    from_address = serializers.BooleanField(required=False)
    address_from = serializers.CharField(max_length=1024, required=False)
    date_from = serializers.DateField(required=False)
    time_from = serializers.CharField(max_length=2, required=False)
    form_from = serializers.CharField(max_length=2, required=False)
    name_from = serializers.CharField(max_length=255, required=False)
    face_from = serializers.CharField(max_length=255, required=False)
    tel_from = serializers.CharField(max_length=25, required=False)
    email_from = serializers.EmailField(max_length=25, required=False)

    city_to_id = serializers.UUIDField()
    to_address = serializers.BooleanField(required=False)
    address_to = serializers.CharField(max_length=1024, required=False)
    date_to = serializers.DateField(required=False)
    time_to = serializers.CharField(max_length=2, required=False)
    form_to = serializers.CharField(max_length=2, required=False)
    name_to = serializers.CharField(max_length=255, required=False)
    face_to = serializers.CharField(max_length=255, required=False)
    tel_to = serializers.CharField(max_length=25, required=False)
    email_to = serializers.EmailField(max_length=25, required=False)

    payer = serializers.CharField(max_length=2, required=False)
    form_payer = serializers.CharField(max_length=2)
    name_payer = serializers.CharField(max_length=255, required=False)
    face_payer = serializers.CharField(max_length=255, required=False)
    tel_payer = serializers.CharField(max_length=25, required=False)
    email_payer = serializers.EmailField(max_length=25, required=False)

    insurance = serializers.BooleanField(required=False)
    return_docs = serializers.BooleanField(required=False)
    declared_cost = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    cost = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class ItemOrderSerializer(ItemSerializer):
    order_id = serializers.UUIDField()
    cargo_id = serializers.UUIDField()
    soft_packaging = serializers.BooleanField(required=False)
    crate = serializers.BooleanField(required=False)
    palletizing = serializers.BooleanField(required=False)
    pallet_board = serializers.BooleanField(required=False)
    seal_bag = serializers.BooleanField(required=False)
    cardboard_box = serializers.BooleanField(required=False)
    high_security_cargo = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
