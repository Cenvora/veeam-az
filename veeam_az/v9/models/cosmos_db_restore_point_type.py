from enum import Enum


class CosmosDbRestorePointType(str, Enum):
    BACKUP = "Backup"
    CONTINUOUS = "Continuous"

    def __str__(self) -> str:
        return str(self.value)
