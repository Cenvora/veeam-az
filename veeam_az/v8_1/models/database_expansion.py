from enum import Enum


class DatabaseExpansion(str, Enum):
    ACCOUNT = "Account"
    ALL = "All"
    NONE = "None"
    PROTECTIONSTATE = "ProtectionState"
    REGION = "Region"
    RESOURCEGROUP = "ResourceGroup"
    SERVER = "Server"
    SUBSCRIPTION = "Subscription"

    def __str__(self) -> str:
        return str(self.value)
