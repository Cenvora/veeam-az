from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagementGroupSettings")


@_attrs_define
class ManagementGroupSettings:
    """
    Attributes:
        group_id_to_add (None | str | Unset):
        group_name_to_add (None | str | Unset):
        group_id_to_remove (None | str | Unset):
    """

    group_id_to_add: None | str | Unset = UNSET
    group_name_to_add: None | str | Unset = UNSET
    group_id_to_remove: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id_to_add: None | str | Unset
        if isinstance(self.group_id_to_add, Unset):
            group_id_to_add = UNSET
        else:
            group_id_to_add = self.group_id_to_add

        group_name_to_add: None | str | Unset
        if isinstance(self.group_name_to_add, Unset):
            group_name_to_add = UNSET
        else:
            group_name_to_add = self.group_name_to_add

        group_id_to_remove: None | str | Unset
        if isinstance(self.group_id_to_remove, Unset):
            group_id_to_remove = UNSET
        else:
            group_id_to_remove = self.group_id_to_remove

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id_to_add is not UNSET:
            field_dict["groupIdToAdd"] = group_id_to_add
        if group_name_to_add is not UNSET:
            field_dict["groupNameToAdd"] = group_name_to_add
        if group_id_to_remove is not UNSET:
            field_dict["groupIdToRemove"] = group_id_to_remove

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_group_id_to_add(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_id_to_add = _parse_group_id_to_add(d.pop("groupIdToAdd", UNSET))

        def _parse_group_name_to_add(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name_to_add = _parse_group_name_to_add(d.pop("groupNameToAdd", UNSET))

        def _parse_group_id_to_remove(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_id_to_remove = _parse_group_id_to_remove(d.pop("groupIdToRemove", UNSET))

        management_group_settings = cls(
            group_id_to_add=group_id_to_add,
            group_name_to_add=group_name_to_add,
            group_id_to_remove=group_id_to_remove,
        )

        return management_group_settings
