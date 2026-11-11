from enum import Enum


class StorageAccountSort(str, Enum):
    ACCESSTIERASC = "AccessTierAsc"
    ACCESSTIERDESC = "AccessTierDesc"
    IMMUTABILITYENABLEDASC = "ImmutabilityEnabledAsc"
    IMMUTABILITYENABLEDDESC = "ImmutabilityEnabledDesc"
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
    SUBSCRIPTIONIDASC = "SubscriptionIdAsc"
    SUBSCRIPTIONIDDESC = "SubscriptionIdDesc"
    SUBSCRIPTIONNAMEASC = "SubscriptionNameAsc"
    SUBSCRIPTIONNAMEDESC = "SubscriptionNameDesc"
    TENANTIDASC = "TenantIdAsc"
    TENANTIDDESC = "TenantIdDesc"
    TENANTNAMEASC = "TenantNameAsc"
    TENANTNAMEDESC = "TenantNameDesc"

    def __str__(self) -> str:
        return str(self.value)
