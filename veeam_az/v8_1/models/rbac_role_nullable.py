from enum import Enum


class RbacRoleNullable(str, Enum):
    INTEGRATIONOPERATOR = "IntegrationOperator"
    PORTALADMIN = "PortalAdmin"
    PORTALOPERATOR = "PortalOperator"
    READONLYUSER = "ReadOnlyUser"
    RESTOREOPERATOR = "RestoreOperator"
    UNKNOWN = "Unknown"
    VEEAMUPDATER = "VeeamUpdater"

    def __str__(self) -> str:
        return str(self.value)
