from enum import Enum


class VnetPolicySessionsReportSort(str, Enum):
    JOBSTATUSASC = "JobStatusAsc"
    JOBSTATUSDESC = "JobStatusDesc"
    TIMEASC = "TimeAsc"
    TIMEDESC = "TimeDesc"

    def __str__(self) -> str:
        return str(self.value)
