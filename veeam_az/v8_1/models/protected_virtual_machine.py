from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.azure_environment import AzureEnvironment
from ..models.os_type_nullable import OSTypeNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_subscription import AzureSubscription
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.region import Region
    from ..models.resource_group import ResourceGroup


T = TypeVar("T", bound="ProtectedVirtualMachine")


@_attrs_define
class ProtectedVirtualMachine:
    """Information on each protected Azure VM.

    Attributes:
        id (None | str | Unset): System ID assigned to the protected Azure VM in the Veeam Backup for Microsoft Azure
            REST API.
        azure_id (None | str | Unset): Resource ID of the protected Azure VM.
        name (None | str | Unset): Name of the protected Azure VM.
        azure_environment (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        os_type (OSTypeNullable | Unset): Type of the operating system installed on the Azure VM.
        region_name (None | str | Unset): Name of the Azure region where the protected Azure VM resides.
        total_size_in_gb (int | Unset): Total size of all virtual disks attached to the protected Azure VM (in GB).
        vm_size (None | str | Unset): Size of the protected Azure VM.
        availability_zone (None | str | Unset): Specifies the Availability Zone where the protected Azure VM resides.
        is_controller (bool | Unset): Defines whether Veeam Backup for Microsoft Azure is installed on the protected
            Azure VM.
        last_backup (datetime.datetime | Unset): Date and time of the most recent backup of the protected Azure VM.
        subscription (AzureSubscription | Unset): Specifies information on an Azure subscription.
        region (Region | Unset): Specifies Azure regions for which the operation is performed.
        resource_group (ResourceGroup | Unset): Specifies information on a resource group.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    azure_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    azure_environment: AzureEnvironment | Unset = UNSET
    os_type: OSTypeNullable | Unset = UNSET
    region_name: None | str | Unset = UNSET
    total_size_in_gb: int | Unset = UNSET
    vm_size: None | str | Unset = UNSET
    availability_zone: None | str | Unset = UNSET
    is_controller: bool | Unset = UNSET
    last_backup: datetime.datetime | Unset = UNSET
    subscription: AzureSubscription | Unset = UNSET
    region: Region | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        azure_id: None | str | Unset
        if isinstance(self.azure_id, Unset):
            azure_id = UNSET
        else:
            azure_id = self.azure_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        os_type: str | Unset = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        total_size_in_gb = self.total_size_in_gb

        vm_size: None | str | Unset
        if isinstance(self.vm_size, Unset):
            vm_size = UNSET
        else:
            vm_size = self.vm_size

        availability_zone: None | str | Unset
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

        is_controller = self.is_controller

        last_backup: str | Unset = UNSET
        if not isinstance(self.last_backup, Unset):
            last_backup = self.last_backup.isoformat()

        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        resource_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = self.resource_group.to_dict()

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if azure_id is not UNSET:
            field_dict["azureId"] = azure_id
        if name is not UNSET:
            field_dict["name"] = name
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if total_size_in_gb is not UNSET:
            field_dict["totalSizeInGB"] = total_size_in_gb
        if vm_size is not UNSET:
            field_dict["vmSize"] = vm_size
        if availability_zone is not UNSET:
            field_dict["availabilityZone"] = availability_zone
        if is_controller is not UNSET:
            field_dict["isController"] = is_controller
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if region is not UNSET:
            field_dict["region"] = region
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_subscription import AzureSubscription
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.region import Region
        from ..models.resource_group import ResourceGroup

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_azure_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_id = _parse_azure_id(d.pop("azureId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureEnvironment | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureEnvironment(_azure_environment)

        _os_type = d.pop("osType", UNSET)
        os_type: OSTypeNullable | Unset
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = OSTypeNullable(_os_type)

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        total_size_in_gb = d.pop("totalSizeInGB", UNSET)

        def _parse_vm_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_size = _parse_vm_size(d.pop("vmSize", UNSET))

        def _parse_availability_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        availability_zone = _parse_availability_zone(d.pop("availabilityZone", UNSET))

        is_controller = d.pop("isController", UNSET)

        _last_backup = d.pop("lastBackup", UNSET)
        last_backup: datetime.datetime | Unset
        if isinstance(_last_backup, Unset):
            last_backup = UNSET
        else:
            last_backup = isoparse(_last_backup)

        _subscription = d.pop("subscription", UNSET)
        subscription: AzureSubscription | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = AzureSubscription.from_dict(_subscription)

        _region = d.pop("region", UNSET)
        region: Region | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

        _resource_group = d.pop("resourceGroup", UNSET)
        resource_group: ResourceGroup | Unset
        if isinstance(_resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = ResourceGroup.from_dict(_resource_group)

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

        protected_virtual_machine = cls(
            id=id,
            azure_id=azure_id,
            name=name,
            azure_environment=azure_environment,
            os_type=os_type,
            region_name=region_name,
            total_size_in_gb=total_size_in_gb,
            vm_size=vm_size,
            availability_zone=availability_zone,
            is_controller=is_controller,
            last_backup=last_backup,
            subscription=subscription,
            region=region,
            resource_group=resource_group,
            field_links=field_links,
        )

        return protected_virtual_machine
