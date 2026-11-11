from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserExportQueryOptions")


@_attrs_define
class UserExportQueryOptions:
    """
    Attributes:
        name_filter (None | str | Unset): Returns only a user with the specified name.
        user_ids (list[UUID] | None | Unset): Specifies the system IDs assigned in the Veeam Backup for Microsoft Azure
            REST API to the user accounts whose data will be exported.
    """

    name_filter: None | str | Unset = UNSET
    user_ids: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name_filter: None | str | Unset
        if isinstance(self.name_filter, Unset):
            name_filter = UNSET
        else:
            name_filter = self.name_filter

        user_ids: list[str] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = []
            for user_ids_type_0_item_data in self.user_ids:
                user_ids_type_0_item = str(user_ids_type_0_item_data)
                user_ids.append(user_ids_type_0_item)

        else:
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name_filter is not UNSET:
            field_dict["nameFilter"] = name_filter
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name_filter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_filter = _parse_name_filter(d.pop("nameFilter", UNSET))

        def _parse_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = []
                _user_ids_type_0 = data
                for user_ids_type_0_item_data in _user_ids_type_0:
                    user_ids_type_0_item = UUID(user_ids_type_0_item_data)

                    user_ids_type_0.append(user_ids_type_0_item)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("userIds", UNSET))

        user_export_query_options = cls(
            name_filter=name_filter,
            user_ids=user_ids,
        )

        return user_export_query_options
