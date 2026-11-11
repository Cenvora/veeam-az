from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_edit_validation_issue_type import AccountEditValidationIssueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountEditValidationIssue")


@_attrs_define
class AccountEditValidationIssue:
    """Information on an error occurred during the account edit data check.

    Attributes:
        type_ (AccountEditValidationIssueType): Type of the error occurred during the account edit data check.
        resources (list[str]): List of Azure resources to which the error occurred.
        subscription (str | Unset): Name or ID of an Azure subscription to which the error occurred.
        policy (str | Unset): Name or ID of a backup policy to which the error occurred.
    """

    type_: AccountEditValidationIssueType
    resources: list[str]
    subscription: str | Unset = UNSET
    policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        resources = self.resources

        subscription = self.subscription

        policy = self.policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "resources": resources,
            }
        )
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AccountEditValidationIssueType(d.pop("type"))

        resources = cast(list[str], d.pop("resources"))

        subscription = d.pop("subscription", UNSET)

        policy = d.pop("policy", UNSET)

        account_edit_validation_issue = cls(
            type_=type_,
            resources=resources,
            subscription=subscription,
            policy=policy,
        )

        account_edit_validation_issue.additional_properties = d
        return account_edit_validation_issue

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
