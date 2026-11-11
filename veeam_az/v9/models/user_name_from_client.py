from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.user_type_nullable import UserTypeNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserNameFromClient")


@_attrs_define
class UserNameFromClient:
    """
    Attributes:
        user_type (UserTypeNullable): Specifies the type of the new user.
        name (str):
        identity_provider_entity_id (None | str | Unset):
    """

    user_type: UserTypeNullable
    name: str
    identity_provider_entity_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_type = self.user_type.value

        name = self.name

        identity_provider_entity_id: None | str | Unset
        if isinstance(self.identity_provider_entity_id, Unset):
            identity_provider_entity_id = UNSET
        else:
            identity_provider_entity_id = self.identity_provider_entity_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "userType": user_type,
                "name": name,
            }
        )
        if identity_provider_entity_id is not UNSET:
            field_dict["identityProviderEntityId"] = identity_provider_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_type = UserTypeNullable(d.pop("userType"))

        name = d.pop("name")

        def _parse_identity_provider_entity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_provider_entity_id = _parse_identity_provider_entity_id(d.pop("identityProviderEntityId", UNSET))

        user_name_from_client = cls(
            user_type=user_type,
            name=name,
            identity_provider_entity_id=identity_provider_entity_id,
        )

        return user_name_from_client
