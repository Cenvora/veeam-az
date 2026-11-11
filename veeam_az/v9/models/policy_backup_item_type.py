from enum import Enum


class PolicyBackupItemType(str, Enum):
    REGION = "Region"
    RESOURCEGROUP = "ResourceGroup"
    SUBSCRIPTION = "Subscription"
    TAG = "Tag"
    UNKNOWN = "Unknown"
    VIRTUALMACHINE = "VirtualMachine"

    def __str__(self) -> str:
        return str(self.value)
