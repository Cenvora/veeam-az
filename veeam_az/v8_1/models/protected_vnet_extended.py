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
    from ..models.vnet_policy_azure_account import VnetPolicyAzureAccount


T = TypeVar("T", bound="ProtectedVnetExtended")


@_attrs_define
class ProtectedVnetExtended:
    """
    Attributes:
        id (UUID | Unset):
        tenant_id (None | Unset | UUID):
        tenant_name (None | str | Unset):
        subscription_id (UUID | Unset):
        subscription_name (str | Unset):
        region_count (int | Unset):
        last_backup (datetime.datetime | Unset):
        last_changes (str | Unset):
        restore_point_count (int | Unset):
        repository_names (list[str] | None | Unset):
        azure_account (VnetPolicyAzureAccount | Unset): Information on a service account whose permissions are used to
            perform virtual network configuration backup.
    """

    id: UUID | Unset = UNSET
    tenant_id: None | Unset | UUID = UNSET
    tenant_name: None | str | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    subscription_name: str | Unset = UNSET
    region_count: int | Unset = UNSET
    last_backup: datetime.datetime | Unset = UNSET
    last_changes: str | Unset = UNSET
    restore_point_count: int | Unset = UNSET
    repository_names: list[str] | None | Unset = UNSET
    azure_account: VnetPolicyAzureAccount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        elif isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        tenant_name: None | str | Unset
        if isinstance(self.tenant_name, Unset):
            tenant_name = UNSET
        else:
            tenant_name = self.tenant_name

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        subscription_name = self.subscription_name

        region_count = self.region_count

        last_backup: str | Unset = UNSET
        if not isinstance(self.last_backup, Unset):
            last_backup = self.last_backup.isoformat()

        last_changes = self.last_changes

        restore_point_count = self.restore_point_count

        repository_names: list[str] | None | Unset
        if isinstance(self.repository_names, Unset):
            repository_names = UNSET
        elif isinstance(self.repository_names, list):
            repository_names = self.repository_names

        else:
            repository_names = self.repository_names

        azure_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_account, Unset):
            azure_account = self.azure_account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if tenant_name is not UNSET:
            field_dict["tenantName"] = tenant_name
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if region_count is not UNSET:
            field_dict["regionCount"] = region_count
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup
        if last_changes is not UNSET:
            field_dict["lastChanges"] = last_changes
        if restore_point_count is not UNSET:
            field_dict["restorePointCount"] = restore_point_count
        if repository_names is not UNSET:
            field_dict["repositoryNames"] = repository_names
        if azure_account is not UNSET:
            field_dict["azureAccount"] = azure_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vnet_policy_azure_account import VnetPolicyAzureAccount

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_tenant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_tenant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_name = _parse_tenant_name(d.pop("tenantName", UNSET))

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        subscription_name = d.pop("subscriptionName", UNSET)

        region_count = d.pop("regionCount", UNSET)

        _last_backup = d.pop("lastBackup", UNSET)
        last_backup: datetime.datetime | Unset
        if isinstance(_last_backup, Unset):
            last_backup = UNSET
        else:
            last_backup = isoparse(_last_backup)

        last_changes = d.pop("lastChanges", UNSET)

        restore_point_count = d.pop("restorePointCount", UNSET)

        def _parse_repository_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repository_names_type_0 = cast(list[str], data)

                return repository_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        repository_names = _parse_repository_names(d.pop("repositoryNames", UNSET))

        _azure_account = d.pop("azureAccount", UNSET)
        azure_account: VnetPolicyAzureAccount | Unset
        if isinstance(_azure_account, Unset):
            azure_account = UNSET
        else:
            azure_account = VnetPolicyAzureAccount.from_dict(_azure_account)

        protected_vnet_extended = cls(
            id=id,
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            region_count=region_count,
            last_backup=last_backup,
            last_changes=last_changes,
            restore_point_count=restore_point_count,
            repository_names=repository_names,
            azure_account=azure_account,
        )

        protected_vnet_extended.additional_properties = d
        return protected_vnet_extended

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
