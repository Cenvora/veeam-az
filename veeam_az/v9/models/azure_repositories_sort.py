from enum import Enum


class AzureRepositoriesSort(str, Enum):
    ACCESSTIERASC = "AccessTierAsc"
    ACCESSTIERDESC = "AccessTierDesc"
    AZURESTORAGEACCOUNTNAMEASC = "AzureStorageAccountNameAsc"
    AZURESTORAGEACCOUNTNAMEDESC = "AzureStorageAccountNameDesc"
    AZURESTORAGEFOLDERASC = "AzureStorageFolderAsc"
    AZURESTORAGEFOLDERDESC = "AzureStorageFolderDesc"
    CONTAINERASC = "ContainerAsc"
    CONTAINERDESC = "ContainerDesc"
    DESCRIPTIONASC = "DescriptionAsc"
    DESCRIPTIONDESC = "DescriptionDesc"
    ENCRYPTIONASC = "EncryptionAsc"
    ENCRYPTIONDESC = "EncryptionDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    IMMUTABILITYASC = "ImmutabilityAsc"
    IMMUTABILITYDESC = "ImmutabilityDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    PERFORMANCEASC = "PerformanceAsc"
    PERFORMANCEDESC = "PerformanceDesc"
    REDUNDANCYASC = "RedundancyAsc"
    REDUNDANCYDESC = "RedundancyDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"
    SUBSCRIPTIONASC = "SubscriptionAsc"
    SUBSCRIPTIONDESC = "SubscriptionDesc"

    def __str__(self) -> str:
        return str(self.value)
