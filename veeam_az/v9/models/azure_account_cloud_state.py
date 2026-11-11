from enum import Enum


class AzureAccountCloudState(str, Enum):
    CERTIFICATEMISMATCH = "CertificateMismatch"
    EXPIREDCERTIFICATE = "ExpiredCertificate"
    EXPIREDCLIENTSECRET = "ExpiredClientSecret"
    INVALID = "Invalid"
    INVALIDCLIENTSECRET = "InvalidClientSecret"
    NOSUBSCRIPTIONS = "NoSubscriptions"
    NOTFOUND = "NotFound"
    UNKNOWN = "Unknown"
    VALID = "Valid"

    def __str__(self) -> str:
        return str(self.value)
