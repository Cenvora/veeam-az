from enum import Enum


class SmtpAccountType(str, Enum):
    BASIC = "Basic"
    NONE = "None"
    OAUTH2 = "OAuth2"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
