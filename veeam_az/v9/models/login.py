from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.user_type import UserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Login")


@_attrs_define
class Login:
    """
    Attributes:
        access_token (None | str | Unset): String that represents authorization issued to the user and that must be used
            in all requests during the current logon session.
        token_type (None | str | Unset): Type of the user authorization.
        refresh_token (None | str | Unset): String that represents authorization granted to the user and that can be
            used to obtain a new access token if the current access token expires or becomes lost.
        expires_in (int | Unset): Access token lifetime.
        issued (datetime.datetime | None | Unset): Date and time when the tokens were issued.
        expires (datetime.datetime | None | Unset): Date and time when the access token expires.
        user_id (UUID | Unset): System ID assigned to the authorized user in the Veeam Backup for Microsoft Azure REST
            API.
        username (None | str | Unset): Name of the authorized user.
        role_name (None | str | Unset): Role assigned to the user. Defines user permissions in Veeam Backup for
            Microsoft Azure.
        user_type (UserType | Unset): Type of the user.
        latest_news_shown (bool | Unset): Defines whether "What's New" was shown for the user after update.
        mfa_enabled (bool | Unset): Defines whether MFA is enabled for the user.
        mfa_token (None | str | Unset): MFA token used to authorize an access of the user with enabled MFA.
        redirect_to (None | str | Unset): SSO redirection URL.
        short_lived (bool | Unset): Defines whether the refresh token lifetime is decreased to 60 minutes.
    """

    access_token: None | str | Unset = UNSET
    token_type: None | str | Unset = UNSET
    refresh_token: None | str | Unset = UNSET
    expires_in: int | Unset = UNSET
    issued: datetime.datetime | None | Unset = UNSET
    expires: datetime.datetime | None | Unset = UNSET
    user_id: UUID | Unset = UNSET
    username: None | str | Unset = UNSET
    role_name: None | str | Unset = UNSET
    user_type: UserType | Unset = UNSET
    latest_news_shown: bool | Unset = UNSET
    mfa_enabled: bool | Unset = UNSET
    mfa_token: None | str | Unset = UNSET
    redirect_to: None | str | Unset = UNSET
    short_lived: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access_token: None | str | Unset
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        token_type: None | str | Unset
        if isinstance(self.token_type, Unset):
            token_type = UNSET
        else:
            token_type = self.token_type

        refresh_token: None | str | Unset
        if isinstance(self.refresh_token, Unset):
            refresh_token = UNSET
        else:
            refresh_token = self.refresh_token

        expires_in = self.expires_in

        issued: None | str | Unset
        if isinstance(self.issued, Unset):
            issued = UNSET
        elif isinstance(self.issued, datetime.datetime):
            issued = self.issued.isoformat()
        else:
            issued = self.issued

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        role_name: None | str | Unset
        if isinstance(self.role_name, Unset):
            role_name = UNSET
        else:
            role_name = self.role_name

        user_type: str | Unset = UNSET
        if not isinstance(self.user_type, Unset):
            user_type = self.user_type.value

        latest_news_shown = self.latest_news_shown

        mfa_enabled = self.mfa_enabled

        mfa_token: None | str | Unset
        if isinstance(self.mfa_token, Unset):
            mfa_token = UNSET
        else:
            mfa_token = self.mfa_token

        redirect_to: None | str | Unset
        if isinstance(self.redirect_to, Unset):
            redirect_to = UNSET
        else:
            redirect_to = self.redirect_to

        short_lived = self.short_lived

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if issued is not UNSET:
            field_dict[".issued"] = issued
        if expires is not UNSET:
            field_dict[".expires"] = expires
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if role_name is not UNSET:
            field_dict["roleName"] = role_name
        if user_type is not UNSET:
            field_dict["userType"] = user_type
        if latest_news_shown is not UNSET:
            field_dict["latestNewsShown"] = latest_news_shown
        if mfa_enabled is not UNSET:
            field_dict["mfa_enabled"] = mfa_enabled
        if mfa_token is not UNSET:
            field_dict["mfa_token"] = mfa_token
        if redirect_to is not UNSET:
            field_dict["redirectTo"] = redirect_to
        if short_lived is not UNSET:
            field_dict["shortLived"] = short_lived

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_access_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_token = _parse_access_token(d.pop("access_token", UNSET))

        def _parse_token_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token_type = _parse_token_type(d.pop("token_type", UNSET))

        def _parse_refresh_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refresh_token = _parse_refresh_token(d.pop("refresh_token", UNSET))

        expires_in = d.pop("expires_in", UNSET)

        def _parse_issued(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issued_type_0 = isoparse(data)

                return issued_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        issued = _parse_issued(d.pop(".issued", UNSET))

        def _parse_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_0 = isoparse(data)

                return expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires = _parse_expires(d.pop(".expires", UNSET))

        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_role_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_name = _parse_role_name(d.pop("roleName", UNSET))

        _user_type = d.pop("userType", UNSET)
        user_type: UserType | Unset
        if isinstance(_user_type, Unset):
            user_type = UNSET
        else:
            user_type = UserType(_user_type)

        latest_news_shown = d.pop("latestNewsShown", UNSET)

        mfa_enabled = d.pop("mfa_enabled", UNSET)

        def _parse_mfa_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mfa_token = _parse_mfa_token(d.pop("mfa_token", UNSET))

        def _parse_redirect_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redirect_to = _parse_redirect_to(d.pop("redirectTo", UNSET))

        short_lived = d.pop("shortLived", UNSET)

        login = cls(
            access_token=access_token,
            token_type=token_type,
            refresh_token=refresh_token,
            expires_in=expires_in,
            issued=issued,
            expires=expires,
            user_id=user_id,
            username=username,
            role_name=role_name,
            user_type=user_type,
            latest_news_shown=latest_news_shown,
            mfa_enabled=mfa_enabled,
            mfa_token=mfa_token,
            redirect_to=redirect_to,
            short_lived=short_lived,
        )

        return login
