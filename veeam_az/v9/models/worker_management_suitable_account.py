from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.worker_management_suitable_account_subscription import WorkerManagementSuitableAccountSubscription


T = TypeVar("T", bound="WorkerManagementSuitableAccount")


@_attrs_define
class WorkerManagementSuitableAccount:
    """Information on a service account that can be used for worker management.

    Attributes:
        azure_account_id (UUID): System ID assigned to the service account in the Veeam Backup for Microsoft Azure REST
            API.
        tenant_id (UUID): Microsoft Azure ID assigned to a tenant with which the service account is associated.
        subscriptions (list[WorkerManagementSuitableAccountSubscription]): List of subscriptions managed by
            azureAccount, suitable for worker management purpose.
        azure_account_name (str | Unset): Name of the service account.
        tenant_name (None | str | Unset): Name of the tenant with which the service account is associated.
    """

    azure_account_id: UUID
    tenant_id: UUID
    subscriptions: list[WorkerManagementSuitableAccountSubscription]
    azure_account_name: str | Unset = UNSET
    tenant_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        azure_account_id = str(self.azure_account_id)

        tenant_id = str(self.tenant_id)

        subscriptions = []
        for subscriptions_item_data in self.subscriptions:
            subscriptions_item = subscriptions_item_data.to_dict()
            subscriptions.append(subscriptions_item)

        azure_account_name = self.azure_account_name

        tenant_name: None | str | Unset
        if isinstance(self.tenant_name, Unset):
            tenant_name = UNSET
        else:
            tenant_name = self.tenant_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "azureAccountId": azure_account_id,
                "tenantId": tenant_id,
                "subscriptions": subscriptions,
            }
        )
        if azure_account_name is not UNSET:
            field_dict["azureAccountName"] = azure_account_name
        if tenant_name is not UNSET:
            field_dict["tenantName"] = tenant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worker_management_suitable_account_subscription import WorkerManagementSuitableAccountSubscription

        d = dict(src_dict)
        azure_account_id = UUID(d.pop("azureAccountId"))

        tenant_id = UUID(d.pop("tenantId"))

        subscriptions = []
        _subscriptions = d.pop("subscriptions")
        for subscriptions_item_data in _subscriptions:
            subscriptions_item = WorkerManagementSuitableAccountSubscription.from_dict(subscriptions_item_data)

            subscriptions.append(subscriptions_item)

        azure_account_name = d.pop("azureAccountName", UNSET)

        def _parse_tenant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_name = _parse_tenant_name(d.pop("tenantName", UNSET))

        worker_management_suitable_account = cls(
            azure_account_id=azure_account_id,
            tenant_id=tenant_id,
            subscriptions=subscriptions,
            azure_account_name=azure_account_name,
            tenant_name=tenant_name,
        )

        worker_management_suitable_account.additional_properties = d
        return worker_management_suitable_account

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
