from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.rbac_role_nullable import RbacRoleNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpdateFromClient")


@_attrs_define
class UserUpdateFromClient:
    """
    Attributes:
        role (RbacRoleNullable | Unset): Specifies the role to assign to the user.
        name (None | str | Unset): Specifies a new name for the user.
        description (None | str | Unset): Specifies a new description for the user.
        password (None | str | Unset): Specifies a new password for the user.
    """

    role: RbacRoleNullable | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    password: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _role = d.pop("role", UNSET)
        role: RbacRoleNullable | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RbacRoleNullable(_role)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        user_update_from_client = cls(
            role=role,
            name=name,
            description=description,
            password=password,
        )

        return user_update_from_client
