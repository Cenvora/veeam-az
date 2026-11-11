from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VmDiskSnapshot")


@_attrs_define
class VmDiskSnapshot:
    """Specifies virtual disks that must be excluded from restore.

    Attributes:
        disk_id (None | str | Unset): Specifies the system ID assigned to a virtual disk in the Veeam Backup for
            Microsoft Azure REST API.
        disk_name (None | str | Unset): Specifies a name of the disk.
    """

    disk_id: None | str | Unset = UNSET
    disk_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        disk_id: None | str | Unset
        if isinstance(self.disk_id, Unset):
            disk_id = UNSET
        else:
            disk_id = self.disk_id

        disk_name: None | str | Unset
        if isinstance(self.disk_name, Unset):
            disk_name = UNSET
        else:
            disk_name = self.disk_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if disk_id is not UNSET:
            field_dict["diskId"] = disk_id
        if disk_name is not UNSET:
            field_dict["diskName"] = disk_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_disk_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disk_id = _parse_disk_id(d.pop("diskId", UNSET))

        def _parse_disk_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disk_name = _parse_disk_name(d.pop("diskName", UNSET))

        vm_disk_snapshot = cls(
            disk_id=disk_id,
            disk_name=disk_name,
        )

        return vm_disk_snapshot
