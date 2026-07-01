from enum import Enum


class TenantWithAccountSort(str, Enum):
    ACCOUNTNAMEASC = "AccountNameAsc"
    ACCOUNTNAMEDESC = "AccountNameDesc"
    TENANTIDASC = "TenantIdAsc"
    TENANTIDDESC = "TenantIdDesc"
    TENANTNAMEASC = "TenantNameAsc"
    TENANTNAMEDESC = "TenantNameDesc"

    def __str__(self) -> str:
        return str(self.value)
