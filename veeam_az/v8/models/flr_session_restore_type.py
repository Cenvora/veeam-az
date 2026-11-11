from enum import Enum


class FlrSessionRestoreType(str, Enum):
    KEEP = "Keep"
    OVERWRITE = "Overwrite"

    def __str__(self) -> str:
        return str(self.value)
