from enum import Enum


class CosmosDbAccountStatus(str, Enum):
    CREATING = "Creating"
    DELETED = "Deleted"
    DELETING = "Deleting"
    DROPPING = "Dropping"
    FAILED = "Failed"
    MIGRATING = "Migrating"
    NOCONTENT = "NoContent"
    OFFLINE = "Offline"
    ONLINE = "Online"
    RESTORING = "Restoring"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    UNKNOWN = "Unknown"
    UPDATING = "Updating"

    def __str__(self) -> str:
        return str(self.value)
