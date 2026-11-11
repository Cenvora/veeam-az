from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SnapshotDestination")


@_attrs_define
class SnapshotDestination:
    """Specifies the target location settings for cloud-native snapshots.

    Attributes:
        subscription_id (UUID): Specifies the Microsoft Azure ID assigned to a subscription to which the backed-up VMs
            belong.
        resource_group_id (str): Specifies the Microsoft Azure ID assigned to a resource group in which snapshots of the
            backed-up VMs will be stored.
    """

    subscription_id: UUID
    resource_group_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id = str(self.subscription_id)

        resource_group_id = self.resource_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionId": subscription_id,
                "resourceGroupId": resource_group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscription_id = UUID(d.pop("subscriptionId"))

        resource_group_id = d.pop("resourceGroupId")

        snapshot_destination = cls(
            subscription_id=subscription_id,
            resource_group_id=resource_group_id,
        )

        snapshot_destination.additional_properties = d
        return snapshot_destination

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
