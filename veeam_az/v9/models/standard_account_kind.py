from enum import Enum


class StandardAccountKind(str, Enum):
    DATABASE = "Database"
    SMTP = "Smtp"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
