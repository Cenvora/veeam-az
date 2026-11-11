from enum import Enum


class FlrSearchTaskState(str, Enum):
    NODATA = "NoData"
    PREPARING = "Preparing"
    READY = "Ready"

    def __str__(self) -> str:
        return str(self.value)
