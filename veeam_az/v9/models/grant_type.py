from enum import Enum


class GrantType(str, Enum):
    AUTHENTICATION_CODE = "Authentication_code"
    MFA = "Mfa"
    PASSWORD = "Password"
    REFRESH_TOKEN = "Refresh_token"
    SAML = "Saml"
    SSOTOKEN = "SsoToken"
    UNKNOWN = "Unknown"
    UPDATER_TOKEN = "Updater_token"

    def __str__(self) -> str:
        return str(self.value)
