from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.rbac_role import RbacRole
from ..models.user_type import UserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentUser")


@_attrs_define
class CurrentUser:
    """
    Attributes:
        id (None | str | Unset):
        name (None | str | Unset):
        description (None | str | Unset):
        mfa_enabled (bool | Unset):
        role (RbacRole | Unset): Role assigned to the user. Defines user permissions in Veeam Backup for Microsoft
            Azure.
        type_ (UserType | Unset): Type of the user.
        identity_provider_entity_id (None | str | Unset):
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    mfa_enabled: bool | Unset = UNSET
    role: RbacRole | Unset = UNSET
    type_: UserType | Unset = UNSET
    identity_provider_entity_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

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

        mfa_enabled = self.mfa_enabled

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if mfa_enabled is not UNSET:
            field_dict["mfaEnabled"] = mfa_enabled
        if role is not UNSET:
            field_dict["role"] = role
        if type_ is not UNSET:
            field_dict["type"] = type_
        if identity_provider_entity_id is not UNSET:
            field_dict["identityProviderEntityId"] = identity_provider_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

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

        mfa_enabled = d.pop("mfaEnabled", UNSET)

        _role = d.pop("role", UNSET)
        role: RbacRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RbacRole(_role)

        _type_ = d.pop("type", UNSET)
        type_: UserType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UserType(_type_)

        def _parse_identity_provider_entity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_provider_entity_id = _parse_identity_provider_entity_id(d.pop("identityProviderEntityId", UNSET))

        current_user = cls(
            id=id,
            name=name,
            description=description,
            mfa_enabled=mfa_enabled,
            role=role,
            type_=type_,
            identity_provider_entity_id=identity_provider_entity_id,
        )

        return current_user
