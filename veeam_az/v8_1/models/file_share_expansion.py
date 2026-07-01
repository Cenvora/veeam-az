from enum import Enum


class FileShareExpansion(str, Enum):
    ACCOUNT = "Account"
    ALL = "All"
    NONE = "None"
    PROTECTIONSTATE = "ProtectionState"
    SUBSCRIPTION = "Subscription"

    def __str__(self) -> str:
        return str(self.value)
