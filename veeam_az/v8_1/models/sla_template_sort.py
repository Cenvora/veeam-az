from enum import Enum


class SlaTemplateSort(str, Enum):
    ARCHIVESTATEASC = "ArchiveStateAsc"
    ARCHIVESTATEDESC = "ArchiveStateDesc"
    BACKUPSSTATEASC = "BackupsStateAsc"
    BACKUPSSTATEDESC = "BackupsStateDesc"
    CURRENTLYASSIGNEDASC = "CurrentlyAssignedAsc"
    CURRENTLYASSIGNEDDESC = "CurrentlyAssignedDesc"
    DESCRIPTIONASC = "DescriptionAsc"
    DESCRIPTIONDESC = "DescriptionDesc"
    LASTMODIFIEDASC = "LastModifiedAsc"
    LASTMODIFIEDDESC = "LastModifiedDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    SNAPSHOTSSTATEASC = "SnapshotsStateAsc"
    SNAPSHOTSSTATEDESC = "SnapshotsStateDesc"

    def __str__(self) -> str:
        return str(self.value)
