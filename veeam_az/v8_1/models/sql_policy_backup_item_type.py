from enum import Enum


class SqlPolicyBackupItemType(str, Enum):
    DATABASE = "Database"
    SQLSERVER = "SqlServer"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
