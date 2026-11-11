from enum import Enum


class TenantSort(str, Enum):
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    TENANTIDASC = "TenantIdAsc"
    TENANTIDDESC = "TenantIdDesc"

    def __str__(self) -> str:
        return str(self.value)
