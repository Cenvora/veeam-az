from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ui_options_storage_duration_ranges import UIOptionsStorageDurationRanges


T = TypeVar("T", bound="UIOptions")


@_attrs_define
class UIOptions:
    """
    Attributes:
        storage_duration_ranges (UIOptionsStorageDurationRanges | Unset):
    """

    storage_duration_ranges: UIOptionsStorageDurationRanges | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        storage_duration_ranges: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_duration_ranges, Unset):
            storage_duration_ranges = self.storage_duration_ranges.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if storage_duration_ranges is not UNSET:
            field_dict["storageDurationRanges"] = storage_duration_ranges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_options_storage_duration_ranges import UIOptionsStorageDurationRanges

        d = dict(src_dict)
        _storage_duration_ranges = d.pop("storageDurationRanges", UNSET)
        storage_duration_ranges: UIOptionsStorageDurationRanges | Unset
        if isinstance(_storage_duration_ranges, Unset):
            storage_duration_ranges = UNSET
        else:
            storage_duration_ranges = UIOptionsStorageDurationRanges.from_dict(_storage_duration_ranges)

        ui_options = cls(
            storage_duration_ranges=storage_duration_ranges,
        )

        return ui_options
