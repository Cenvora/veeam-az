from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_subscription import AzureSubscription
    from ..models.vnet_policy_azure_account import VnetPolicyAzureAccount


T = TypeVar("T", bound="VnetPolicyAdditionalProtectedResources")


@_attrs_define
class VnetPolicyAdditionalProtectedResources:
    """Information on a service account whose permissions are used to perform virtual network configuration backup, and on
    the subscriptions manually added to the virtual network configuration backup policy.

        Attributes:
            azure_account (VnetPolicyAzureAccount | Unset): Information on a service account whose permissions are used to
                perform virtual network configuration backup.
            subscriptions (list[AzureSubscription] | Unset): Information on each subscription manually added to the virtual
                network configuration backup policy.
    """

    azure_account: VnetPolicyAzureAccount | Unset = UNSET
    subscriptions: list[AzureSubscription] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        azure_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_account, Unset):
            azure_account = self.azure_account.to_dict()

        subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if azure_account is not UNSET:
            field_dict["azureAccount"] = azure_account
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_subscription import AzureSubscription
        from ..models.vnet_policy_azure_account import VnetPolicyAzureAccount

        d = dict(src_dict)
        _azure_account = d.pop("azureAccount", UNSET)
        azure_account: VnetPolicyAzureAccount | Unset
        if isinstance(_azure_account, Unset):
            azure_account = UNSET
        else:
            azure_account = VnetPolicyAzureAccount.from_dict(_azure_account)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[AzureSubscription] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = AzureSubscription.from_dict(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        vnet_policy_additional_protected_resources = cls(
            azure_account=azure_account,
            subscriptions=subscriptions,
        )

        vnet_policy_additional_protected_resources.additional_properties = d
        return vnet_policy_additional_protected_resources

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
