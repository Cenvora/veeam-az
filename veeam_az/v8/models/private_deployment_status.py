from enum import Enum


class PrivateDeploymentStatus(str, Enum):
    DISABLED = "Disabled"
    DISABLING = "Disabling"
    ENABLED = "Enabled"
    ENABLING = "Enabling"

    def __str__(self) -> str:
        return str(self.value)
