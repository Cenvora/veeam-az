from enum import Enum


class ProtectedDatabaseSort(str, Enum):
    DATARETRIEVALSTATUSASC = "DataRetrievalStatusAsc"
    DATARETRIEVALSTATUSDESC = "DataRetrievalStatusDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    LASTBACKUPASC = "LastBackupAsc"
    LASTBACKUPDESC = "LastBackupDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    REPOSITORYNAMEASC = "RepositoryNameAsc"
    REPOSITORYNAMEDESC = "RepositoryNameDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    SERVERNAMEASC = "ServerNameAsc"
    SERVERNAMEDESC = "ServerNameDesc"
    SIZEASC = "SizeAsc"
    SIZEDESC = "SizeDesc"

    def __str__(self) -> str:
        return str(self.value)
