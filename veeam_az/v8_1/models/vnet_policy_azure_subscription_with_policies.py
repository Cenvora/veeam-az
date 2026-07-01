from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_subscription import AzureSubscription


T = TypeVar("T", bound="VnetPolicyAzureSubscriptionWithPolicies")


@_attrs_define
class VnetPolicyAzureSubscriptionWithPolicies:
    """
    Attributes:
        subscription (AzureSubscription | Unset): Specifies information on an Azure subscription.
        policy_names (list[str] | Unset): List of Azure VM, Azure SQL and Azure file share backup policies in which the
            subscription is specified.
    """

    subscription: AzureSubscription | Unset = UNSET
    policy_names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        policy_names: list[str] | Unset = UNSET
        if not isinstance(self.policy_names, Unset):
            policy_names = self.policy_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if policy_names is not UNSET:
            field_dict["policyNames"] = policy_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_subscription import AzureSubscription

        d = dict(src_dict)
        _subscription = d.pop("subscription", UNSET)
        subscription: AzureSubscription | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = AzureSubscription.from_dict(_subscription)

        policy_names = cast(list[str], d.pop("policyNames", UNSET))

        vnet_policy_azure_subscription_with_policies = cls(
            subscription=subscription,
            policy_names=policy_names,
        )

        vnet_policy_azure_subscription_with_policies.additional_properties = d
        return vnet_policy_azure_subscription_with_policies

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
