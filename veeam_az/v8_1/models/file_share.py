from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="FileShare")


@_attrs_define
class FileShare:
    """Specifies information on a file share.

    Attributes:
        id (None | str | Unset): System ID assigned to the file share in the Veeam Backup for Microsoft Azure REST API.
        azure_id (None | str | Unset): Resource ID of the file share.
        name (None | str | Unset): Name of the file share.
        access_tier (None | str | Unset): Access tier applied to the file share.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the file share resides.
        region_name (None | str | Unset): Name of the Azure region where the file share resides.
        storage_account_name (None | str | Unset): Name of the storage account where the file share resides.
        resource_group_name (None | str | Unset): Name of a resource group where the file share belongs.
        size (int | None | Unset): Size of the file share (in bytes).
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to a subscription to which the file share belongs.
        tenant_id (None | str | Unset): Microsoft Azure ID assigned to a tenant to which the file share belongs.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    azure_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    access_tier: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    storage_account_name: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    size: int | None | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
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

        access_tier: None | str | Unset
        if isinstance(self.access_tier, Unset):
            access_tier = UNSET
        else:
            access_tier = self.access_tier

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        storage_account_name: None | str | Unset
        if isinstance(self.storage_account_name, Unset):
            storage_account_name = UNSET
        else:
            storage_account_name = self.storage_account_name

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

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
        if access_tier is not UNSET:
            field_dict["accessTier"] = access_tier
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if storage_account_name is not UNSET:
            field_dict["storageAccountName"] = storage_account_name
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if size is not UNSET:
            field_dict["size"] = size
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

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

        def _parse_access_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_tier = _parse_access_tier(d.pop("accessTier", UNSET))

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_storage_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_account_name = _parse_storage_account_name(d.pop("storageAccountName", UNSET))

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

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

        file_share = cls(
            id=id,
            azure_id=azure_id,
            name=name,
            access_tier=access_tier,
            region_id=region_id,
            region_name=region_name,
            storage_account_name=storage_account_name,
            resource_group_name=resource_group_name,
            size=size,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            field_links=field_links,
        )

        return file_share
