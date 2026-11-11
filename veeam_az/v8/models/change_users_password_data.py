from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ChangeUsersPasswordData")


@_attrs_define
class ChangeUsersPasswordData:
    """
    Attributes:
        new_password (str): Specifies a new password for the user.
        admins_password (str): Specifies the password of the Default Admin.
    """

    new_password: str
    admins_password: str

    def to_dict(self) -> dict[str, Any]:
        new_password = self.new_password

        admins_password = self.admins_password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "newPassword": new_password,
                "adminsPassword": admins_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_password = d.pop("newPassword")

        admins_password = d.pop("adminsPassword")

        change_users_password_data = cls(
            new_password=new_password,
            admins_password=admins_password,
        )

        return change_users_password_data
