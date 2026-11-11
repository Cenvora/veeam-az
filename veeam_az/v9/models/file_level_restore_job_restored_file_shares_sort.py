from enum import Enum


class FileLevelRestoreJobRestoredFileSharesSort(str, Enum):
    FILEPATHASC = "FilePathAsc"
    FILEPATHDESC = "FilePathDesc"
    IDASC = "IdAsc"
    IDDESC = "IdDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"

    def __str__(self) -> str:
        return str(self.value)
