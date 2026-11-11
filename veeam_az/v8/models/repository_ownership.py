from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryOwnership")


@_attrs_define
class RepositoryOwnership:
    """
    Attributes:
        has_another_owner (bool | Unset):
        current_owner_identifier (None | str | Unset):
        current_owner_name (None | str | Unset):
    """

    has_another_owner: bool | Unset = UNSET
    current_owner_identifier: None | str | Unset = UNSET
    current_owner_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        has_another_owner = self.has_another_owner

        current_owner_identifier: None | str | Unset
        if isinstance(self.current_owner_identifier, Unset):
            current_owner_identifier = UNSET
        else:
            current_owner_identifier = self.current_owner_identifier

        current_owner_name: None | str | Unset
        if isinstance(self.current_owner_name, Unset):
            current_owner_name = UNSET
        else:
            current_owner_name = self.current_owner_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if has_another_owner is not UNSET:
            field_dict["hasAnotherOwner"] = has_another_owner
        if current_owner_identifier is not UNSET:
            field_dict["currentOwnerIdentifier"] = current_owner_identifier
        if current_owner_name is not UNSET:
            field_dict["currentOwnerName"] = current_owner_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_another_owner = d.pop("hasAnotherOwner", UNSET)

        def _parse_current_owner_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_owner_identifier = _parse_current_owner_identifier(d.pop("currentOwnerIdentifier", UNSET))

        def _parse_current_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_owner_name = _parse_current_owner_name(d.pop("currentOwnerName", UNSET))

        repository_ownership = cls(
            has_another_owner=has_another_owner,
            current_owner_identifier=current_owner_identifier,
            current_owner_name=current_owner_name,
        )

        return repository_ownership
