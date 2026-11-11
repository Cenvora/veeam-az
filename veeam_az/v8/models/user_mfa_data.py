from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserMfaData")


@_attrs_define
class UserMfaData:
    """
    Attributes:
        user_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the user
            for whom MFA will be enabled.
        qr_string (None | str | Unset): String that can be used to generate a QR code.
        secret_key (None | str | Unset): Secret key used to associate the authorization server with an authenticator
            application.
        scratch_codes (list[str] | None | Unset): Recovery scratch codes that can be used to get authorization instead
            of a verification code. Each recovery code can be used only once.
        token (None | str | Unset): Token used to associate the authenticator application with the authorization server.
    """

    user_id: None | str | Unset = UNSET
    qr_string: None | str | Unset = UNSET
    secret_key: None | str | Unset = UNSET
    scratch_codes: list[str] | None | Unset = UNSET
    token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        qr_string: None | str | Unset
        if isinstance(self.qr_string, Unset):
            qr_string = UNSET
        else:
            qr_string = self.qr_string

        secret_key: None | str | Unset
        if isinstance(self.secret_key, Unset):
            secret_key = UNSET
        else:
            secret_key = self.secret_key

        scratch_codes: list[str] | None | Unset
        if isinstance(self.scratch_codes, Unset):
            scratch_codes = UNSET
        elif isinstance(self.scratch_codes, list):
            scratch_codes = self.scratch_codes

        else:
            scratch_codes = self.scratch_codes

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if qr_string is not UNSET:
            field_dict["qrString"] = qr_string
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if scratch_codes is not UNSET:
            field_dict["scratchCodes"] = scratch_codes
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_qr_string(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qr_string = _parse_qr_string(d.pop("qrString", UNSET))

        def _parse_secret_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_key = _parse_secret_key(d.pop("secretKey", UNSET))

        def _parse_scratch_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scratch_codes_type_0 = cast(list[str], data)

                return scratch_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scratch_codes = _parse_scratch_codes(d.pop("scratchCodes", UNSET))

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

        user_mfa_data = cls(
            user_id=user_id,
            qr_string=qr_string,
            secret_key=secret_key,
            scratch_codes=scratch_codes,
            token=token,
        )

        return user_mfa_data
