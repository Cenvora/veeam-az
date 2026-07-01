from enum import Enum


class AzureAccountCheckResultStatus(str, Enum):
    CERTIFICATEMISMATCH = "CertificateMismatch"
    DOESNOTEXIST = "DoesNotExist"
    EXPIREDCERTIFICATE = "ExpiredCertificate"
    EXPIREDCLIENTSECRET = "ExpiredClientSecret"
    INVALIDCLIENTSECRET = "InvalidClientSecret"
    NOSUBSCRIPTIONS = "NoSubscriptions"
    SUBSCRIPTIONPERMISSIONSMISSING = "SubscriptionPermissionsMissing"
    UNKNOWN = "Unknown,"
    VALID = "Valid"
    VALIDATIONFAILURE = "ValidationFailure"
    WORKERSUBSCRIPTIONCHANGED = "WorkerSubscriptionChanged"

    def __str__(self) -> str:
        return str(self.value)
