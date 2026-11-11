from enum import Enum


class PolicyCosmosDbBackupWorkload(str, Enum):
    MONGODB = "MongoDB"
    POSTGRESQL = "PostgreSQL"

    def __str__(self) -> str:
        return str(self.value)
