from enum import Enum


class SlaFilterSessionStatus(str, Enum):
    ALL = "All"
    FAILURE = "Failure"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
