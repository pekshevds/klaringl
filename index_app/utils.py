from enum import Enum
from datetime import datetime


class TimeOfTheYear(Enum):
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"


def get_current_time_of_the_year() -> str:
    months = [
        TimeOfTheYear.WINTER,
        TimeOfTheYear.WINTER,
        TimeOfTheYear.WINTER,
        TimeOfTheYear.SPRING,
        TimeOfTheYear.SPRING,
        TimeOfTheYear.SPRING,
        TimeOfTheYear.SUMMER,
        TimeOfTheYear.SUMMER,
        TimeOfTheYear.SUMMER,
        TimeOfTheYear.AUTUMN,
        TimeOfTheYear.AUTUMN,
        TimeOfTheYear.AUTUMN,
    ]
    return months[datetime.now().month].value
