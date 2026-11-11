from enum import Enum


class BottleneckType(str, Enum):
    CPU = "cpu"
    CPUCORELIMIT = "cpuCoreLimit"
    NOISSUES = "noIssues"
    RAM = "ram"

    def __str__(self) -> str:
        return str(self.value)
