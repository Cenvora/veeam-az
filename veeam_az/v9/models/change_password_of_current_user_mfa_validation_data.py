from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangePasswordOfCurrentUserMfaValidationData")


@_attrs_define
class ChangePasswordOfCurrentUserMfaValidationData:
    """
    Attributes:
        new_password (None | str | Unset):
        mfa_token (None | str | Unset):
        mfa_code (None | str | Unset):
    """

    new_password: None | str | Unset = UNSET
    mfa_token: None | str | Unset = UNSET
    mfa_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_password: None | str | Unset
        if isinstance(self.new_password, Unset):
            new_password = UNSET
        else:
            new_password = self.new_password

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password
        if mfa_token is not UNSET:
            field_dict["mfaToken"] = mfa_token
        if mfa_code is not UNSET:
            field_dict["mfaCode"] = mfa_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_new_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_password = _parse_new_password(d.pop("newPassword", UNSET))

        def _parse_mfa_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mfa_token = _parse_mfa_token(d.pop("mfaToken", UNSET))

        def _parse_mfa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mfa_code = _parse_mfa_code(d.pop("mfaCode", UNSET))

        change_password_of_current_user_mfa_validation_data = cls(
            new_password=new_password,
            mfa_token=mfa_token,
            mfa_code=mfa_code,
        )

        return change_password_of_current_user_mfa_validation_data
