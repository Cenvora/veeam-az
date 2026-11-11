from enum import Enum


class VirtualMachineExpansion(str, Enum):
    ACCOUNT = "Account"
    ALL = "All"
    NONE = "None"
    PROTECTIONSTATE = "ProtectionState"
    REGION = "Region"
    RESOURCEGROUP = "ResourceGroup"
    SUBSCRIPTION = "Subscription"

    def __str__(self) -> str:
        return str(self.value)
