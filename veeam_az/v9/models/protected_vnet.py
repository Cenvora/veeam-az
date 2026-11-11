from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.vnet_policy_azure_account import VnetPolicyAzureAccount


T = TypeVar("T", bound="ProtectedVnet")


@_attrs_define
class ProtectedVnet:
    """
    Attributes:
        id (UUID | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to a protected virtual
            network.
        subscription_id (UUID | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to an Azure
            subscription with which the protected virtual network is associated.
        subscription_name (str | Unset): Name of the Azure subscription with which the protected virtual network is
            associated.
        last_backup (datetime.datetime | Unset): Date and time of the most recent backup of the protected virtual
            network.
        last_changes (str | Unset): List containing data on the virtual network configuration items that were recently
            added to the backup scope or deleted from it.
        azure_account (VnetPolicyAzureAccount | Unset): Information on a service account whose permissions are used to
            perform virtual network configuration backup.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    subscription_name: str | Unset = UNSET
    last_backup: datetime.datetime | Unset = UNSET
    last_changes: str | Unset = UNSET
    azure_account: VnetPolicyAzureAccount | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        subscription_name = self.subscription_name

        last_backup: str | Unset = UNSET
        if not isinstance(self.last_backup, Unset):
            last_backup = self.last_backup.isoformat()

        last_changes = self.last_changes

        azure_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_account, Unset):
            azure_account = self.azure_account.to_dict()

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup
        if last_changes is not UNSET:
            field_dict["lastChanges"] = last_changes
        if azure_account is not UNSET:
            field_dict["azureAccount"] = azure_account
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.vnet_policy_azure_account import VnetPolicyAzureAccount

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        subscription_name = d.pop("subscriptionName", UNSET)

        _last_backup = d.pop("lastBackup", UNSET)
        last_backup: datetime.datetime | Unset
        if isinstance(_last_backup, Unset):
            last_backup = UNSET
        else:
            last_backup = isoparse(_last_backup)

        last_changes = d.pop("lastChanges", UNSET)

        _azure_account = d.pop("azureAccount", UNSET)
        azure_account: VnetPolicyAzureAccount | Unset
        if isinstance(_azure_account, Unset):
            azure_account = UNSET
        else:
            azure_account = VnetPolicyAzureAccount.from_dict(_azure_account)

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

        protected_vnet = cls(
            id=id,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            last_backup=last_backup,
            last_changes=last_changes,
            azure_account=azure_account,
            field_links=field_links,
        )

        protected_vnet.additional_properties = d
        return protected_vnet

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
