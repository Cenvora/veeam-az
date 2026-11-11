from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.storage_account_performance import StorageAccountPerformance
from ..models.storage_account_redundancy import StorageAccountRedundancy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="StorageAccount")


@_attrs_define
class StorageAccount:
    """Specifies information on a storage account.

    Attributes:
        id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to a
            storage account.
        resource_id (None | str | Unset): Specifies the complete resource ID containing all information on the storage
            account.
        name (None | str | Unset): Specifies the name of the storage account.
        sku_name (None | str | Unset): Specifies the name of a SKU (Stock Keeping Unit).
        performance (StorageAccountPerformance | Unset): Specifies the type of a performance tier specified for the
            storage account.
        redundancy (StorageAccountRedundancy | Unset): Specifies the type of Azure storage data redundancy.
        access_tier (None | str | Unset): Specifies an access tier of the storage account.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the storage account resides.
        region_name (None | str | Unset): Specifies the name of the Azure region.
        resource_group_name (None | str | Unset): Name of an Azure resource group to which the storage account belongs.
        removed_from_azure (bool | Unset): Defines whether the storage account was removed form the Microsoft Azure
            infrastructure.
        supports_tiering (bool | Unset): Defines whether the storage account supports tiering.
        is_immutable_storage (bool | Unset): Defines whether the *Enable versioning for blobs* option is enabled for the
            storage account.
        is_immutable_storage_policy_locked (bool | Unset): Defines whether the storage account is locked by time-based
            retention policy.
        subscription_id (None | Unset | UUID): Microsoft Azure ID assigned to a subscription to which the storage
            account belongs.
        tenant_id (None | str | Unset): Microsoft Azure ID assigned to a tenant to which the storage account belongs.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    sku_name: None | str | Unset = UNSET
    performance: StorageAccountPerformance | Unset = UNSET
    redundancy: StorageAccountRedundancy | Unset = UNSET
    access_tier: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    removed_from_azure: bool | Unset = UNSET
    supports_tiering: bool | Unset = UNSET
    is_immutable_storage: bool | Unset = UNSET
    is_immutable_storage_policy_locked: bool | Unset = UNSET
    subscription_id: None | Unset | UUID = UNSET
    tenant_id: None | str | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sku_name: None | str | Unset
        if isinstance(self.sku_name, Unset):
            sku_name = UNSET
        else:
            sku_name = self.sku_name

        performance: str | Unset = UNSET
        if not isinstance(self.performance, Unset):
            performance = self.performance.value

        redundancy: str | Unset = UNSET
        if not isinstance(self.redundancy, Unset):
            redundancy = self.redundancy.value

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

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        removed_from_azure = self.removed_from_azure

        supports_tiering = self.supports_tiering

        is_immutable_storage = self.is_immutable_storage

        is_immutable_storage_policy_locked = self.is_immutable_storage_policy_locked

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

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
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if name is not UNSET:
            field_dict["name"] = name
        if sku_name is not UNSET:
            field_dict["skuName"] = sku_name
        if performance is not UNSET:
            field_dict["performance"] = performance
        if redundancy is not UNSET:
            field_dict["redundancy"] = redundancy
        if access_tier is not UNSET:
            field_dict["accessTier"] = access_tier
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if removed_from_azure is not UNSET:
            field_dict["removedFromAzure"] = removed_from_azure
        if supports_tiering is not UNSET:
            field_dict["supportsTiering"] = supports_tiering
        if is_immutable_storage is not UNSET:
            field_dict["isImmutableStorage"] = is_immutable_storage
        if is_immutable_storage_policy_locked is not UNSET:
            field_dict["isImmutableStoragePolicyLocked"] = is_immutable_storage_policy_locked
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

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_sku_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku_name = _parse_sku_name(d.pop("skuName", UNSET))

        _performance = d.pop("performance", UNSET)
        performance: StorageAccountPerformance | Unset
        if isinstance(_performance, Unset):
            performance = UNSET
        else:
            performance = StorageAccountPerformance(_performance)

        _redundancy = d.pop("redundancy", UNSET)
        redundancy: StorageAccountRedundancy | Unset
        if isinstance(_redundancy, Unset):
            redundancy = UNSET
        else:
            redundancy = StorageAccountRedundancy(_redundancy)

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

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        removed_from_azure = d.pop("removedFromAzure", UNSET)

        supports_tiering = d.pop("supportsTiering", UNSET)

        is_immutable_storage = d.pop("isImmutableStorage", UNSET)

        is_immutable_storage_policy_locked = d.pop("isImmutableStoragePolicyLocked", UNSET)

        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

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

        storage_account = cls(
            id=id,
            resource_id=resource_id,
            name=name,
            sku_name=sku_name,
            performance=performance,
            redundancy=redundancy,
            access_tier=access_tier,
            region_id=region_id,
            region_name=region_name,
            resource_group_name=resource_group_name,
            removed_from_azure=removed_from_azure,
            supports_tiering=supports_tiering,
            is_immutable_storage=is_immutable_storage,
            is_immutable_storage_policy_locked=is_immutable_storage_policy_locked,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            field_links=field_links,
        )

        return storage_account
