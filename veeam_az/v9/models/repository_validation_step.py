from enum import Enum


class RepositoryValidationStep(str, Enum):
    ALL = "All"
    ARCHIVESETTINGS = "ArchiveSettings"
    IMMUTABILITYSETTINGS = "ImmutabilitySettings"
    NONE = "None"
    REPOSITORYOWNERSHIP = "RepositoryOwnership"
    REPOSITORYSETTINGS = "RepositorySettings"
    SECURITYSETTINGS = "SecuritySettings"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
