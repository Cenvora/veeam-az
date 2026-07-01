from enum import Enum


class CosmosDbEventsSort(str, Enum):
    EVENTTIMEASC = "EventTimeAsc"
    EVENTTIMEDESC = "EventTimeDesc"

    def __str__(self) -> str:
        return str(self.value)
