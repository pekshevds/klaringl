from rest_framework import serializers
from server.base_serializers import DirectorySerializer, BaseSerializer
from calculator_app.models import City, Rate, ExpeditionRate


class ItemCalculateRequestSerializer(serializers.Serializer):
    hard_packaging = serializers.BooleanField(required=False)
    soft_packaging = serializers.BooleanField(required=False)
    palletizing = serializers.BooleanField(required=False)
    prr_from = serializers.BooleanField(required=False)
    prr_to = serializers.BooleanField(required=False)
    weight = serializers.DecimalField(max_digits=15, decimal_places=2)
    length = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    width = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    height = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    volume = serializers.DecimalField(max_digits=15, decimal_places=5, required=False)


class CalculateRequestSerializer(serializers.Serializer):
    city_from_id = serializers.UUIDField()
    city_to_id = serializers.UUIDField()

    from_address = serializers.BooleanField()
    date_from = serializers.DateField(required=False)
    by_time_from = serializers.BooleanField()
    time_from = serializers.TimeField(required=False)

    to_address = serializers.BooleanField()
    date_to = serializers.DateField(required=False)
    by_time_to = serializers.BooleanField()
    time_to = serializers.TimeField(required=False)

    insurance = serializers.BooleanField()
    return_docs = serializers.BooleanField()
    declared_cost = serializers.DecimalField(max_digits=15, decimal_places=2)
    items = ItemCalculateRequestSerializer(many=True)


class FastCalculateRequestSerializer(serializers.Serializer):
    city_from_id = serializers.UUIDField()
    city_to_id = serializers.UUIDField()
    weight = serializers.DecimalField(max_digits=15, decimal_places=2)
    volume = serializers.DecimalField(max_digits=15, decimal_places=2)


class FastCalculateRequest2Serializer(serializers.Serializer):
    city_from_id = serializers.UUIDField()
    city_to_id = serializers.UUIDField()
    weight = serializers.DecimalField(max_digits=15, decimal_places=2)
    volume = serializers.DecimalField(max_digits=15, decimal_places=2)
    from_address = serializers.BooleanField()
    to_address = serializers.BooleanField()


class CalculateResponseSerializer(serializers.Serializer):
    cost = serializers.DecimalField(max_digits=15, decimal_places=2)


class CitySerializer(DirectorySerializer):
    def create(self, validated_data):
        city_id = validated_data.get("id")
        city, _ = City.objects.get_or_create(id=city_id)
        city.name = validated_data.get("name", city.name)
        city.save()
        return city


