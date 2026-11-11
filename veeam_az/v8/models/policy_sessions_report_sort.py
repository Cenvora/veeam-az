from enum import Enum


class PolicySessionsReportSort(str, Enum):
    JOBSTATUSASC = "JobStatusAsc"
    JOBSTATUSDESC = "JobStatusDesc"
    SESSIONTYPEASC = "SessionTypeAsc"
    SESSIONTYPEDESC = "SessionTypeDesc"
    TIMEASC = "TimeAsc"
    TIMEDESC = "TimeDesc"

    def __str__(self) -> str:
        return str(self.value)
