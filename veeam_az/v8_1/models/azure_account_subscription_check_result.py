from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_for_service_account import SubscriptionForServiceAccount


T = TypeVar("T", bound="AzureAccountSubscriptionCheckResult")


@_attrs_define
class AzureAccountSubscriptionCheckResult:
    """Information on each subscription.

    Attributes:
        subscription (SubscriptionForServiceAccount | Unset): Information on each subscription.
        role_definition (str | Unset): List of Azure roles available for the account.
        existing_role (None | str | Unset): Role assigned to the Entra ID application with which the service account is
            associated.
    """

    subscription: SubscriptionForServiceAccount | Unset = UNSET
    role_definition: str | Unset = UNSET
    existing_role: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        role_definition = self.role_definition

        existing_role: None | str | Unset
        if isinstance(self.existing_role, Unset):
            existing_role = UNSET
        else:
            existing_role = self.existing_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if role_definition is not UNSET:
            field_dict["roleDefinition"] = role_definition
        if existing_role is not UNSET:
            field_dict["existingRole"] = existing_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_for_service_account import SubscriptionForServiceAccount

        d = dict(src_dict)
        _subscription = d.pop("subscription", UNSET)
        subscription: SubscriptionForServiceAccount | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = SubscriptionForServiceAccount.from_dict(_subscription)

        role_definition = d.pop("roleDefinition", UNSET)

        def _parse_existing_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        existing_role = _parse_existing_role(d.pop("existingRole", UNSET))

        azure_account_subscription_check_result = cls(
            subscription=subscription,
            role_definition=role_definition,
            existing_role=existing_role,
        )

        azure_account_subscription_check_result.additional_properties = d
        return azure_account_subscription_check_result

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
