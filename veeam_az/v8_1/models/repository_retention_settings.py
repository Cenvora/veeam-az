from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.retention_duration_type_nullable import RetentionDurationTypeNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryRetentionSettings")


@_attrs_define
class RepositoryRetentionSettings:
    """Specifies period of time to keep restore points in a backup chain.

    Attributes:
        time_retention_duration (int | None | Unset): Specifies the number of days, weeks, months or years to keep
            restore points in a backup chain.
        retention_duration_type (RetentionDurationTypeNullable | Unset): Specifies the type of the period.
    """

    time_retention_duration: int | None | Unset = UNSET
    retention_duration_type: RetentionDurationTypeNullable | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        time_retention_duration: int | None | Unset
        if isinstance(self.time_retention_duration, Unset):
            time_retention_duration = UNSET
        else:
            time_retention_duration = self.time_retention_duration

        retention_duration_type: str | Unset = UNSET
        if not isinstance(self.retention_duration_type, Unset):
            retention_duration_type = self.retention_duration_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if time_retention_duration is not UNSET:
            field_dict["timeRetentionDuration"] = time_retention_duration
        if retention_duration_type is not UNSET:
            field_dict["retentionDurationType"] = retention_duration_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_time_retention_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_retention_duration = _parse_time_retention_duration(d.pop("timeRetentionDuration", UNSET))

        _retention_duration_type = d.pop("retentionDurationType", UNSET)
        retention_duration_type: RetentionDurationTypeNullable | Unset
        if isinstance(_retention_duration_type, Unset):
            retention_duration_type = UNSET
        else:
            retention_duration_type = RetentionDurationTypeNullable(_retention_duration_type)

        repository_retention_settings = cls(
            time_retention_duration=time_retention_duration,
            retention_duration_type=retention_duration_type,
        )

        return repository_retention_settings
