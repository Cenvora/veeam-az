from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sla_backup_schedule import SlaBackupSchedule
    from ..models.sla_snapshot_schedule import SlaSnapshotSchedule
    from ..models.sla_threshold_settings import SlaThresholdSettings


T = TypeVar("T", bound="SlaConfiguration")


@_attrs_define
class SlaConfiguration:
    """Specifies the SLA template configuration.

    Attributes:
        snapshot (SlaSnapshotSchedule | Unset): Specifies scheduling and retention settings for snapshots.
        backup (SlaBackupSchedule | Unset): Specifies scheduling, retention and archival settings for backups.
        threshold (SlaThresholdSettings | Unset): Specifies the SLA threshold settings.
    """

    snapshot: SlaSnapshotSchedule | Unset = UNSET
    backup: SlaBackupSchedule | Unset = UNSET
    threshold: SlaThresholdSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict()

        backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup, Unset):
            backup = self.backup.to_dict()

        threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threshold, Unset):
            threshold = self.threshold.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot
        if backup is not UNSET:
            field_dict["backup"] = backup
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sla_backup_schedule import SlaBackupSchedule
        from ..models.sla_snapshot_schedule import SlaSnapshotSchedule
        from ..models.sla_threshold_settings import SlaThresholdSettings

        d = dict(src_dict)
        _snapshot = d.pop("snapshot", UNSET)
        snapshot: SlaSnapshotSchedule | Unset
        if isinstance(_snapshot, Unset):
            snapshot = UNSET
        else:
            snapshot = SlaSnapshotSchedule.from_dict(_snapshot)

        _backup = d.pop("backup", UNSET)
        backup: SlaBackupSchedule | Unset
        if isinstance(_backup, Unset):
            backup = UNSET
        else:
            backup = SlaBackupSchedule.from_dict(_backup)

        _threshold = d.pop("threshold", UNSET)
        threshold: SlaThresholdSettings | Unset
        if isinstance(_threshold, Unset):
            threshold = UNSET
        else:
            threshold = SlaThresholdSettings.from_dict(_threshold)

        sla_configuration = cls(
            snapshot=snapshot,
            backup=backup,
            threshold=threshold,
        )

        sla_configuration.additional_properties = d
        return sla_configuration

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
