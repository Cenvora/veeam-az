from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.azure_environment import AzureEnvironment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_subscription import AzureSubscription
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.protected_file_share_storage_account import ProtectedFileShareStorageAccount
    from ..models.protection_file_share_state import ProtectionFileShareState
    from ..models.region import Region
    from ..models.resource_group import ResourceGroup


T = TypeVar("T", bound="ProtectedFileShareExtended")


@_attrs_define
class ProtectedFileShareExtended:
    """
    Attributes:
        id (None | str | Unset):
        azure_id (None | str | Unset):
        name (None | str | Unset):
        storage_account (ProtectedFileShareStorageAccount | Unset): Information on the storage account where the file
            share resides.
        azure_environment (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        region_name (None | str | Unset):
        size_in_mb (int | Unset):
        subscription_id (UUID | Unset):
        last_backup (datetime.datetime | Unset):
        subscription (AzureSubscription | Unset): Specifies information on an Azure subscription.
        region (Region | Unset): Specifies Azure regions for which the operation is performed.
        resource_group (ResourceGroup | Unset): Specifies information on a resource group.
        policy_name (None | str | Unset):
        protection_state (ProtectionFileShareState | Unset):
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    azure_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    storage_account: ProtectedFileShareStorageAccount | Unset = UNSET
    azure_environment: AzureEnvironment | Unset = UNSET
    region_name: None | str | Unset = UNSET
    size_in_mb: int | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    last_backup: datetime.datetime | Unset = UNSET
    subscription: AzureSubscription | Unset = UNSET
    region: Region | Unset = UNSET
    resource_group: ResourceGroup | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    protection_state: ProtectionFileShareState | Unset = UNSET
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

        storage_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_account, Unset):
            storage_account = self.storage_account.to_dict()

        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        size_in_mb = self.size_in_mb

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

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

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        protection_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protection_state, Unset):
            protection_state = self.protection_state.to_dict()

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
        if storage_account is not UNSET:
            field_dict["storageAccount"] = storage_account
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if size_in_mb is not UNSET:
            field_dict["sizeInMb"] = size_in_mb
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if region is not UNSET:
            field_dict["region"] = region
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if protection_state is not UNSET:
            field_dict["protectionState"] = protection_state
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_subscription import AzureSubscription
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.protected_file_share_storage_account import ProtectedFileShareStorageAccount
        from ..models.protection_file_share_state import ProtectionFileShareState
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

        _storage_account = d.pop("storageAccount", UNSET)
        storage_account: ProtectedFileShareStorageAccount | Unset
        if isinstance(_storage_account, Unset):
            storage_account = UNSET
        else:
            storage_account = ProtectedFileShareStorageAccount.from_dict(_storage_account)

        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureEnvironment | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureEnvironment(_azure_environment)

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        size_in_mb = d.pop("sizeInMb", UNSET)

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

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

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        _protection_state = d.pop("protectionState", UNSET)
        protection_state: ProtectionFileShareState | Unset
        if isinstance(_protection_state, Unset):
            protection_state = UNSET
        else:
            protection_state = ProtectionFileShareState.from_dict(_protection_state)

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

        protected_file_share_extended = cls(
            id=id,
            azure_id=azure_id,
            name=name,
            storage_account=storage_account,
            azure_environment=azure_environment,
            region_name=region_name,
            size_in_mb=size_in_mb,
            subscription_id=subscription_id,
            last_backup=last_backup,
            subscription=subscription,
            region=region,
            resource_group=resource_group,
            policy_name=policy_name,
            protection_state=protection_state,
            field_links=field_links,
        )

        return protected_file_share_extended
