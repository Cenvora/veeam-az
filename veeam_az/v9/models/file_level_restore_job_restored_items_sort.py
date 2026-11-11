from enum import Enum


class FileLevelRestoreJobRestoredItemsSort(str, Enum):
    FILEPATHASC = "FilePathAsc"
    FILEPATHDESC = "FilePathDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    VIRTUALMACHINEASC = "VirtualMachineAsc"
    VIRTUALMACHINEDESC = "VirtualMachineDesc"

    def __str__(self) -> str:
        return str(self.value)
