from enum import Enum


class AzureEnvironmentNullable(str, Enum):
    CHINA = "China"
    GERMANY = "Germany"
    GLOBAL = "Global"
    UNKNOWN = "Unknown"
    USGOVERNMENT = "USGovernment"

    def __str__(self) -> str:
        return str(self.value)
