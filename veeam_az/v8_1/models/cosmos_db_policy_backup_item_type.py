from enum import Enum


class CosmosDbPolicyBackupItemType(str, Enum):
    ACCOUNT = "Account"
    RESOURCEGROUP = "ResourceGroup"
    SUBSCRIPTION = "Subscription"
    TAG = "Tag"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
