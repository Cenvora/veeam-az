from enum import Enum


class ConfigurationRestorePointSort(str, Enum):
    CREATIONTIMEASC = "CreationTimeAsc"
    CREATIONTIMEDESC = "CreationTimeDesc"
    FILENAMEASC = "FileNameAsc"
    FILENAMEDESC = "FileNameDesc"
    INSTANCEIDASC = "InstanceIdAsc"
    INSTANCEIDDESC = "InstanceIdDesc"
    PRODUCTVERSIONASC = "ProductVersionAsc"
    PRODUCTVERSIONDESC = "ProductVersionDesc"
    REPOSITORYNAMEASC = "RepositoryNameAsc"
    REPOSITORYNAMEDESC = "RepositoryNameDesc"
    SIZEASC = "SizeAsc"
    SIZEDESC = "SizeDesc"
    TYPEASC = "TypeAsc"
    TYPEDESC = "TypeDesc"

    def __str__(self) -> str:
        return str(self.value)
