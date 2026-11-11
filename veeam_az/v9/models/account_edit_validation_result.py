from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_result_severity import CheckResultSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_edit_validation_issue import AccountEditValidationIssue


T = TypeVar("T", bound="AccountEditValidationResult")


@_attrs_define
class AccountEditValidationResult:
    """Result of the account edit data check.

    Attributes:
        result (CheckResultSeverity): Specifies the state of the configuration check operation.
        issues (list[AccountEditValidationIssue] | Unset): List of errors occurred during the account edit data check.
    """

    result: CheckResultSeverity
    issues: list[AccountEditValidationIssue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = self.result.value

        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
            }
        )
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_edit_validation_issue import AccountEditValidationIssue

        d = dict(src_dict)
        result = CheckResultSeverity(d.pop("result"))

        _issues = d.pop("issues", UNSET)
        issues: list[AccountEditValidationIssue] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = AccountEditValidationIssue.from_dict(issues_item_data)

                issues.append(issues_item)

        account_edit_validation_result = cls(
            result=result,
            issues=issues,
        )

        account_edit_validation_result.additional_properties = d
        return account_edit_validation_result

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
