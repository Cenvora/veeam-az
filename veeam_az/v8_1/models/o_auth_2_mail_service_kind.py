from enum import Enum


class OAuth2MailServiceKind(str, Enum):
    GOOGLE = "Google"
    MICROSOFT = "Microsoft"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
