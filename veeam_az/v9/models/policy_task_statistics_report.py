from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyTaskStatisticsReport")


@_attrs_define
class PolicyTaskStatisticsReport:
    """
    Attributes:
        snapshots_count (int | Unset): Number of snapshots successfully created for the specified time period.
        backups_count (int | Unset): Number of backups successfully created for the specified time period.
        archives_count (int | Unset): Number of archived backups successfully created for the specified time period.
        snapshots_total_count (int | Unset): Total number of snapshots processed for the specified time period.
        backups_total_count (int | Unset): Total number of backups processed for the specified time period.
        archives_total_count (int | Unset): Total number of archived backups processed for the specified time period.
    """

    snapshots_count: int | Unset = UNSET
    backups_count: int | Unset = UNSET
    archives_count: int | Unset = UNSET
    snapshots_total_count: int | Unset = UNSET
    backups_total_count: int | Unset = UNSET
    archives_total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshots_count = self.snapshots_count

        backups_count = self.backups_count

        archives_count = self.archives_count

        snapshots_total_count = self.snapshots_total_count

        backups_total_count = self.backups_total_count

        archives_total_count = self.archives_total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshots_count is not UNSET:
            field_dict["snapshotsCount"] = snapshots_count
        if backups_count is not UNSET:
            field_dict["backupsCount"] = backups_count
        if archives_count is not UNSET:
            field_dict["archivesCount"] = archives_count
        if snapshots_total_count is not UNSET:
            field_dict["snapshotsTotalCount"] = snapshots_total_count
        if backups_total_count is not UNSET:
            field_dict["backupsTotalCount"] = backups_total_count
        if archives_total_count is not UNSET:
            field_dict["archivesTotalCount"] = archives_total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshots_count = d.pop("snapshotsCount", UNSET)

        backups_count = d.pop("backupsCount", UNSET)

        archives_count = d.pop("archivesCount", UNSET)

        snapshots_total_count = d.pop("snapshotsTotalCount", UNSET)

        backups_total_count = d.pop("backupsTotalCount", UNSET)

        archives_total_count = d.pop("archivesTotalCount", UNSET)

        policy_task_statistics_report = cls(
            snapshots_count=snapshots_count,
            backups_count=backups_count,
            archives_count=archives_count,
            snapshots_total_count=snapshots_total_count,
            backups_total_count=backups_total_count,
            archives_total_count=archives_total_count,
        )

        policy_task_statistics_report.additional_properties = d
        return policy_task_statistics_report

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
