from django.shortcuts import get_object_or_404
import csv
from order_app.models import (
    City,
    Rate
)

cities = {}


def get_moskow():
    return get_object_or_404(City, name="Москва")


def str_to_dec(str_in: str) -> float:
    return float(str_in.replace(",", "."))


def load():
    moskow = get_moskow()
    with open("server/rates.csv", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for line in reader:
            city_name = line[0]
            city = cities.get(city_name)
            if not city:
                city = City.objects.create(name=city_name)
                cities[city_name] = city
            Rate.objects.create(
                city_from=moskow,
                city_to=city,
                delivery_time=line[1],
                shipping_schedule=line[2],
                cost_by_weight_0_25=str_to_dec(line[3]),
                cost_by_weight_25_50=str_to_dec(line[4]),
                cost_by_weight_50_150=str_to_dec(line[5]),
                cost_by_weight_150_300=str_to_dec(line[6]),
                cost_by_weight_300_500=str_to_dec(line[7]),
                cost_by_weight_500_1000=str_to_dec(line[8]),
                cost_by_weight_1000_1500=str_to_dec(line[9]),
                cost_by_weight_1500_2000=str_to_dec(line[10]),
                cost_by_weight_2000_3000=str_to_dec(line[11]),
                cost_by_weight_3000_5000=str_to_dec(line[12]),
                cost_by_weight_5000_10000=str_to_dec(line[13]),
                cost_by_weight_10000_inf=str_to_dec(line[14]),
                cost_by_volume_0_01=str_to_dec(line[15]),
                cost_by_volume_01_02=str_to_dec(line[16]),
                cost_by_volume_02_06=str_to_dec(line[17]),
                cost_by_volume_06_12=str_to_dec(line[18]),
                cost_by_volume_12_20=str_to_dec(line[19]),
                cost_by_volume_20_40=str_to_dec(line[20]),
                cost_by_volume_40_60=str_to_dec(line[21]),
                cost_by_volume_60_80=str_to_dec(line[22]),
                cost_by_volume_80_120=str_to_dec(line[23]),
                cost_by_volume_120_200=str_to_dec(line[24]),
                cost_by_volume_200_400=str_to_dec(line[25]),
                cost_by_volume_400_inf=str_to_dec(line[26])
                )
