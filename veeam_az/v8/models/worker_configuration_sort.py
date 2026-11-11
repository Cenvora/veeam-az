from enum import Enum


class WorkerConfigurationSort(str, Enum):
    MAXINSTANCESASC = "MaxInstancesAsc"
    MAXINSTANCESDESC = "MaxInstancesDesc"
    MININSTANCESASC = "MinInstancesAsc"
    MININSTANCESDESC = "MinInstancesDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"
    SUBNETASC = "SubnetAsc"
    SUBNETDESC = "SubnetDesc"

    def __str__(self) -> str:
        return str(self.value)
