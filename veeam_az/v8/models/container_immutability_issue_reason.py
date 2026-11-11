from enum import Enum


class ContainerImmutabilityIssueReason(str, Enum):
    CONTAINERPOLICYNOTSET = "ContainerPolicyNotSet"
    UNKNOWN = "Unknown"
    UNSUPPORTEDBYAZURE = "UnsupportedByAzure"
    VERSIONINGFORBLOBSDISABLED = "VersioningForBlobsDisabled"

    def __str__(self) -> str:
        return str(self.value)
