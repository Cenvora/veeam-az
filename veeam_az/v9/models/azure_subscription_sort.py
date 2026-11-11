from enum import Enum


class AzureSubscriptionSort(str, Enum):
    AZUREACCOUNTEXPIRINGASC = "AzureAccountExpiringAsc"
    AZUREACCOUNTEXPIRINGDESC = "AzureAccountExpiringDesc"
    AZUREACCOUNTNAMEASC = "AzureAccountNameAsc"
    AZUREACCOUNTNAMEDESC = "AzureAccountNameDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"

    def __str__(self) -> str:
        return str(self.value)
