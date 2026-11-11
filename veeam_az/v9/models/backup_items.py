from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_machine_to_backup import VirtualMachineToBackup


T = TypeVar("T", bound="BackupItems")


@_attrs_define
class BackupItems:
    """Specifies a list of Azure VMs for which snapshots must be created.

    Attributes:
        virtual_machines (list[VirtualMachineToBackup] | None | Unset):
    """

    virtual_machines: list[VirtualMachineToBackup] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        virtual_machines: list[dict[str, Any]] | None | Unset
        if isinstance(self.virtual_machines, Unset):
            virtual_machines = UNSET
        elif isinstance(self.virtual_machines, list):
            virtual_machines = []
            for virtual_machines_type_0_item_data in self.virtual_machines:
                virtual_machines_type_0_item = virtual_machines_type_0_item_data.to_dict()
                virtual_machines.append(virtual_machines_type_0_item)

        else:
            virtual_machines = self.virtual_machines

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if virtual_machines is not UNSET:
            field_dict["virtualMachines"] = virtual_machines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.virtual_machine_to_backup import VirtualMachineToBackup

        d = dict(src_dict)

        def _parse_virtual_machines(data: object) -> list[VirtualMachineToBackup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                virtual_machines_type_0 = []
                _virtual_machines_type_0 = data
                for virtual_machines_type_0_item_data in _virtual_machines_type_0:
                    virtual_machines_type_0_item = VirtualMachineToBackup.from_dict(virtual_machines_type_0_item_data)

                    virtual_machines_type_0.append(virtual_machines_type_0_item)

                return virtual_machines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VirtualMachineToBackup] | None | Unset, data)

        virtual_machines = _parse_virtual_machines(d.pop("virtualMachines", UNSET))

        backup_items = cls(
            virtual_machines=virtual_machines,
        )

        return backup_items
