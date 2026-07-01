from enum import Enum


class ScheduleType(str, Enum):
    ARCHIVE = "Archive"
    BACKUP = "Backup"
    SNAPSHOT = "Snapshot"

    def __str__(self) -> str:
        return str(self.value)
