from enum import Enum


class ConfigurationRestoreStatus(str, Enum):
    CONFIGURATIONCHECK = "ConfigurationCheck"
    MAINTENANCEMODE = "MaintenanceMode"
    NEVEREXECUTED = "NeverExecuted"
    RESTORE = "Restore"

    def __str__(self) -> str:
        return str(self.value)
