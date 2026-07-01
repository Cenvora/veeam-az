from enum import Enum


class CertificateType(str, Enum):
    WEBSERVER = "WebServer"
    WORKER = "Worker"

    def __str__(self) -> str:
        return str(self.value)
