from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicySubscriptionFromClient")


@_attrs_define
class PolicySubscriptionFromClient:
    """
    Attributes:
        subscription_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a subscription where the
            protected resources belong.
    """

    subscription_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = self.subscription_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_subscription_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        policy_subscription_from_client = cls(
            subscription_id=subscription_id,
        )

        return policy_subscription_from_client
