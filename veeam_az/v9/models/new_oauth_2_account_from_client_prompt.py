from enum import Enum


class NewOauth2AccountFromClientPrompt(str, Enum):
    CONSENT = "consent"
    LOGIN = "login"
    NONE = "none"
    SELECT_ACCOUNT = "select_account"

    def __str__(self) -> str:
        return str(self.value)
