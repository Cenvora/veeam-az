from enum import Enum


class RegionExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    SUBSCRIPTION = "Subscription"
    WORKERSUPPORT = "WorkerSupport"

    def __str__(self) -> str:
        return str(self.value)
