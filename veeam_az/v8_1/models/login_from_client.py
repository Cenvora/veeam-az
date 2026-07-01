from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.grant_type import GrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginFromClient")


@_attrs_define
class LoginFromClient:
    r"""
    Attributes:
        username (None | str | Unset): \[Required if the `grant_type` parameter value is *Password*\] User name.
        password (None | str | Unset): \[Required if the `grant_type` parameter value is *Password*\] Password of the
            user.
        refresh_token (None | str | Unset): \[Required if the `grant_type` parameter value is *Refresh_token*\] Refresh
            token.
        grant_type (GrantType | Unset): Grant type that will be used to authenticate a user.
        mfa_token (None | str | Unset): \[Required if the `grant_type` parameter value is *Mfa*\] MFA token.
        mfa_code (None | str | Unset): \[Required if the `grant_type` parameter value is *Mfa*\] Verification code.
        updater_token (None | str | Unset): \[Required if the `grant_type` parameter value is *Updater_token*\] Updater
            token.
        saml_response (None | str | Unset): \[Required if the `grant_type` parameter value is *Saml*\] Saml response
            obtained from the identity provider.
        sso_token (None | str | Unset): \[Required if the `grant_type` parameter value is *SsoToken*\] Single sign-on
            token.
        authorization_code (None | str | Unset): \[Required if the `grant_type` parameter value is
            *Authorization_code*\] Short lived authorization code.
        short_lived_refresh_token (bool | None | Unset): Defines whether to decrease the refresh token lifetime to 60
            minutes.
    """

    username: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    refresh_token: None | str | Unset = UNSET
    grant_type: GrantType | Unset = UNSET
    mfa_token: None | str | Unset = UNSET
    mfa_code: None | str | Unset = UNSET
    updater_token: None | str | Unset = UNSET
    saml_response: None | str | Unset = UNSET
    sso_token: None | str | Unset = UNSET
    authorization_code: None | str | Unset = UNSET
    short_lived_refresh_token: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        refresh_token: None | str | Unset
        if isinstance(self.refresh_token, Unset):
            refresh_token = UNSET
        else:
            refresh_token = self.refresh_token

        grant_type: str | Unset = UNSET
        if not isinstance(self.grant_type, Unset):
            grant_type = self.grant_type.value

        mfa_token: None | str | Unset
        if isinstance(self.mfa_token, Unset):
            mfa_token = UNSET
        else:
            mfa_token = self.mfa_token

        mfa_code: None | str | Unset
        if isinstance(self.mfa_code, Unset):
            mfa_code = UNSET
        else:
            mfa_code = self.mfa_code

        updater_token: None | str | Unset
        if isinstance(self.updater_token, Unset):
            updater_token = UNSET
        else:
            updater_token = self.updater_token

        saml_response: None | str | Unset
        if isinstance(self.saml_response, Unset):
            saml_response = UNSET
        else:
            saml_response = self.saml_response

        sso_token: None | str | Unset
        if isinstance(self.sso_token, Unset):
            sso_token = UNSET
        else:
            sso_token = self.sso_token

        authorization_code: None | str | Unset
        if isinstance(self.authorization_code, Unset):
            authorization_code = UNSET
        else:
            authorization_code = self.authorization_code

        short_lived_refresh_token: bool | None | Unset
        if isinstance(self.short_lived_refresh_token, Unset):
            short_lived_refresh_token = UNSET
        else:
            short_lived_refresh_token = self.short_lived_refresh_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if mfa_token is not UNSET:
            field_dict["mfa_token"] = mfa_token
        if mfa_code is not UNSET:
            field_dict["mfa_code"] = mfa_code
        if updater_token is not UNSET:
            field_dict["updater_token"] = updater_token
        if saml_response is not UNSET:
            field_dict["saml_response"] = saml_response
        if sso_token is not UNSET:
            field_dict["sso_token"] = sso_token
        if authorization_code is not UNSET:
            field_dict["authorization_code"] = authorization_code
        if short_lived_refresh_token is not UNSET:
            field_dict["short_lived_refresh_token"] = short_lived_refresh_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_refresh_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refresh_token = _parse_refresh_token(d.pop("refresh_token", UNSET))

        _grant_type = d.pop("grant_type", UNSET)
        grant_type: GrantType | Unset
        if isinstance(_grant_type, Unset):
            grant_type = UNSET
        else:
            grant_type = GrantType(_grant_type)

        def _parse_mfa_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mfa_token = _parse_mfa_token(d.pop("mfa_token", UNSET))

        def _parse_mfa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mfa_code = _parse_mfa_code(d.pop("mfa_code", UNSET))

        def _parse_updater_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updater_token = _parse_updater_token(d.pop("updater_token", UNSET))

        def _parse_saml_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saml_response = _parse_saml_response(d.pop("saml_response", UNSET))

        def _parse_sso_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sso_token = _parse_sso_token(d.pop("sso_token", UNSET))

        def _parse_authorization_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorization_code = _parse_authorization_code(d.pop("authorization_code", UNSET))

        def _parse_short_lived_refresh_token(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        short_lived_refresh_token = _parse_short_lived_refresh_token(d.pop("short_lived_refresh_token", UNSET))

        login_from_client = cls(
            username=username,
            password=password,
            refresh_token=refresh_token,
            grant_type=grant_type,
            mfa_token=mfa_token,
            mfa_code=mfa_code,
            updater_token=updater_token,
            saml_response=saml_response,
            sso_token=sso_token,
            authorization_code=authorization_code,
            short_lived_refresh_token=short_lived_refresh_token,
        )

        return login_from_client
