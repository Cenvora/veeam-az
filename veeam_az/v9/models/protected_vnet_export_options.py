from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedVnetExportOptions")


@_attrs_define
class ProtectedVnetExportOptions:
    """
    Attributes:
        restore_point_ids (list[UUID] | None | Unset): Specifies system IDs assigned in the Veeam Backup for Microsoft
            Azure REST API to the virtual network configuration restore points whose data will be exported.
        search_pattern (None | str | Unset): Exports only data on those items of a resource collection that match the
            specified search pattern in the parameter value.
    """

    restore_point_ids: list[UUID] | None | Unset = UNSET
    search_pattern: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_point_ids: list[str] | None | Unset
        if isinstance(self.restore_point_ids, Unset):
            restore_point_ids = UNSET
        elif isinstance(self.restore_point_ids, list):
            restore_point_ids = []
            for restore_point_ids_type_0_item_data in self.restore_point_ids:
                restore_point_ids_type_0_item = str(restore_point_ids_type_0_item_data)
                restore_point_ids.append(restore_point_ids_type_0_item)

        else:
            restore_point_ids = self.restore_point_ids

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restore_point_ids is not UNSET:
            field_dict["restorePointIds"] = restore_point_ids
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_restore_point_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                restore_point_ids_type_0 = []
                _restore_point_ids_type_0 = data
                for restore_point_ids_type_0_item_data in _restore_point_ids_type_0:
                    restore_point_ids_type_0_item = UUID(restore_point_ids_type_0_item_data)

                    restore_point_ids_type_0.append(restore_point_ids_type_0_item)

                return restore_point_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        restore_point_ids = _parse_restore_point_ids(d.pop("restorePointIds", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        protected_vnet_export_options = cls(
            restore_point_ids=restore_point_ids,
            search_pattern=search_pattern,
        )

        protected_vnet_export_options.additional_properties = d
        return protected_vnet_export_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
