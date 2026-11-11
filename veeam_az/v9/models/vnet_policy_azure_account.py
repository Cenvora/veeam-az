from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VnetPolicyAzureAccount")


@_attrs_define
class VnetPolicyAzureAccount:
    """Information on a service account whose permissions are used to perform virtual network configuration backup.

    Attributes:
        account_id (UUID | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the service
            account.
        account_name (str | Unset): Name of the service account.
        tenant_id (UUID | Unset): Microsoft Azure ID assigned to a tenant with which the service account is associated.
        tenant_name (None | str | Unset): Name of the tenant with which the service account is associated.
    """

    account_id: UUID | Unset = UNSET
    account_name: str | Unset = UNSET
    tenant_id: UUID | Unset = UNSET
    tenant_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_id: str | Unset = UNSET
        if not isinstance(self.account_id, Unset):
            account_id = str(self.account_id)

        account_name = self.account_name

        tenant_id: str | Unset = UNSET
        if not isinstance(self.tenant_id, Unset):
            tenant_id = str(self.tenant_id)

        tenant_name: None | str | Unset
        if isinstance(self.tenant_name, Unset):
            tenant_name = UNSET
        else:
            tenant_name = self.tenant_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if tenant_name is not UNSET:
            field_dict["tenantName"] = tenant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _account_id = d.pop("accountId", UNSET)
        account_id: UUID | Unset
        if isinstance(_account_id, Unset):
            account_id = UNSET
        else:
            account_id = UUID(_account_id)

        account_name = d.pop("accountName", UNSET)

        _tenant_id = d.pop("tenantId", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)

        def _parse_tenant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_name = _parse_tenant_name(d.pop("tenantName", UNSET))

        vnet_policy_azure_account = cls(
            account_id=account_id,
            account_name=account_name,
            tenant_id=tenant_id,
            tenant_name=tenant_name,
        )

        return vnet_policy_azure_account
