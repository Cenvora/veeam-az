from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.azure_account_purpose import AzureAccountPurpose
from ..types import UNSET, Unset

T = TypeVar("T", bound="MissingSubscriptionPurpose")


@_attrs_define
class MissingSubscriptionPurpose:
    """Information on each operation that cannot be performed due to missing service account permissions.

    Attributes:
        purpose (AzureAccountPurpose | Unset): Operations that can be performed using the service account.
        missing_actions (list[str] | Unset): List of missing service account permissions due to which the operation
            cannot be performed.
        missing_data_actions (list[str] | Unset): List of missing service account data actions due to which the
            operation cannot be performed.
    """

    purpose: AzureAccountPurpose | Unset = UNSET
    missing_actions: list[str] | Unset = UNSET
    missing_data_actions: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value

        missing_actions: list[str] | Unset = UNSET
        if not isinstance(self.missing_actions, Unset):
            missing_actions = self.missing_actions

        missing_data_actions: list[str] | Unset = UNSET
        if not isinstance(self.missing_data_actions, Unset):
            missing_data_actions = self.missing_data_actions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if missing_actions is not UNSET:
            field_dict["missingActions"] = missing_actions
        if missing_data_actions is not UNSET:
            field_dict["missingDataActions"] = missing_data_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _purpose = d.pop("purpose", UNSET)
        purpose: AzureAccountPurpose | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = AzureAccountPurpose(_purpose)

        missing_actions = cast(list[str], d.pop("missingActions", UNSET))

        missing_data_actions = cast(list[str], d.pop("missingDataActions", UNSET))

        missing_subscription_purpose = cls(
            purpose=purpose,
            missing_actions=missing_actions,
            missing_data_actions=missing_data_actions,
        )

        return missing_subscription_purpose
