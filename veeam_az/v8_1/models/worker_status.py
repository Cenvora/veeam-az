from enum import Enum


class WorkerStatus(str, Enum):
    BUSY = "Busy"
    CREATING = "Creating"
    DEALLOCATED = "Deallocated"
    DEALLOCATING = "Deallocating"
    IDLE = "Idle"
    PENDINGREMOVAL = "PendingRemoval"
    RECOVERING = "Recovering"
    REMOVED = "Removed"
    STARTING = "Starting"
    STOPPED = "Stopped"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