class RateSerializer(BaseSerializer):
    city_from = CitySerializer()
    city_to = CitySerializer()
    delivery_time = serializers.CharField(required=False, allow_null=True)
    shipping_schedule = serializers.CharField(required=False, allow_null=True)

    cost_by_weight_0_25 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_25_50 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_50_150 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_150_300 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_300_500 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_500_1000 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_1000_1500 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_1500_2000 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_2000_3000 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_3000_5000 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_5000_10000 = serializers.DecimalField(
        max_digits=15, decimal_places=2
    )
    cost_by_weight_10000_inf = serializers.DecimalField(max_digits=15, decimal_places=2)

    cost_by_volume_0_01 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_01_02 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_02_06 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_06_12 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_12_20 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_20_40 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_40_60 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_60_80 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_80_120 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_120_200 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_200_400 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_400_inf = serializers.DecimalField(max_digits=15, decimal_places=2)

    def create(self, validated_data):
        serializer = CitySerializer(data=validated_data.get("city_from"))
        serializer.is_valid(raise_exception=True)
        city_from = serializer.save()

        serializer = CitySerializer(data=validated_data.get("city_to"))
        serializer.is_valid(raise_exception=True)
        city_to = serializer.save()

        rate, _ = Rate.objects.get_or_create(city_from=city_from, city_to=city_to)
        rate.cost_by_weight_0_25 = validated_data.get(
            "cost_by_weight_0_25", rate.cost_by_weight_0_25
        )
        rate.cost_by_weight_25_50 = validated_data.get(
            "cost_by_weight_25_50", rate.cost_by_weight_25_50
        )
        rate.cost_by_weight_50_150 = validated_data.get(
            "cost_by_weight_50_150", rate.cost_by_weight_50_150
        )
        rate.cost_by_weight_150_300 = validated_data.get(
            "cost_by_weight_150_300", rate.cost_by_weight_150_300
        )
        rate.cost_by_weight_300_500 = validated_data.get(
            "cost_by_weight_300_500", rate.cost_by_weight_300_500
        )
        rate.cost_by_weight_500_1000 = validated_data.get(
            "cost_by_weight_500_1000", rate.cost_by_weight_500_1000
        )
        rate.cost_by_weight_1000_1500 = validated_data.get(
            "cost_by_weight_1000_1500", rate.cost_by_weight_1000_1500
        )
        rate.cost_by_weight_1500_2000 = validated_data.get(
            "cost_by_weight_1500_2000", rate.cost_by_weight_1500_2000
        )
        rate.cost_by_weight_2000_3000 = validated_data.get(
            "cost_by_weight_2000_3000", rate.cost_by_weight_2000_3000
        )
        rate.cost_by_weight_3000_5000 = validated_data.get(
            "cost_by_weight_3000_5000", rate.cost_by_weight_3000_5000
        )
        rate.cost_by_weight_5000_10000 = validated_data.get(
            "cost_by_weight_5000_10000", rate.cost_by_weight_5000_10000
        )
        rate.cost_by_weight_10000_inf = validated_data.get(
            "cost_by_weight_10000_inf", rate.cost_by_weight_10000_inf
        )

        rate.cost_by_volume_0_01 = validated_data.get(
            "cost_by_volume_0_01", rate.cost_by_volume_0_01
        )
        rate.cost_by_volume_01_02 = validated_data.get(
            "cost_by_volume_01_02", rate.cost_by_volume_01_02
        )
        rate.cost_by_volume_02_06 = validated_data.get(
            "cost_by_volume_02_06", rate.cost_by_volume_02_06
        )
        rate.cost_by_volume_06_12 = validated_data.get(
            "cost_by_volume_06_12", rate.cost_by_volume_06_12
        )
        rate.cost_by_volume_12_20 = validated_data.get(
            "cost_by_volume_12_20", rate.cost_by_volume_12_20
        )
        rate.cost_by_volume_20_40 = validated_data.get(
            "cost_by_volume_20_40", rate.cost_by_volume_20_40
        )
        rate.cost_by_volume_40_60 = validated_data.get(
            "cost_by_volume_40_60", rate.cost_by_volume_40_60
        )
        rate.cost_by_volume_60_80 = validated_data.get(
            "cost_by_volume_60_80", rate.cost_by_volume_60_80
        )
        rate.cost_by_volume_80_120 = validated_data.get(
            "cost_by_volume_80_120", rate.cost_by_volume_80_120
        )
        rate.cost_by_volume_120_200 = validated_data.get(
            "cost_by_volume_120_200", rate.cost_by_volume_120_200
        )
        rate.cost_by_volume_200_400 = validated_data.get(
            "cost_by_volume_200_400", rate.cost_by_volume_200_400
        )
        rate.cost_by_volume_400_inf = validated_data.get(
            "cost_by_volume_400_inf", rate.cost_by_volume_400_inf
        )
        rate.save()
        return rate


