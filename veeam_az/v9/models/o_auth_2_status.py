from enum import Enum


class OAuth2Status(str, Enum):
    FAILURE = "Failure"
    PENDING = "Pending"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
