from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationBackupServerParameters")


@_attrs_define
class ConfigurationBackupServerParameters:
    """
    Attributes:
        repository_name (None | str | Unset):
        retention_restore_points_numbers (int | None | Unset):
    """

    repository_name: None | str | Unset = UNSET
    retention_restore_points_numbers: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_name: None | str | Unset
        if isinstance(self.repository_name, Unset):
            repository_name = UNSET
        else:
            repository_name = self.repository_name

        retention_restore_points_numbers: int | None | Unset
        if isinstance(self.retention_restore_points_numbers, Unset):
            retention_restore_points_numbers = UNSET
        else:
            retention_restore_points_numbers = self.retention_restore_points_numbers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if retention_restore_points_numbers is not UNSET:
            field_dict["retentionRestorePointsNumbers"] = retention_restore_points_numbers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_repository_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_name = _parse_repository_name(d.pop("repositoryName", UNSET))

        def _parse_retention_restore_points_numbers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_restore_points_numbers = _parse_retention_restore_points_numbers(
            d.pop("retentionRestorePointsNumbers", UNSET)
        )

        configuration_backup_server_parameters = cls(
            repository_name=repository_name,
            retention_restore_points_numbers=retention_restore_points_numbers,
        )

        configuration_backup_server_parameters.additional_properties = d
        return configuration_backup_server_parameters

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
