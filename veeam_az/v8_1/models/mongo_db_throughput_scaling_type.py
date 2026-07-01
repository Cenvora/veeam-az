from enum import Enum


class MongoDbThroughputScalingType(str, Enum):
    AUTOSCALE = "Autoscale"
    MANUAL = "Manual"

    def __str__(self) -> str:
        return str(self.value)
