from enum import Enum


class AzureAccountExpansion(str, Enum):
    ALL = "All"
    ASSIGNEDUSERS = "AssignedUsers"
    CLOUDSTATE = "CloudState"
    NONE = "None"
    TENANTS = "Tenants"

    def __str__(self) -> str:
        return str(self.value)
