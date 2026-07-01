from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.azure_account_check_result_status import AzureAccountCheckResultStatus
from ..models.check_result_severity import CheckResultSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_account import AzureAccount
    from ..models.azure_account_subscription_check_result import AzureAccountSubscriptionCheckResult


T = TypeVar("T", bound="AzureAccountCheckResult")


@_attrs_define
class AzureAccountCheckResult:
    """Results of the configuration check of service accounts.

    Attributes:
        account (AzureAccount | Unset): Information on a service account.
        subscriptions (list[AzureAccountSubscriptionCheckResult] | Unset): Information on the subscriptions with which
            the service account is associated.
        status (AzureAccountCheckResultStatus | Unset): Status of the service account configuration check.
        severity (CheckResultSeverity | Unset): Specifies the state of the configuration check operation.
    """

    account: AzureAccount | Unset = UNSET
    subscriptions: list[AzureAccountSubscriptionCheckResult] | Unset = UNSET
    status: AzureAccountCheckResultStatus | Unset = UNSET
    severity: CheckResultSeverity | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if status is not UNSET:
            field_dict["status"] = status
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_account import AzureAccount
        from ..models.azure_account_subscription_check_result import AzureAccountSubscriptionCheckResult

        d = dict(src_dict)
        _account = d.pop("account", UNSET)
        account: AzureAccount | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = AzureAccount.from_dict(_account)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[AzureAccountSubscriptionCheckResult] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = AzureAccountSubscriptionCheckResult.from_dict(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        _status = d.pop("status", UNSET)
        status: AzureAccountCheckResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AzureAccountCheckResultStatus(_status)

        _severity = d.pop("severity", UNSET)
        severity: CheckResultSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = CheckResultSeverity(_severity)

        azure_account_check_result = cls(
            account=account,
            subscriptions=subscriptions,
            status=status,
            severity=severity,
        )

        return azure_account_check_result
