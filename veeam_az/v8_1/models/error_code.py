from enum import Enum


class ErrorCode(str, Enum):
    CANNOTACCESSTENANTOFEDITEDSERVICEACCOUNT = "CannotAccessTenantOfEditedServiceAccount"

    def __str__(self) -> str:
        return str(self.value)
