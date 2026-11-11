from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.int_range import IntRange


T = TypeVar("T", bound="UIOptionsStorageDurationRanges")


@_attrs_define
class UIOptionsStorageDurationRanges:
    """
    Attributes:
        inferred (IntRange | Unset):
        hot (IntRange | Unset):
        cool (IntRange | Unset):
        archive (IntRange | Unset):
    """

    inferred: IntRange | Unset = UNSET
    hot: IntRange | Unset = UNSET
    cool: IntRange | Unset = UNSET
    archive: IntRange | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        inferred: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inferred, Unset):
            inferred = self.inferred.to_dict()

        hot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hot, Unset):
            hot = self.hot.to_dict()

        cool: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cool, Unset):
            cool = self.cool.to_dict()

        archive: dict[str, Any] | Unset = UNSET
        if not isinstance(self.archive, Unset):
            archive = self.archive.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if inferred is not UNSET:
            field_dict["Inferred"] = inferred
        if hot is not UNSET:
            field_dict["Hot"] = hot
        if cool is not UNSET:
            field_dict["Cool"] = cool
        if archive is not UNSET:
            field_dict["Archive"] = archive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.int_range import IntRange

        d = dict(src_dict)
        _inferred = d.pop("Inferred", UNSET)
        inferred: IntRange | Unset
        if isinstance(_inferred, Unset):
            inferred = UNSET
        else:
            inferred = IntRange.from_dict(_inferred)

        _hot = d.pop("Hot", UNSET)
        hot: IntRange | Unset
        if isinstance(_hot, Unset):
            hot = UNSET
        else:
            hot = IntRange.from_dict(_hot)

        _cool = d.pop("Cool", UNSET)
        cool: IntRange | Unset
        if isinstance(_cool, Unset):
            cool = UNSET
        else:
            cool = IntRange.from_dict(_cool)

        _archive = d.pop("Archive", UNSET)
        archive: IntRange | Unset
        if isinstance(_archive, Unset):
            archive = UNSET
        else:
            archive = IntRange.from_dict(_archive)

        ui_options_storage_duration_ranges = cls(
            inferred=inferred,
            hot=hot,
            cool=cool,
            archive=archive,
        )

        return ui_options_storage_duration_ranges
