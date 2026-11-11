from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_restore_config_parameters import DatabaseRestoreConfigParameters
    from ..models.disk_restore_config_parameters import DiskRestoreConfigParameters
    from ..models.virtual_machine_restore_config_parameters import VirtualMachineRestoreConfigParameters


T = TypeVar("T", bound="RestoreConfigParameters")


@_attrs_define
class RestoreConfigParameters:
    """
    Attributes:
        virtual_machine (VirtualMachineRestoreConfigParameters | Unset):
        disks (list[DiskRestoreConfigParameters] | None | Unset):
        database (DatabaseRestoreConfigParameters | Unset):
    """

    virtual_machine: VirtualMachineRestoreConfigParameters | Unset = UNSET
    disks: list[DiskRestoreConfigParameters] | None | Unset = UNSET
    database: DatabaseRestoreConfigParameters | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        virtual_machine: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_machine, Unset):
            virtual_machine = self.virtual_machine.to_dict()

        disks: list[dict[str, Any]] | None | Unset
        if isinstance(self.disks, Unset):
            disks = UNSET
        elif isinstance(self.disks, list):
            disks = []
            for disks_type_0_item_data in self.disks:
                disks_type_0_item = disks_type_0_item_data.to_dict()
                disks.append(disks_type_0_item)

        else:
            disks = self.disks

        database: dict[str, Any] | Unset = UNSET
        if not isinstance(self.database, Unset):
            database = self.database.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if virtual_machine is not UNSET:
            field_dict["virtualMachine"] = virtual_machine
        if disks is not UNSET:
            field_dict["disks"] = disks
        if database is not UNSET:
            field_dict["database"] = database

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_restore_config_parameters import DatabaseRestoreConfigParameters
        from ..models.disk_restore_config_parameters import DiskRestoreConfigParameters
        from ..models.virtual_machine_restore_config_parameters import VirtualMachineRestoreConfigParameters

        d = dict(src_dict)
        _virtual_machine = d.pop("virtualMachine", UNSET)
        virtual_machine: VirtualMachineRestoreConfigParameters | Unset
        if isinstance(_virtual_machine, Unset):
            virtual_machine = UNSET
        else:
            virtual_machine = VirtualMachineRestoreConfigParameters.from_dict(_virtual_machine)

        def _parse_disks(data: object) -> list[DiskRestoreConfigParameters] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disks_type_0 = []
                _disks_type_0 = data
                for disks_type_0_item_data in _disks_type_0:
                    disks_type_0_item = DiskRestoreConfigParameters.from_dict(disks_type_0_item_data)

                    disks_type_0.append(disks_type_0_item)

                return disks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DiskRestoreConfigParameters] | None | Unset, data)

        disks = _parse_disks(d.pop("disks", UNSET))

        _database = d.pop("database", UNSET)
        database: DatabaseRestoreConfigParameters | Unset
        if isinstance(_database, Unset):
            database = UNSET
        else:
            database = DatabaseRestoreConfigParameters.from_dict(_database)

        restore_config_parameters = cls(
            virtual_machine=virtual_machine,
            disks=disks,
            database=database,
        )

        return restore_config_parameters
