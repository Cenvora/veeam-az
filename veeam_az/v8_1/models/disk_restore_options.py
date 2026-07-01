from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.disk_type import DiskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_subscription import AzureSubscription
    from ..models.region import Region
    from ..models.resource_group import ResourceGroup
    from ..models.storage_account import StorageAccount


T = TypeVar("T", bound="DiskRestoreOptions")


@_attrs_define
class DiskRestoreOptions:
    """/[Applies only if restore to a new location or with different settings is performed/] Specifies disk restore
    settings.

        Attributes:
            region (Region | Unset): Specifies Azure regions for which the operation is performed.
            service_account_id (str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST
                API to a service account whose permissions will be used to perform the restore operation.
            subscription (AzureSubscription | Unset): Specifies information on an Azure subscription.
            type_ (DiskType | Unset): Specifies the type of the virtual disk.
            availability_zone (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure
                REST API to an Availability Zone to which the virtual disks will be restored.
            disk_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API
                to a virtual disk that will be restored.
            name (None | str | Unset): Specifies a name for the restored virtual disk.
            resource_group (ResourceGroup | Unset): Specifies information on a resource group.
            storage_account (StorageAccount | Unset): Specifies information on a storage account.
    """

    region: Region | Unset = UNSET
    service_account_id: str | Unset = UNSET
    subscription: AzureSubscription | Unset = UNSET
    type_: DiskType | Unset = UNSET
    availability_zone: None | str | Unset = UNSET
    disk_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    storage_account: StorageAccount | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        service_account_id = self.service_account_id

        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        availability_zone: None | str | Unset
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

        disk_id: None | str | Unset
        if isinstance(self.disk_id, Unset):
            disk_id = UNSET
        else:
            disk_id = self.disk_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        resource_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = self.resource_group.to_dict()

        storage_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_account, Unset):
            storage_account = self.storage_account.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if type_ is not UNSET:
            field_dict["type"] = type_
        if availability_zone is not UNSET:
            field_dict["availabilityZone"] = availability_zone
        if disk_id is not UNSET:
            field_dict["diskId"] = disk_id
        if name is not UNSET:
            field_dict["name"] = name
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if storage_account is not UNSET:
            field_dict["storageAccount"] = storage_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_subscription import AzureSubscription
        from ..models.region import Region
        from ..models.resource_group import ResourceGroup
        from ..models.storage_account import StorageAccount

        d = dict(src_dict)
        _region = d.pop("region", UNSET)
        region: Region | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

        service_account_id = d.pop("serviceAccountId", UNSET)

        _subscription = d.pop("subscription", UNSET)
        subscription: AzureSubscription | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = AzureSubscription.from_dict(_subscription)

        _type_ = d.pop("type", UNSET)
        type_: DiskType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DiskType(_type_)

        def _parse_availability_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        availability_zone = _parse_availability_zone(d.pop("availabilityZone", UNSET))

        def _parse_disk_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disk_id = _parse_disk_id(d.pop("diskId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _resource_group = d.pop("resourceGroup", UNSET)
        resource_group: ResourceGroup | Unset
        if isinstance(_resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = ResourceGroup.from_dict(_resource_group)

        _storage_account = d.pop("storageAccount", UNSET)
        storage_account: StorageAccount | Unset
        if isinstance(_storage_account, Unset):
            storage_account = UNSET
        else:
            storage_account = StorageAccount.from_dict(_storage_account)

        disk_restore_options = cls(
            region=region,
            service_account_id=service_account_id,
            subscription=subscription,
            type_=type_,
            availability_zone=availability_zone,
            disk_id=disk_id,
            name=name,
            resource_group=resource_group,
            storage_account=storage_account,
        )

        return disk_restore_options
