from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive_sla_schedule import ArchiveSlaSchedule
    from ..models.daily_sla_schedule import DailySlaSchedule
    from ..models.health_check_schedule import HealthCheckSchedule
    from ..models.monthly_sla_schedule import MonthlySlaSchedule
    from ..models.time_window_sla_schedule import TimeWindowSlaSchedule
    from ..models.weekly_sla_schedule import WeeklySlaSchedule


T = TypeVar("T", bound="SlaBackupSchedule")


@_attrs_define
class SlaBackupSchedule:
    r"""Specifies scheduling, retention and archival settings for backups.

    Attributes:
        daily (DailySlaSchedule | Unset): Specifies the daily schedule settings.
        weekly (WeeklySlaSchedule | Unset): Specifies the weekly schedule settings.
        monthly (MonthlySlaSchedule | Unset): Specifies the monthly schedule settings.
        archive (ArchiveSlaSchedule | Unset): Specifies the backup archival settings.
        execution_window (TimeWindowSlaSchedule | Unset): Specifies a snapshot or a backup window during which the
            restore points will be created.
        health_check_schedule (HealthCheckSchedule | Unset): \[Applies if backup creation is enabled for the backup
            policy] Specifies the health check schedule settings.
        change_block_tracking_enabled (bool | None | Unset): Defines whether to enable Changed Block Tracking (CBT) for
            the template. Note that enabling CBT requires an extra snapshot to be permanently stored. For more information,
            see the <a href="https://helpcenter.veeam.com/docs/vbazure/guide/temporary_restore_points.html?ver=81">Veeam
            Backup for Microsoft Azure User Guide.</a>
    """

    daily: DailySlaSchedule | Unset = UNSET
    weekly: WeeklySlaSchedule | Unset = UNSET
    monthly: MonthlySlaSchedule | Unset = UNSET
    archive: ArchiveSlaSchedule | Unset = UNSET
    execution_window: TimeWindowSlaSchedule | Unset = UNSET
    health_check_schedule: HealthCheckSchedule | Unset = UNSET
    change_block_tracking_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily, Unset):
            daily = self.daily.to_dict()

        weekly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weekly, Unset):
            weekly = self.weekly.to_dict()

        monthly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        archive: dict[str, Any] | Unset = UNSET
        if not isinstance(self.archive, Unset):
            archive = self.archive.to_dict()

        execution_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_window, Unset):
            execution_window = self.execution_window.to_dict()

        health_check_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health_check_schedule, Unset):
            health_check_schedule = self.health_check_schedule.to_dict()

        change_block_tracking_enabled: bool | None | Unset
        if isinstance(self.change_block_tracking_enabled, Unset):
            change_block_tracking_enabled = UNSET
        else:
            change_block_tracking_enabled = self.change_block_tracking_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily is not UNSET:
            field_dict["daily"] = daily
        if weekly is not UNSET:
            field_dict["weekly"] = weekly
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if archive is not UNSET:
            field_dict["archive"] = archive
        if execution_window is not UNSET:
            field_dict["executionWindow"] = execution_window
        if health_check_schedule is not UNSET:
            field_dict["healthCheckSchedule"] = health_check_schedule
        if change_block_tracking_enabled is not UNSET:
            field_dict["changeBlockTrackingEnabled"] = change_block_tracking_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archive_sla_schedule import ArchiveSlaSchedule
        from ..models.daily_sla_schedule import DailySlaSchedule
        from ..models.health_check_schedule import HealthCheckSchedule
        from ..models.monthly_sla_schedule import MonthlySlaSchedule
        from ..models.time_window_sla_schedule import TimeWindowSlaSchedule
        from ..models.weekly_sla_schedule import WeeklySlaSchedule

        d = dict(src_dict)
        _daily = d.pop("daily", UNSET)
        daily: DailySlaSchedule | Unset
        if isinstance(_daily, Unset):
            daily = UNSET
        else:
            daily = DailySlaSchedule.from_dict(_daily)

        _weekly = d.pop("weekly", UNSET)
        weekly: WeeklySlaSchedule | Unset
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = WeeklySlaSchedule.from_dict(_weekly)

        _monthly = d.pop("monthly", UNSET)
        monthly: MonthlySlaSchedule | Unset
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = MonthlySlaSchedule.from_dict(_monthly)

        _archive = d.pop("archive", UNSET)
        archive: ArchiveSlaSchedule | Unset
        if isinstance(_archive, Unset):
            archive = UNSET
        else:
            archive = ArchiveSlaSchedule.from_dict(_archive)

        _execution_window = d.pop("executionWindow", UNSET)
        execution_window: TimeWindowSlaSchedule | Unset
        if isinstance(_execution_window, Unset):
            execution_window = UNSET
        else:
            execution_window = TimeWindowSlaSchedule.from_dict(_execution_window)

        _health_check_schedule = d.pop("healthCheckSchedule", UNSET)
        health_check_schedule: HealthCheckSchedule | Unset
        if isinstance(_health_check_schedule, Unset):
            health_check_schedule = UNSET
        else:
            health_check_schedule = HealthCheckSchedule.from_dict(_health_check_schedule)

        def _parse_change_block_tracking_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        change_block_tracking_enabled = _parse_change_block_tracking_enabled(d.pop("changeBlockTrackingEnabled", UNSET))

        sla_backup_schedule = cls(
            daily=daily,
            weekly=weekly,
            monthly=monthly,
            archive=archive,
            execution_window=execution_window,
            health_check_schedule=health_check_schedule,
            change_block_tracking_enabled=change_block_tracking_enabled,
        )

        sla_backup_schedule.additional_properties = d
        return sla_backup_schedule

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