class ExpeditionRateSerializer(BaseSerializer):
    city_to = CitySerializer()

    cost_by_weight_0_25 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_25_50 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_50_150 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_150_300 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_300_500 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_500_1000 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_1000_1500 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_1500_2000 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_2000_3000 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_3000_5000 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_weight_5000_10000 = serializers.DecimalField(
        max_digits=15, decimal_places=2
    )
    cost_by_weight_10000_inf = serializers.DecimalField(max_digits=15, decimal_places=2)

    cost_by_volume_0_01 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_01_02 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_02_06 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_06_12 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_12_20 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_20_40 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_40_60 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_60_80 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_80_120 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_120_200 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_200_400 = serializers.DecimalField(max_digits=15, decimal_places=2)
    cost_by_volume_400_inf = serializers.DecimalField(max_digits=15, decimal_places=2)

    def create(self, validated_data):
        serializer = CitySerializer(data=validated_data.get("city_to"))
        serializer.is_valid(raise_exception=True)
        city_to = serializer.save()

        rate, _ = ExpeditionRate.objects.get_or_create(city_to=city_to)
        rate.cost_by_weight_0_25 = validated_data.get(
            "cost_by_weight_0_25", rate.cost_by_weight_0_25
        )
        rate.cost_by_weight_25_50 = validated_data.get(
            "cost_by_weight_25_50", rate.cost_by_weight_25_50
        )
        rate.cost_by_weight_50_150 = validated_data.get(
            "cost_by_weight_50_150", rate.cost_by_weight_50_150
        )
        rate.cost_by_weight_150_300 = validated_data.get(
            "cost_by_weight_150_300", rate.cost_by_weight_150_300
        )
        rate.cost_by_weight_300_500 = validated_data.get(
            "cost_by_weight_300_500", rate.cost_by_weight_300_500
        )
        rate.cost_by_weight_500_1000 = validated_data.get(
            "cost_by_weight_500_1000", rate.cost_by_weight_500_1000
        )
        rate.cost_by_weight_1000_1500 = validated_data.get(
            "cost_by_weight_1000_1500", rate.cost_by_weight_1000_1500
        )
        rate.cost_by_weight_1500_2000 = validated_data.get(
            "cost_by_weight_1500_2000", rate.cost_by_weight_1500_2000
        )
        rate.cost_by_weight_2000_3000 = validated_data.get(
            "cost_by_weight_2000_3000", rate.cost_by_weight_2000_3000
        )
        rate.cost_by_weight_3000_5000 = validated_data.get(
            "cost_by_weight_3000_5000", rate.cost_by_weight_3000_5000
        )
        rate.cost_by_weight_5000_10000 = validated_data.get(
            "cost_by_weight_5000_10000", rate.cost_by_weight_5000_10000
        )
        rate.cost_by_weight_10000_inf = validated_data.get(
            "cost_by_weight_10000_inf", rate.cost_by_weight_10000_inf
        )

        rate.cost_by_volume_0_01 = validated_data.get(
            "cost_by_volume_0_01", rate.cost_by_volume_0_01
        )
        rate.cost_by_volume_01_02 = validated_data.get(
            "cost_by_volume_01_02", rate.cost_by_volume_01_02
        )
        rate.cost_by_volume_02_06 = validated_data.get(
            "cost_by_volume_02_06", rate.cost_by_volume_02_06
        )
        rate.cost_by_volume_06_12 = validated_data.get(
            "cost_by_volume_06_12", rate.cost_by_volume_06_12
        )
        rate.cost_by_volume_12_20 = validated_data.get(
            "cost_by_volume_12_20", rate.cost_by_volume_12_20
        )
        rate.cost_by_volume_20_40 = validated_data.get(
            "cost_by_volume_20_40", rate.cost_by_volume_20_40
        )
        rate.cost_by_volume_40_60 = validated_data.get(
            "cost_by_volume_40_60", rate.cost_by_volume_40_60
        )
        rate.cost_by_volume_60_80 = validated_data.get(
            "cost_by_volume_60_80", rate.cost_by_volume_60_80
        )
        rate.cost_by_volume_80_120 = validated_data.get(
            "cost_by_volume_80_120", rate.cost_by_volume_80_120
        )
        rate.cost_by_volume_120_200 = validated_data.get(
            "cost_by_volume_120_200", rate.cost_by_volume_120_200
        )
        rate.cost_by_volume_200_400 = validated_data.get(
            "cost_by_volume_200_400", rate.cost_by_volume_200_400
        )
        rate.cost_by_volume_400_inf = validated_data.get(
            "cost_by_volume_400_inf", rate.cost_by_volume_400_inf
        )
        rate.save()
        return rate
