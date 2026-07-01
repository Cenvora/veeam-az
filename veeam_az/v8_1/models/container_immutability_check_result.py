from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.container_immutability_issue import ContainerImmutabilityIssue


T = TypeVar("T", bound="ContainerImmutabilityCheckResult")


@_attrs_define
class ContainerImmutabilityCheckResult:
    """
    Attributes:
        issues (list[ContainerImmutabilityIssue] | None | Unset):
    """

    issues: list[ContainerImmutabilityIssue] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        issues: list[dict[str, Any]] | None | Unset
        if isinstance(self.issues, Unset):
            issues = UNSET
        elif isinstance(self.issues, list):
            issues = []
            for issues_type_0_item_data in self.issues:
                issues_type_0_item = issues_type_0_item_data.to_dict()
                issues.append(issues_type_0_item)

        else:
            issues = self.issues

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.container_immutability_issue import ContainerImmutabilityIssue

        d = dict(src_dict)

        def _parse_issues(data: object) -> list[ContainerImmutabilityIssue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                issues_type_0 = []
                _issues_type_0 = data
                for issues_type_0_item_data in _issues_type_0:
                    issues_type_0_item = ContainerImmutabilityIssue.from_dict(issues_type_0_item_data)

                    issues_type_0.append(issues_type_0_item)

                return issues_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContainerImmutabilityIssue] | None | Unset, data)

        issues = _parse_issues(d.pop("issues", UNSET))

        container_immutability_check_result = cls(
            issues=issues,
        )

        return container_immutability_check_result
