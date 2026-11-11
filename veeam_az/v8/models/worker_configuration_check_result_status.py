from enum import Enum


class WorkerConfigurationCheckResultStatus(str, Enum):
    NETWORKDOESNOTEXIST = "NetworkDoesNotExist"
    VALID = "Valid"
    VALIDATIONERROR = "ValidationError"
    WORKERSUBSCRIPTIONCHANGED = "WorkerSubscriptionChanged"

    def __str__(self) -> str:
        return str(self.value)
