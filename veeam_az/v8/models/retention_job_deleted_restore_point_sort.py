from enum import Enum


class RetentionJobDeletedRestorePointSort(str, Enum):
    BACKUPSIZEASC = "BackupSizeAsc"
    BACKUPSIZEDESC = "BackupSizeDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    REPOSITORYASC = "RepositoryAsc"
    REPOSITORYDESC = "RepositoryDesc"
    RESOURCEGROUPASC = "ResourceGroupAsc"
    RESOURCEGROUPDESC = "ResourceGroupDesc"
    RESOURCENAMEASC = "ResourceNameAsc"
    RESOURCENAMEDESC = "ResourceNameDesc"
    SNAPSHOTTIMEASC = "SnapshotTimeAsc"
    SNAPSHOTTIMEDESC = "SnapshotTimeDesc"

    def __str__(self) -> str:
        return str(self.value)
