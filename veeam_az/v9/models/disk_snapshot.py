from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.disk_type import DiskType
from ..models.os_type_nullable import OSTypeNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_subscription import AzureSubscription
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.region import Region
    from ..models.resource_group import ResourceGroup
    from ..models.storage_account import StorageAccount


T = TypeVar("T", bound="DiskSnapshot")


@_attrs_define
class DiskSnapshot:
    """
    Attributes:
        name (None | str | Unset): Specifies the name of the virtual disk snapshot.
        disk_type (DiskType | Unset): Specifies the type of the virtual disk.
        sku (None | str | Unset): Specifies the SKU (Stock Keeping Unit) of the virtual disk.
        availability_zone (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure
            REST API to the Availability Zone where the virtual disk resides.
        size_in_gb (int | Unset): Specifies the size of the virtual disk (in GB).
        os_type (OSTypeNullable | Unset): Type of the operating system installed on the Azure VM.
        disk_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API
            to a virtual disk in the Veeam Backup for Microsoft Azure REST API.
        subscription (AzureSubscription | Unset): Specifies information on an Azure subscription.
        region (Region | Unset): Specifies Azure regions for which the operation is performed.
        resource_group (ResourceGroup | Unset): Specifies information on a resource group.
        storage_account (StorageAccount | Unset): Specifies information on a storage account.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
        disk_name (None | str | Unset): Specifies the name of the virtual disk.
        snapshot_accounts (list[UUID] | None | Unset): Specifies service accounts that have access to the snapshot.
    """

    name: None | str | Unset = UNSET
    disk_type: DiskType | Unset = UNSET
    sku: None | str | Unset = UNSET
    availability_zone: None | str | Unset = UNSET
    size_in_gb: int | Unset = UNSET
    os_type: OSTypeNullable | Unset = UNSET
    disk_id: None | str | Unset = UNSET
    subscription: AzureSubscription | Unset = UNSET
    region: Region | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    storage_account: StorageAccount | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET
    disk_name: None | str | Unset = UNSET
    snapshot_accounts: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        disk_type: str | Unset = UNSET
        if not isinstance(self.disk_type, Unset):
            disk_type = self.disk_type.value

        sku: None | str | Unset
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        availability_zone: None | str | Unset
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

        size_in_gb = self.size_in_gb

        os_type: str | Unset = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        disk_id: None | str | Unset
        if isinstance(self.disk_id, Unset):
            disk_id = UNSET
        else:
            disk_id = self.disk_id

        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        resource_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = self.resource_group.to_dict()

        storage_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_account, Unset):
            storage_account = self.storage_account.to_dict()

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        disk_name: None | str | Unset
        if isinstance(self.disk_name, Unset):
            disk_name = UNSET
        else:
            disk_name = self.disk_name

        snapshot_accounts: list[str] | None | Unset
        if isinstance(self.snapshot_accounts, Unset):
            snapshot_accounts = UNSET
        elif isinstance(self.snapshot_accounts, list):
            snapshot_accounts = []
            for snapshot_accounts_type_0_item_data in self.snapshot_accounts:
                snapshot_accounts_type_0_item = str(snapshot_accounts_type_0_item_data)
                snapshot_accounts.append(snapshot_accounts_type_0_item)

        else:
            snapshot_accounts = self.snapshot_accounts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if disk_type is not UNSET:
            field_dict["diskType"] = disk_type
        if sku is not UNSET:
            field_dict["sku"] = sku
        if availability_zone is not UNSET:
            field_dict["availabilityZone"] = availability_zone
        if size_in_gb is not UNSET:
            field_dict["sizeInGB"] = size_in_gb
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if disk_id is not UNSET:
            field_dict["diskId"] = disk_id
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if region is not UNSET:
            field_dict["region"] = region
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if storage_account is not UNSET:
            field_dict["storageAccount"] = storage_account
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if disk_name is not UNSET:
            field_dict["diskName"] = disk_name
        if snapshot_accounts is not UNSET:
            field_dict["snapshotAccounts"] = snapshot_accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_subscription import AzureSubscription
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.region import Region
        from ..models.resource_group import ResourceGroup
        from ..models.storage_account import StorageAccount

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _disk_type = d.pop("diskType", UNSET)
        disk_type: DiskType | Unset
        if isinstance(_disk_type, Unset):
            disk_type = UNSET
        else:
            disk_type = DiskType(_disk_type)

        def _parse_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku = _parse_sku(d.pop("sku", UNSET))

        def _parse_availability_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        availability_zone = _parse_availability_zone(d.pop("availabilityZone", UNSET))

        size_in_gb = d.pop("sizeInGB", UNSET)

        _os_type = d.pop("osType", UNSET)
        os_type: OSTypeNullable | Unset
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = OSTypeNullable(_os_type)

        def _parse_disk_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disk_id = _parse_disk_id(d.pop("diskId", UNSET))

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

        _storage_account = d.pop("storageAccount", UNSET)
        storage_account: StorageAccount | Unset
        if isinstance(_storage_account, Unset):
            storage_account = UNSET
        else:
            storage_account = StorageAccount.from_dict(_storage_account)

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

        def _parse_disk_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disk_name = _parse_disk_name(d.pop("diskName", UNSET))

        def _parse_snapshot_accounts(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                snapshot_accounts_type_0 = []
                _snapshot_accounts_type_0 = data
                for snapshot_accounts_type_0_item_data in _snapshot_accounts_type_0:
                    snapshot_accounts_type_0_item = UUID(snapshot_accounts_type_0_item_data)

                    snapshot_accounts_type_0.append(snapshot_accounts_type_0_item)

                return snapshot_accounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        snapshot_accounts = _parse_snapshot_accounts(d.pop("snapshotAccounts", UNSET))

        disk_snapshot = cls(
            name=name,
            disk_type=disk_type,
            sku=sku,
            availability_zone=availability_zone,
            size_in_gb=size_in_gb,
            os_type=os_type,
            disk_id=disk_id,
            subscription=subscription,
            region=region,
            resource_group=resource_group,
            storage_account=storage_account,
            field_links=field_links,
            disk_name=disk_name,
            snapshot_accounts=snapshot_accounts,
        )

        return disk_snapshot
