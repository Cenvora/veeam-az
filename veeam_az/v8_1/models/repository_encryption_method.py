from enum import Enum


class RepositoryEncryptionMethod(str, Enum):
    KEYVAULT = "KeyVault"
    NONE = "None"
    PASSWORD = "Password"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
