from rest_framework import serializers
from server.base_serializers import (
    DirectorySerializer,
    BaseSerializer
)
from calculator_app.models import City


class CitySerializer(DirectorySerializer):

    def create(self, validated_data):
        """books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)"""
        name = validated_data["name"]
        city = City.find_by_name(name=name)
        if not city:
            city = City.objects.create(**validated_data)
        return city


class RateSerializer(BaseSerializer):
    city_from = CitySerializer()
    city_to = CitySerializer()
    delivery_time = serializers.CharField()
    shipping_schedule = serializers.CharField()

    cost_by_weight_0_25 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_25_50 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_50_150 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_150_300 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_300_500 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_500_1000 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_1000_1500 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_1500_2000 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_2000_3000 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_3000_5000 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_5000_10000 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_weight_10000_inf = serializers.DecimalField(
        max_digits=15, decimal_places=2)

    cost_by_volume_0_01 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_01_02 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_02_06 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_06_12 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_12_20 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_20_40 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_40_60 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_60_80 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_80_120 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_120_200 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_200_400 = serializers.DecimalField(
        max_digits=15, decimal_places=2)
    cost_by_volume_400_inf = serializers.DecimalField(
        max_digits=15, decimal_places=2)
