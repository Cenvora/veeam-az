from enum import Enum


class ContainerImmutabilityPolicyState(str, Enum):
    LOCKED = "Locked"
    NOTPRESENT = "NotPresent"
    UNLOCKED = "Unlocked"

    def __str__(self) -> str:
        return str(self.value)
