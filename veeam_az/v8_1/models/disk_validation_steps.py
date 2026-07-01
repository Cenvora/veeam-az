from enum import Enum


class DiskValidationSteps(str, Enum):
    ALL = "All"
    AVAILABILITYZONE = "AvailabilityZone"
    DATARETRIEVAL = "DataRetrieval"
    DISKTYPE = "DiskType"
    NAME = "Name"
    NONE = "None"
    PERMISSIONS = "Permissions"
    REGION = "Region"
    RESOURCEGROUP = "ResourceGroup"
    SNAPSHOT = "Snapshot"
    STORAGEACCOUNT = "StorageAccount"
    SUBSCRIPTION = "Subscription"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
