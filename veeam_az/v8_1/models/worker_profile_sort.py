from enum import Enum


class WorkerProfileSort(str, Enum):
    MAXINSTANCESASC = "MaxInstancesAsc"
    MAXINSTANCESDESC = "MaxInstancesDesc"
    MININSTANCESASC = "MinInstancesAsc"
    MININSTANCESDESC = "MinInstancesDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"

    def __str__(self) -> str:
        return str(self.value)
