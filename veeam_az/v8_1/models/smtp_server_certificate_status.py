from enum import Enum


class SmtpServerCertificateStatus(str, Enum):
    ERROR = "Error"
    INSECUREUNVERIFIED = "InsecureUnverified"
    INSECUREVERIFIED = "InsecureVerified"
    SECUREVERIFIED = "SecureVerified"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
