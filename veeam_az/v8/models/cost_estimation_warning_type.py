from enum import Enum


class CostEstimationWarningType(str, Enum):
    BACKUPTODIFFERENTREGION = "BackupToDifferentRegion"
    PRICEISAPPROXIMATE = "PriceIsApproximate"
    RETENTIONTOOSHORTFORCOOLSTORAGE = "RetentionTooShortForCoolStorage"
    SIMULATIONSHORTENED = "SimulationShortened"
    SNAPSHOTSRETENTIONAFFECTSCOSTS = "SnapshotsRetentionAffectsCosts"
    SNAPSHOTSRETENTIONAFFECTSTRAFFICCOSTS = "SnapshotsRetentionAffectsTrafficCosts"
    STAGINGSERVERINDIFFERENTREGIONTHANDATABASE = "StagingServerInDifferentRegionThanDatabase"
    STORAGECOULDBECHEAPER = "StorageCouldBeCheaper"
    UNKNOWN = "Unknown"
    VMHASNODISKS = "VmHasNoDisks"

    def __str__(self) -> str:
        return str(self.value)
