from enum import Enum


class ResourceGroupSort(str, Enum):
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LOCATIONASC = "LocationAsc"
    LOCATIONDESC = "LocationDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    SUBSCRIPTIONNAMEASC = "SubscriptionNameAsc"
    SUBSCRIPTIONNAMEDESC = "SubscriptionNameDesc"

    def __str__(self) -> str:
        return str(self.value)
