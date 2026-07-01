from enum import Enum


class CosmosDbCapacityMode(str, Enum):
    NONE = "None"
    PROVISIONED = "Provisioned"
    SERVERLESS = "Serverless"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
