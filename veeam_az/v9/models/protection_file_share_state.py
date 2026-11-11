from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_share_backup_destination import FileShareBackupDestination
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionFileShareState")


@_attrs_define
class ProtectionFileShareState:
    """
    Attributes:
        restore_point_count (int):
        destinations (list[FileShareBackupDestination] | None | Unset):
    """

    restore_point_count: int
    destinations: list[FileShareBackupDestination] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_point_count = self.restore_point_count

        destinations: list[str] | None | Unset
        if isinstance(self.destinations, Unset):
            destinations = UNSET
        elif isinstance(self.destinations, list):
            destinations = []
            for destinations_type_0_item_data in self.destinations:
                destinations_type_0_item = destinations_type_0_item_data.value
                destinations.append(destinations_type_0_item)

        else:
            destinations = self.destinations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restorePointCount": restore_point_count,
            }
        )
        if destinations is not UNSET:
            field_dict["destinations"] = destinations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restore_point_count = d.pop("restorePointCount")

        def _parse_destinations(data: object) -> list[FileShareBackupDestination] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                destinations_type_0 = []
                _destinations_type_0 = data
                for destinations_type_0_item_data in _destinations_type_0:
                    destinations_type_0_item = FileShareBackupDestination(destinations_type_0_item_data)

                    destinations_type_0.append(destinations_type_0_item)

                return destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileShareBackupDestination] | None | Unset, data)

        destinations = _parse_destinations(d.pop("destinations", UNSET))

        protection_file_share_state = cls(
            restore_point_count=restore_point_count,
            destinations=destinations,
        )

        protection_file_share_state.additional_properties = d
        return protection_file_share_state

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
