from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vm_disk_snapshot import VmDiskSnapshot


T = TypeVar("T", bound="DiskBulkRestoreToOriginalOptions")


@_attrs_define
class DiskBulkRestoreToOriginalOptions:
    """/[Applies only if restore to the original location is performed/] Specifies disk restore settings.

    Attributes:
        excluded_disks (list[VmDiskSnapshot] | None | Unset): Specifies information on virtual disks that will be
            excluded from the restore operation.
    """

    excluded_disks: list[VmDiskSnapshot] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        excluded_disks: list[dict[str, Any]] | None | Unset
        if isinstance(self.excluded_disks, Unset):
            excluded_disks = UNSET
        elif isinstance(self.excluded_disks, list):
            excluded_disks = []
            for excluded_disks_type_0_item_data in self.excluded_disks:
                excluded_disks_type_0_item = excluded_disks_type_0_item_data.to_dict()
                excluded_disks.append(excluded_disks_type_0_item)

        else:
            excluded_disks = self.excluded_disks

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if excluded_disks is not UNSET:
            field_dict["excludedDisks"] = excluded_disks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vm_disk_snapshot import VmDiskSnapshot

        d = dict(src_dict)

        def _parse_excluded_disks(data: object) -> list[VmDiskSnapshot] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_disks_type_0 = []
                _excluded_disks_type_0 = data
                for excluded_disks_type_0_item_data in _excluded_disks_type_0:
                    excluded_disks_type_0_item = VmDiskSnapshot.from_dict(excluded_disks_type_0_item_data)

                    excluded_disks_type_0.append(excluded_disks_type_0_item)

                return excluded_disks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VmDiskSnapshot] | None | Unset, data)

        excluded_disks = _parse_excluded_disks(d.pop("excludedDisks", UNSET))

        disk_bulk_restore_to_original_options = cls(
            excluded_disks=excluded_disks,
        )

        return disk_bulk_restore_to_original_options
