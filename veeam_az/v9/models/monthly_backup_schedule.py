from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.month import Month
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_retention_settings import RepositoryRetentionSettings


T = TypeVar("T", bound="MonthlyBackupSchedule")


@_attrs_define
class MonthlyBackupSchedule:
    """Specifies the monthly schedule settings for image-level backups.

    Attributes:
        selected_months (list[Month] | None | Unset): Specifies the months when the backup policy must start creating
            cloud-native snapshots.
        retention (RepositoryRetentionSettings | Unset): Specifies period of time to keep restore points in a backup
            chain.
        target_repository_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft
            Azure REST API to the target backup repository.
    """

    selected_months: list[Month] | None | Unset = UNSET
    retention: RepositoryRetentionSettings | Unset = UNSET
    target_repository_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        selected_months: list[str] | None | Unset
        if isinstance(self.selected_months, Unset):
            selected_months = UNSET
        elif isinstance(self.selected_months, list):
            selected_months = []
            for selected_months_type_0_item_data in self.selected_months:
                selected_months_type_0_item = selected_months_type_0_item_data.value
                selected_months.append(selected_months_type_0_item)

        else:
            selected_months = self.selected_months

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
        if selected_months is not UNSET:
            field_dict["selectedMonths"] = selected_months
        if retention is not UNSET:
            field_dict["retention"] = retention
        if target_repository_id is not UNSET:
            field_dict["targetRepositoryId"] = target_repository_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_retention_settings import RepositoryRetentionSettings

        d = dict(src_dict)

        def _parse_selected_months(data: object) -> list[Month] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_months_type_0 = []
                _selected_months_type_0 = data
                for selected_months_type_0_item_data in _selected_months_type_0:
                    selected_months_type_0_item = Month(selected_months_type_0_item_data)

                    selected_months_type_0.append(selected_months_type_0_item)

                return selected_months_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Month] | None | Unset, data)

        selected_months = _parse_selected_months(d.pop("selectedMonths", UNSET))

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

        monthly_backup_schedule = cls(
            selected_months=selected_months,
            retention=retention,
            target_repository_id=target_repository_id,
        )

        return monthly_backup_schedule
