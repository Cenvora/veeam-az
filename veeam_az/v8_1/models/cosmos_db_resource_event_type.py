from enum import Enum


class CosmosDbResourceEventType(str, Enum):
    CREATE = "Create"
    DELETE = "Delete"
    RECREATE = "Recreate"
    REPLACE = "Replace"
    SYSTEMOPERATION = "SystemOperation"

    def __str__(self) -> str:
        return str(self.value)
