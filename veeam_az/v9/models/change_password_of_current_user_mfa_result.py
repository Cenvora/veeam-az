from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangePasswordOfCurrentUserMfaResult")


@_attrs_define
class ChangePasswordOfCurrentUserMfaResult:
    """
    Attributes:
        mfa_token (None | str | Unset):
    """

    mfa_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mfa_token: None | str | Unset
        if isinstance(self.mfa_token, Unset):
            mfa_token = UNSET
        else:
            mfa_token = self.mfa_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mfa_token is not UNSET:
            field_dict["mfaToken"] = mfa_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_mfa_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mfa_token = _parse_mfa_token(d.pop("mfaToken", UNSET))

        change_password_of_current_user_mfa_result = cls(
            mfa_token=mfa_token,
        )

        return change_password_of_current_user_mfa_result
