from enum import Enum


class VirtualNetworkExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    RESOURCEGROUP = "ResourceGroup"
    SUBNETS = "Subnets"

    def __str__(self) -> str:
        return str(self.value)
