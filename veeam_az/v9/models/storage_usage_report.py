from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageUsageReport")


@_attrs_define
class StorageUsageReport:
    """
    Attributes:
        snapshots_count (int | Unset): Total number of snapshots created for the protected resources.
        archives_count (int | Unset): Total amount of storage space currently consumed by archived backups (in bytes).
        backup_count (int | Unset): Total amount of storage space currently consumed by backups (in bytes).
        total_usage (int | Unset): Total amount of currently used storage space (in bytes).
        hot_usage (int | Unset): Total amount of currently used Hot tier storage space (in bytes).
        cool_usage (int | Unset): Total amount of currently used Cool tier storage space (in bytes).
        archive_usage (int | Unset): Total amount of currently used Archive tier storage space (in bytes).
    """

    snapshots_count: int | Unset = UNSET
    archives_count: int | Unset = UNSET
    backup_count: int | Unset = UNSET
    total_usage: int | Unset = UNSET
    hot_usage: int | Unset = UNSET
    cool_usage: int | Unset = UNSET
    archive_usage: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshots_count = self.snapshots_count

        archives_count = self.archives_count

        backup_count = self.backup_count

        total_usage = self.total_usage

        hot_usage = self.hot_usage

        cool_usage = self.cool_usage

        archive_usage = self.archive_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshots_count is not UNSET:
            field_dict["snapshotsCount"] = snapshots_count
        if archives_count is not UNSET:
            field_dict["archivesCount"] = archives_count
        if backup_count is not UNSET:
            field_dict["backupCount"] = backup_count
        if total_usage is not UNSET:
            field_dict["totalUsage"] = total_usage
        if hot_usage is not UNSET:
            field_dict["hotUsage"] = hot_usage
        if cool_usage is not UNSET:
            field_dict["coolUsage"] = cool_usage
        if archive_usage is not UNSET:
            field_dict["archiveUsage"] = archive_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshots_count = d.pop("snapshotsCount", UNSET)

        archives_count = d.pop("archivesCount", UNSET)

        backup_count = d.pop("backupCount", UNSET)

        total_usage = d.pop("totalUsage", UNSET)

        hot_usage = d.pop("hotUsage", UNSET)

        cool_usage = d.pop("coolUsage", UNSET)

        archive_usage = d.pop("archiveUsage", UNSET)

        storage_usage_report = cls(
            snapshots_count=snapshots_count,
            archives_count=archives_count,
            backup_count=backup_count,
            total_usage=total_usage,
            hot_usage=hot_usage,
            cool_usage=cool_usage,
            archive_usage=archive_usage,
        )

        storage_usage_report.additional_properties = d
        return storage_usage_report

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
