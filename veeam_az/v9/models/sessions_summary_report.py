from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.summary_count_difference import SummaryCountDifference
from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionsSummaryReport")


@_attrs_define
class SessionsSummaryReport:
    """
    Attributes:
        latest_sessions_error_count (int | Unset): Total number of sessions completed with errors for the past 24 hours.
        latest_sessions_error_count_difference (SummaryCountDifference | Unset): Difference between the previous and the
            current result.
        latest_sessions_warning_count (int | Unset): Total number of sessions completed with warnings for the past 24
            hours.
        latest_sessions_warning_count_difference (SummaryCountDifference | Unset): Difference between the previous and
            the current result.
        latest_sessions_success_count (int | Unset): Total number of sessions completed successfully during the past 24
            hours.
        latest_sessions_success_count_difference (SummaryCountDifference | Unset): Difference between the previous and
            the current result.
        latest_sessions_running_count (int | Unset): Total number of sessions completed for the past 24 hours.
    """

    latest_sessions_error_count: int | Unset = UNSET
    latest_sessions_error_count_difference: SummaryCountDifference | Unset = UNSET
    latest_sessions_warning_count: int | Unset = UNSET
    latest_sessions_warning_count_difference: SummaryCountDifference | Unset = UNSET
    latest_sessions_success_count: int | Unset = UNSET
    latest_sessions_success_count_difference: SummaryCountDifference | Unset = UNSET
    latest_sessions_running_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_sessions_error_count = self.latest_sessions_error_count

        latest_sessions_error_count_difference: str | Unset = UNSET
        if not isinstance(self.latest_sessions_error_count_difference, Unset):
            latest_sessions_error_count_difference = self.latest_sessions_error_count_difference.value

        latest_sessions_warning_count = self.latest_sessions_warning_count

        latest_sessions_warning_count_difference: str | Unset = UNSET
        if not isinstance(self.latest_sessions_warning_count_difference, Unset):
            latest_sessions_warning_count_difference = self.latest_sessions_warning_count_difference.value

        latest_sessions_success_count = self.latest_sessions_success_count

        latest_sessions_success_count_difference: str | Unset = UNSET
        if not isinstance(self.latest_sessions_success_count_difference, Unset):
            latest_sessions_success_count_difference = self.latest_sessions_success_count_difference.value

        latest_sessions_running_count = self.latest_sessions_running_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_sessions_error_count is not UNSET:
            field_dict["latestSessionsErrorCount"] = latest_sessions_error_count
        if latest_sessions_error_count_difference is not UNSET:
            field_dict["latestSessionsErrorCountDifference"] = latest_sessions_error_count_difference
        if latest_sessions_warning_count is not UNSET:
            field_dict["latestSessionsWarningCount"] = latest_sessions_warning_count
        if latest_sessions_warning_count_difference is not UNSET:
            field_dict["latestSessionsWarningCountDifference"] = latest_sessions_warning_count_difference
        if latest_sessions_success_count is not UNSET:
            field_dict["latestSessionsSuccessCount"] = latest_sessions_success_count
        if latest_sessions_success_count_difference is not UNSET:
            field_dict["latestSessionsSuccessCountDifference"] = latest_sessions_success_count_difference
        if latest_sessions_running_count is not UNSET:
            field_dict["latestSessionsRunningCount"] = latest_sessions_running_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latest_sessions_error_count = d.pop("latestSessionsErrorCount", UNSET)

        _latest_sessions_error_count_difference = d.pop("latestSessionsErrorCountDifference", UNSET)
        latest_sessions_error_count_difference: SummaryCountDifference | Unset
        if isinstance(_latest_sessions_error_count_difference, Unset):
            latest_sessions_error_count_difference = UNSET
        else:
            latest_sessions_error_count_difference = SummaryCountDifference(_latest_sessions_error_count_difference)

        latest_sessions_warning_count = d.pop("latestSessionsWarningCount", UNSET)

        _latest_sessions_warning_count_difference = d.pop("latestSessionsWarningCountDifference", UNSET)
        latest_sessions_warning_count_difference: SummaryCountDifference | Unset
        if isinstance(_latest_sessions_warning_count_difference, Unset):
            latest_sessions_warning_count_difference = UNSET
        else:
            latest_sessions_warning_count_difference = SummaryCountDifference(_latest_sessions_warning_count_difference)

        latest_sessions_success_count = d.pop("latestSessionsSuccessCount", UNSET)

        _latest_sessions_success_count_difference = d.pop("latestSessionsSuccessCountDifference", UNSET)
        latest_sessions_success_count_difference: SummaryCountDifference | Unset
        if isinstance(_latest_sessions_success_count_difference, Unset):
            latest_sessions_success_count_difference = UNSET
        else:
            latest_sessions_success_count_difference = SummaryCountDifference(_latest_sessions_success_count_difference)

        latest_sessions_running_count = d.pop("latestSessionsRunningCount", UNSET)

        sessions_summary_report = cls(
            latest_sessions_error_count=latest_sessions_error_count,
            latest_sessions_error_count_difference=latest_sessions_error_count_difference,
            latest_sessions_warning_count=latest_sessions_warning_count,
            latest_sessions_warning_count_difference=latest_sessions_warning_count_difference,
            latest_sessions_success_count=latest_sessions_success_count,
            latest_sessions_success_count_difference=latest_sessions_success_count_difference,
            latest_sessions_running_count=latest_sessions_running_count,
        )

        sessions_summary_report.additional_properties = d
        return sessions_summary_report

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
