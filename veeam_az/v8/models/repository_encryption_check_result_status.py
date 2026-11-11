from enum import Enum


class RepositoryEncryptionCheckResultStatus(str, Enum):
    ENCRYPTIONWASDISABLED = "EncryptionWasDisabled"
    INCORRECTPASSWORD = "IncorrectPassword"
    INVALIDENCRYPTIONSETTINGS = "InvalidEncryptionSettings"
    KEYVAULTKEYMISSING = "KeyVaultKeyMissing"
    KEYVAULTKEYTHUMBPRINTMISMATCH = "KeyVaultKeyThumbprintMismatch"
    KEYVAULTMISSING = "KeyVaultMissing"
    MISSINGPASSWORD = "MissingPassword"
    UNKNOWN = "Unknown"
    VALID = "Valid"
    VALIDATIONFAILURE = "ValidationFailure"

    def __str__(self) -> str:
        return str(self.value)
