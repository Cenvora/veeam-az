from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetentionJobInfo")


@_attrs_define
class RetentionJobInfo:
    """Information on the removed restore points.

    Attributes:
        deleted_restore_points_count (int | Unset): Number of restore points removed from configuration database.
    """

    deleted_restore_points_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        deleted_restore_points_count = self.deleted_restore_points_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if deleted_restore_points_count is not UNSET:
            field_dict["deletedRestorePointsCount"] = deleted_restore_points_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted_restore_points_count = d.pop("deletedRestorePointsCount", UNSET)

        retention_job_info = cls(
            deleted_restore_points_count=deleted_restore_points_count,
        )

        return retention_job_info
