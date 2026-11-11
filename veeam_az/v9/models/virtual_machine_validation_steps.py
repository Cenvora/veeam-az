from enum import Enum


class VirtualMachineValidationSteps(str, Enum):
    ALL = "All"
    AVAILABILITYSET = "AvailabilitySet"
    AVAILABILITYZONE = "AvailabilityZone"
    DATARETRIEVAL = "DataRetrieval"
    DISKS = "Disks"
    DISKTYPE = "DiskType"
    NAME = "Name"
    NETWORK = "Network"
    NONE = "None"
    PERMISSIONS = "Permissions"
    REGION = "Region"
    RESOURCEGROUP = "ResourceGroup"
    SECURITYGROUP = "SecurityGroup"
    SNAPSHOT = "Snapshot"
    STORAGEACCOUNT = "StorageAccount"
    SUBNET = "Subnet"
    SUBSCRIPTION = "Subscription"
    UNKNOWN = "Unknown"
    VMSIZE = "VmSize"

    def __str__(self) -> str:
        return str(self.value)
