from enum import Enum


class UserSort(str, Enum):
    ACCOUNTTYPEASC = "AccountTypeAsc"
    ACCOUNTTYPEDESC = "AccountTypeDesc"
    DESCRIPTIONASC = "DescriptionAsc"
    DESCRIPTIONDESC = "DescriptionDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    IDENTITYPROVIDERIDASC = "IdentityProviderIdAsc"
    IDENTITYPROVIDERIDDESC = "IdentityProviderIdDesc"
    ISDEFAULTASC = "IsDefaultAsc"
    ISDEFAULTDESC = "IsDefaultDesc"
    MFAENABLEDASC = "MfaEnabledAsc"
    MFAENABLEDDESC = "MfaEnabledDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    ROLEASC = "RoleAsc"
    ROLEDESC = "RoleDesc"

    def __str__(self) -> str:
        return str(self.value)
