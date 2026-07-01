from enum import Enum


class DatabaseStatus(str, Enum):
    AUTOCLOSED = "AutoClosed"
    COPYING = "Copying"
    CREATING = "Creating"
    DISABLED = "Disabled"
    EMERGENCYMODE = "EmergencyMode"
    INACCESSIBLE = "Inaccessible"
    OFFLINE = "Offline"
    OFFLINECHANGINGDWPERFORMANCETIERS = "OfflineChangingDwPerformanceTiers"
    OFFLINESECONDARY = "OfflineSecondary"
    ONLINE = "Online"
    ONLINECHANGINGDWPERFORMANCETIERS = "OnlineChangingDwPerformanceTiers"
    OTHER = "Other"
    PAUSED = "Paused"
    PAUSING = "Pausing"
    RECOVERING = "Recovering"
    RECOVERYPENDING = "RecoveryPending"
    RESTORING = "Restoring"
    RESUMING = "Resuming"
    SCALING = "Scaling"
    SHUTDOWN = "Shutdown"
    STANDBY = "Standby"
    SUSPECT = "Suspect"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
