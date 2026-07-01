from enum import Enum


class PolicyInstancesReportSort(str, Enum):
    INSTANCENAMEASC = "InstanceNameAsc"
    INSTANCENAMEDESC = "InstanceNameDesc"
    JOBSTATUSASC = "JobStatusAsc"
    JOBSTATUSDESC = "JobStatusDesc"

    def __str__(self) -> str:
        return str(self.value)
