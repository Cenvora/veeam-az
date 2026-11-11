from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangePasswordOfCurrentUserData")


@_attrs_define
class ChangePasswordOfCurrentUserData:
    """
    Attributes:
        current_password (None | str | Unset): Specifies the current password of the currently authorized user.
        new_password (None | str | Unset): Specifies a new password for the currently authorized user.
    """

    current_password: None | str | Unset = UNSET
    new_password: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        current_password: None | str | Unset
        if isinstance(self.current_password, Unset):
            current_password = UNSET
        else:
            current_password = self.current_password

        new_password: None | str | Unset
        if isinstance(self.new_password, Unset):
            new_password = UNSET
        else:
            new_password = self.new_password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if current_password is not UNSET:
            field_dict["currentPassword"] = current_password
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password

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

        def _parse_new_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_password = _parse_new_password(d.pop("newPassword", UNSET))

        change_password_of_current_user_data = cls(
            current_password=current_password,
            new_password=new_password,
        )

        return change_password_of_current_user_data
