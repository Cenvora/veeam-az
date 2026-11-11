from enum import Enum


class CredentialsStateFilterOptions(str, Enum):
    ALL = "All"
    ONLYWITHCREDENTIALS = "OnlyWithCredentials"
    ONLYWITHOUTCREDENTIALS = "OnlyWithoutCredentials"

    def __str__(self) -> str:
        return str(self.value)
