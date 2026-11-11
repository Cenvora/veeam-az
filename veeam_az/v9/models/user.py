from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.rbac_role import RbacRole
from ..models.user_type import UserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        role (RbacRole): Role assigned to the user. Defines user permissions in Veeam Backup for Microsoft Azure.
        type_ (UserType | Unset): Type of the user.
        identity_provider_entity_id (None | str | Unset): Microsoft Azure ID assigned to the identity provider entity of
            the user.
        id (None | str | Unset): System ID assigned to a user in the Veeam Backup for Microsoft Azure REST API.
        name (None | str | Unset): User name.
        description (None | str | Unset): Description of the user.
        mfa_enabled (bool | Unset): Defines whether MFA is enabled for the user.
        is_default (bool | Unset): Defines whether the user is the Default Admin.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    role: RbacRole
    type_: UserType | Unset = UNSET
    identity_provider_entity_id: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    mfa_enabled: bool | Unset = UNSET
    is_default: bool | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        role = self.role.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        identity_provider_entity_id: None | str | Unset
        if isinstance(self.identity_provider_entity_id, Unset):
            identity_provider_entity_id = UNSET
        else:
            identity_provider_entity_id = self.identity_provider_entity_id

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

        is_default = self.is_default

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if identity_provider_entity_id is not UNSET:
            field_dict["identityProviderEntityId"] = identity_provider_entity_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if mfa_enabled is not UNSET:
            field_dict["mfaEnabled"] = mfa_enabled
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)
        role = RbacRole(d.pop("role"))

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

        is_default = d.pop("isDefault", UNSET)

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        user = cls(
            role=role,
            type_=type_,
            identity_provider_entity_id=identity_provider_entity_id,
            id=id,
            name=name,
            description=description,
            mfa_enabled=mfa_enabled,
            is_default=is_default,
            field_links=field_links,
        )

        return user
