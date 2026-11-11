from enum import Enum


class CostEstimationSchedulePeriod(str, Enum):
    DAILY = "Daily"
    MONTHLY = "Monthly"
    UNKNOWN = "Unknown"
    WEEKLY = "Weekly"
    YEARLY = "Yearly"

    def __str__(self) -> str:
        return str(self.value)
