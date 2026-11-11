from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.region import Region


T = TypeVar("T", bound="WorkerProfile")


@_attrs_define
class WorkerProfile:
    r"""
    Attributes:
        min_instances (int | Unset): Number of worker instances that are deployed in the specified region and kept in
            the Azure environment even when no operations are performed by Veeam Backup for Microsoft Azure.
        max_instances (int | Unset): Maximum number of worker instances that can be deployed in the specified region and
            used simultaneously to process Azure resources during backup and restore operations. <br> **Note**: After a
            backup or restore operation completes, Veeam Backup for Microsoft Azure keeps the minimum number of worker
            instances running for 10 minutes and then deallocates them; other instances are automatically removed from the
            backup infrastructure.
        region (Region | Unset): Specifies Azure regions for which the operation is performed.
        virtual_machine_simple_type (None | str | Unset): \[Applies only if one single VM size will be used to launch
            all worker instances in the specified region] Profile used for backup, restore and archive operations.
        virtual_machine_small_type (None | str | Unset): Profile used to create image-level backups and restore data if
            the total disk size of the processed Azure VM or the total size of the processed Azure SQL database is less than
            100 GB.
        virtual_machine_medium_type (None | str | Unset): Profile used to create image-level backups and restore data if
            the total disk size of the processed Azure VM or the total size of the processed Azure SQL database is 100 GB -
            1 TB.
        virtual_machine_large_type (None | str | Unset): Profile used to create image-level backups and restore data if
            the total disk size of the processed Azure VM or the total size of the processed Azure SQL database is more than
            1 TB.
        virtual_machine_archive_type (None | str | Unset): Profile used to create archived backups.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    min_instances: int | Unset = UNSET
    max_instances: int | Unset = UNSET
    region: Region | Unset = UNSET
    virtual_machine_simple_type: None | str | Unset = UNSET
    virtual_machine_small_type: None | str | Unset = UNSET
    virtual_machine_medium_type: None | str | Unset = UNSET
    virtual_machine_large_type: None | str | Unset = UNSET
    virtual_machine_archive_type: None | str | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        min_instances = self.min_instances

        max_instances = self.max_instances

        region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

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

        virtual_machine_archive_type: None | str | Unset
        if isinstance(self.virtual_machine_archive_type, Unset):
            virtual_machine_archive_type = UNSET
        else:
            virtual_machine_archive_type = self.virtual_machine_archive_type

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if min_instances is not UNSET:
            field_dict["minInstances"] = min_instances
        if max_instances is not UNSET:
            field_dict["maxInstances"] = max_instances
        if region is not UNSET:
            field_dict["region"] = region
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
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.region import Region

        d = dict(src_dict)
        min_instances = d.pop("minInstances", UNSET)

        max_instances = d.pop("maxInstances", UNSET)

        _region = d.pop("region", UNSET)
        region: Region | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

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

        def _parse_virtual_machine_archive_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_machine_archive_type = _parse_virtual_machine_archive_type(d.pop("virtualMachineArchiveType", UNSET))

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        worker_profile = cls(
            min_instances=min_instances,
            max_instances=max_instances,
            region=region,
            virtual_machine_simple_type=virtual_machine_simple_type,
            virtual_machine_small_type=virtual_machine_small_type,
            virtual_machine_medium_type=virtual_machine_medium_type,
            virtual_machine_large_type=virtual_machine_large_type,
            virtual_machine_archive_type=virtual_machine_archive_type,
            field_links=field_links,
        )

        return worker_profile
