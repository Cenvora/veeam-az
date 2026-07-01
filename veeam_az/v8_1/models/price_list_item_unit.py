from enum import Enum


class PriceListItemUnit(str, Enum):
    ONEGB = "OneGb"
    ONEGBPERMONTH = "OneGbPerMonth"
    ONEHOUR = "OneHour"
    TENKILO = "TenKilo"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
