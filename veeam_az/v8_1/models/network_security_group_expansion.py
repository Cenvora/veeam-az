from enum import Enum


class NetworkSecurityGroupExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    RESOURCEGROUP = "ResourceGroup"
    SUBSCRIPTION = "Subscription"

    def __str__(self) -> str:
        return str(self.value)
