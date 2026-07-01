from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerProfileFromClient")


@_attrs_define
class WorkerProfileFromClient:
    r"""
    Attributes:
        region_id (str): Specifies a Microsoft Azure ID assigned to a region for which a set of worker profiles will be
            added.
        min_instances (int | Unset): Specifies number of worker instances that are deployed in the specified region and
            kept in the Azure environment even when no operations are performed by Veeam Backup for Microsoft Azure.
        max_instances (int | Unset): Specifies a maximum number of worker instances that can be deployed in the
            specified region and used simultaneously to process Azure resources during backup and restore operations. <br>
            **Note**: After a backup or restore operation completes, Veeam Backup for Microsoft Azure keeps the minimum
            number of worker instances running for 10 minutes and then deallocates them; the other instances are
            automatically removed from the backup infrastructure.
        virtual_machine_simple_type (None | str | Unset): \[Applies only if one single VM size will be used to launch
            all worker instances in the specified region] Specifies a profile used for backup, restore and archive
            operations.
        virtual_machine_small_type (None | str | Unset): Specifies a profile used to create image-level backups and
            restore data if the total disk size of the processed Azure VM or the total size of the processed Azure SQL
            database is less than 100 GB.
        virtual_machine_medium_type (None | str | Unset): Specifies a profile used to create image-level backups and
            restore data if the total disk size of the processed Azure VM or the total size of the processed Azure SQL
            database is 100 GB - 1 TB.
        virtual_machine_large_type (None | str | Unset): Specifies a profile used to create image-level backups and
            restore data if the total disk size of the processed Azure VM or the total size of the processed Azure SQL
            database is more than 1 TB.
        virtual_machine_archive_type (str | Unset): Specifies a profile used to create archived backups.
    """

    region_id: str
    min_instances: int | Unset = UNSET
    max_instances: int | Unset = UNSET
    virtual_machine_simple_type: None | str | Unset = UNSET
    virtual_machine_small_type: None | str | Unset = UNSET
    virtual_machine_medium_type: None | str | Unset = UNSET
    virtual_machine_large_type: None | str | Unset = UNSET
    virtual_machine_archive_type: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        region_id = self.region_id

        min_instances = self.min_instances

        max_instances = self.max_instances

        virtual_machine_simple_type: None | str | Unset
        if isinstance(self.virtual_machine_simple_type, Unset):
            virtual_machine_simple_type = UNSET
        else:
            virtual_machine_simple_type = self.virtual_machine_simple_type

        virtual_machine_small_type: None | str | Unset
        if isinstance(self.virtual_machine_small_type, Unset):
            virtual_machine_small_type = UNSET
        else:
            virtual_machine_small_type = self.virtual_machine_small_type

        virtual_machine_medium_type: None | str | Unset
        if isinstance(self.virtual_machine_medium_type, Unset):
            virtual_machine_medium_type = UNSET
        else:
            virtual_machine_medium_type = self.virtual_machine_medium_type

        virtual_machine_large_type: None | str | Unset
        if isinstance(self.virtual_machine_large_type, Unset):
            virtual_machine_large_type = UNSET
        else:
            virtual_machine_large_type = self.virtual_machine_large_type

        virtual_machine_archive_type = self.virtual_machine_archive_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "regionId": region_id,
            }
        )
        if min_instances is not UNSET:
            field_dict["minInstances"] = min_instances
        if max_instances is not UNSET:
            field_dict["maxInstances"] = max_instances
        if virtual_machine_simple_type is not UNSET:
            field_dict["virtualMachineSimpleType"] = virtual_machine_simple_type
        if virtual_machine_small_type is not UNSET:
            field_dict["virtualMachineSmallType"] = virtual_machine_small_type
        if virtual_machine_medium_type is not UNSET:
            field_dict["virtualMachineMediumType"] = virtual_machine_medium_type
        if virtual_machine_large_type is not UNSET:
            field_dict["virtualMachineLargeType"] = virtual_machine_large_type
        if virtual_machine_archive_type is not UNSET:
            field_dict["virtualMachineArchiveType"] = virtual_machine_archive_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        region_id = d.pop("regionId")

        min_instances = d.pop("minInstances", UNSET)

        max_instances = d.pop("maxInstances", UNSET)

        def _parse_virtual_machine_simple_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_machine_simple_type = _parse_virtual_machine_simple_type(d.pop("virtualMachineSimpleType", UNSET))

        def _parse_virtual_machine_small_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_machine_small_type = _parse_virtual_machine_small_type(d.pop("virtualMachineSmallType", UNSET))

        def _parse_virtual_machine_medium_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_machine_medium_type = _parse_virtual_machine_medium_type(d.pop("virtualMachineMediumType", UNSET))

        def _parse_virtual_machine_large_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_machine_large_type = _parse_virtual_machine_large_type(d.pop("virtualMachineLargeType", UNSET))

        virtual_machine_archive_type = d.pop("virtualMachineArchiveType", UNSET)

        worker_profile_from_client = cls(
            region_id=region_id,
            min_instances=min_instances,
            max_instances=max_instances,
            virtual_machine_simple_type=virtual_machine_simple_type,
            virtual_machine_small_type=virtual_machine_small_type,
            virtual_machine_medium_type=virtual_machine_medium_type,
            virtual_machine_large_type=virtual_machine_large_type,
            virtual_machine_archive_type=virtual_machine_archive_type,
        )

        return worker_profile_from_client
