from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangePasswordOfCurrentUserMfaData")


@_attrs_define
class ChangePasswordOfCurrentUserMfaData:
    """
    Attributes:
        current_password (None | str | Unset):
    """

    current_password: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        current_password: None | str | Unset
        if isinstance(self.current_password, Unset):
            current_password = UNSET
        else:
            current_password = self.current_password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if current_password is not UNSET:
            field_dict["currentPassword"] = current_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_current_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_password = _parse_current_password(d.pop("currentPassword", UNSET))

        change_password_of_current_user_mfa_data = cls(
            current_password=current_password,
        )

        return change_password_of_current_user_mfa_data
