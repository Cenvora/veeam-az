from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.rbac_role_nullable import RbacRoleNullable
from ..models.user_type_nullable import UserTypeNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFromClient")


@_attrs_define
class UserFromClient:
    """
    Attributes:
        name (str): Specifies a name for the new user.
        description (str): Specifies a description for the new user.
        role (RbacRoleNullable | Unset): Specifies the role to assign to the user.
        type_ (UserTypeNullable | Unset): Specifies the type of the new user.
        identity_provider_entity_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to the identity
            provider entity of the new user.
        password (None | str | Unset): Specifies a password of the new user.
    """

    name: str
    description: str
    role: RbacRoleNullable | Unset = UNSET
    type_: UserTypeNullable | Unset = UNSET
    identity_provider_entity_id: None | str | Unset = UNSET
    password: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        identity_provider_entity_id: None | str | Unset
        if isinstance(self.identity_provider_entity_id, Unset):
            identity_provider_entity_id = UNSET
        else:
            identity_provider_entity_id = self.identity_provider_entity_id

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if type_ is not UNSET:
            field_dict["type"] = type_
        if identity_provider_entity_id is not UNSET:
            field_dict["identityProviderEntityId"] = identity_provider_entity_id
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        _role = d.pop("role", UNSET)
        role: RbacRoleNullable | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RbacRoleNullable(_role)

        _type_ = d.pop("type", UNSET)
        type_: UserTypeNullable | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UserTypeNullable(_type_)

        def _parse_identity_provider_entity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_provider_entity_id = _parse_identity_provider_entity_id(d.pop("identityProviderEntityId", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        user_from_client = cls(
            name=name,
            description=description,
            role=role,
            type_=type_,
            identity_provider_entity_id=identity_provider_entity_id,
            password=password,
        )

        return user_from_client
