from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_retention_settings import RepositoryRetentionSettings


T = TypeVar("T", bound="DailyBackupSchedule")


@_attrs_define
class DailyBackupSchedule:
    """Specifies the daily schedule settings for the backup policy.

    Attributes:
        hours (list[int] | None | Unset): Hours when the backup policy must start creating image-level backups.
        retention (RepositoryRetentionSettings | Unset): Specifies period of time to keep restore points in a backup
            chain.
        target_repository_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API
            to the target backup repository.
    """

    hours: list[int] | None | Unset = UNSET
    retention: RepositoryRetentionSettings | Unset = UNSET
    target_repository_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        hours: list[int] | None | Unset
        if isinstance(self.hours, Unset):
            hours = UNSET
        elif isinstance(self.hours, list):
            hours = self.hours

        else:
            hours = self.hours

        retention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention.to_dict()

        target_repository_id: None | str | Unset
        if isinstance(self.target_repository_id, Unset):
            target_repository_id = UNSET
        else:
            target_repository_id = self.target_repository_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if hours is not UNSET:
            field_dict["hours"] = hours
        if retention is not UNSET:
            field_dict["retention"] = retention
        if target_repository_id is not UNSET:
            field_dict["targetRepositoryId"] = target_repository_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_retention_settings import RepositoryRetentionSettings

        d = dict(src_dict)

        def _parse_hours(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hours_type_0 = cast(list[int], data)

                return hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        hours = _parse_hours(d.pop("hours", UNSET))

        _retention = d.pop("retention", UNSET)
        retention: RepositoryRetentionSettings | Unset
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = RepositoryRetentionSettings.from_dict(_retention)

        def _parse_target_repository_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_repository_id = _parse_target_repository_id(d.pop("targetRepositoryId", UNSET))

        daily_backup_schedule = cls(
            hours=hours,
            retention=retention,
            target_repository_id=target_repository_id,
        )

        return daily_backup_schedule
