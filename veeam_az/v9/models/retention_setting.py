from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.retention_duration_type_nullable import RetentionDurationTypeNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="RetentionSetting")


@_attrs_define
class RetentionSetting:
    """Global retention settings for keeping session records (for `sessionsSettings`, the minimum possible value is 1 day)
    or snapshots of unprotected Azure VMs (for `obsoleteSnapshotsSettings`, the minimum possible value is 15 days).

        Attributes:
            duration (int | None | Unset): Number of periods to keep snapshots or session records.
            type_ (RetentionDurationTypeNullable | Unset): Specifies the type of the period.
            keep_forever (bool | None | Unset): Defines whether to keep all session records in the configuration database.
    """

    duration: int | None | Unset = UNSET
    type_: RetentionDurationTypeNullable | Unset = UNSET
    keep_forever: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        duration: int | None | Unset
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        keep_forever: bool | None | Unset
        if isinstance(self.keep_forever, Unset):
            keep_forever = UNSET
        else:
            keep_forever = self.keep_forever

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if type_ is not UNSET:
            field_dict["type"] = type_
        if keep_forever is not UNSET:
            field_dict["keepForever"] = keep_forever

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration = _parse_duration(d.pop("duration", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: RetentionDurationTypeNullable | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RetentionDurationTypeNullable(_type_)

        def _parse_keep_forever(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keep_forever = _parse_keep_forever(d.pop("keepForever", UNSET))

        retention_setting = cls(
            duration=duration,
            type_=type_,
            keep_forever=keep_forever,
        )

        return retention_setting
