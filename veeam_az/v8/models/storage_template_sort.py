from enum import Enum


class StorageTemplateSort(str, Enum):
    ARCHIVEENABLEDASC = "ArchiveEnabledAsc"
    ARCHIVEENABLEDDESC = "ArchiveEnabledDesc"
    BACKUPSENABLEDASC = "BackupsEnabledAsc"
    BACKUPSENABLEDDESC = "BackupsEnabledDesc"
    CURRENTLYASSIGNEDASC = "CurrentlyAssignedAsc"
    CURRENTLYASSIGNEDDESC = "CurrentlyAssignedDesc"
    DESCRIPTIONASC = "DescriptionAsc"
    DESCRIPTIONDESC = "DescriptionDesc"
    LASTMODIFIEDASC = "LastModifiedAsc"
    LASTMODIFIEDDESC = "LastModifiedDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"

    def __str__(self) -> str:
        return str(self.value)
