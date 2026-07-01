from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.check_result_severity import CheckResultSeverity
from ..models.container_immutability_issue_reason import ContainerImmutabilityIssueReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerImmutabilityIssue")


@_attrs_define
class ContainerImmutabilityIssue:
    """
    Attributes:
        reason (ContainerImmutabilityIssueReason | Unset):
        message (None | str | Unset):
        severity (CheckResultSeverity | Unset): Specifies the state of the configuration check operation.
    """

    reason: ContainerImmutabilityIssueReason | Unset = UNSET
    message: None | str | Unset = UNSET
    severity: CheckResultSeverity | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _reason = d.pop("reason", UNSET)
        reason: ContainerImmutabilityIssueReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ContainerImmutabilityIssueReason(_reason)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        _severity = d.pop("severity", UNSET)
        severity: CheckResultSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = CheckResultSeverity(_severity)

        container_immutability_issue = cls(
            reason=reason,
            message=message,
            severity=severity,
        )

        return container_immutability_issue
