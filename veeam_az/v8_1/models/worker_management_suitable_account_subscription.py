from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerManagementSuitableAccountSubscription")


@_attrs_define
class WorkerManagementSuitableAccountSubscription:
    """
    Attributes:
        subscription_id (UUID): Microsoft Azure ID assigned to a subscription with which the service account is
            associated.
        subscription_name (str | Unset): Name of the Azure subscription with which the service account is associated.
    """

    subscription_id: UUID
    subscription_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id = str(self.subscription_id)

        subscription_name = self.subscription_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionId": subscription_id,
            }
        )
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscription_id = UUID(d.pop("subscriptionId"))

        subscription_name = d.pop("subscriptionName", UNSET)

        worker_management_suitable_account_subscription = cls(
            subscription_id=subscription_id,
            subscription_name=subscription_name,
        )

        worker_management_suitable_account_subscription.additional_properties = d
        return worker_management_suitable_account_subscription

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
