from enum import Enum


class KeyVaultKeyExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    VERSIONS = "Versions"

    def __str__(self) -> str:
        return str(self.value)
