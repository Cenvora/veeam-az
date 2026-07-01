from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyProtectedItem")


@_attrs_define
class PolicyProtectedItem:
    """Information on each protected resource.

    Attributes:
        resource_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure to a protected
            Azure resource.
        policy_id (UUID | Unset): System ID assigned in the Veeam Backup for Microsoft Azure to a backup policy.
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to a subscription to which the file share belongs.
    """

    resource_id: None | str | Unset = UNSET
    policy_id: UUID | Unset = UNSET
    subscription_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        policy_id: str | Unset = UNSET
        if not isinstance(self.policy_id, Unset):
            policy_id = str(self.policy_id)

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        _policy_id = d.pop("policyId", UNSET)
        policy_id: UUID | Unset
        if isinstance(_policy_id, Unset):
            policy_id = UNSET
        else:
            policy_id = UUID(_policy_id)

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        policy_protected_item = cls(
            resource_id=resource_id,
            policy_id=policy_id,
            subscription_id=subscription_id,
        )

        return policy_protected_item
