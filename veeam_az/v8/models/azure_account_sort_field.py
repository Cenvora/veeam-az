from enum import Enum


class AzureAccountSortField(str, Enum):
    AZUREACCOUNTORIGINASC = "AzureAccountOriginAsc"
    AZUREACCOUNTORIGINDESC = "AzureAccountOriginDesc"
    AZUREACCOUNTSTATEASC = "AzureAccountStateAsc"
    AZUREACCOUNTSTATEDESC = "AzureAccountStateDesc"
    DESCRIPTIONASC = "DescriptionAsc"
    DESCRIPTIONDESC = "DescriptionDesc"
    ENTRAGROUPNAMEASC = "EntraGroupNameAsc"
    ENTRAGROUPNAMEDESC = "EntraGroupNameDesc"
    EXPIRATIONDATEASC = "ExpirationDateAsc"
    EXPIRATIONDATEDESC = "ExpirationDateDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    PERMISSIONLASTCHECKASC = "PermissionLastCheckAsc"
    PERMISSIONLASTCHECKDESC = "PermissionLastCheckDesc"
    PERMISSIONSTATUSASC = "PermissionStatusAsc"
    PERMISSIONSTATUSDESC = "PermissionStatusDesc"
    SUBSCRIPTIONSNUMBERSASC = "SubscriptionsNumbersAsc"
    SUBSCRIPTIONSNUMBERSDESC = "SubscriptionsNumbersDesc"

    def __str__(self) -> str:
        return str(self.value)
