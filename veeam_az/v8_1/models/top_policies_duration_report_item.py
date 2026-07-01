from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.policy_type import PolicyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TopPoliciesDurationReportItem")


@_attrs_define
class TopPoliciesDurationReportItem:
    """
    Attributes:
        policy_id (UUID | Unset): System ID assigned to the policy in the Veeam Backup for Microsoft Azure REST API.
        policy_name (str | Unset): Name of the policy.
        policy_type (PolicyType | Unset): Workload type protected by a backup policy.
        duration (int | Unset): Duration of the most recent policy execution (in ms).
        avg_duration (int | Unset): Average duration of the policy execution (in ms).
        execution_start_time (datetime.datetime | None | Unset): Date and time when the policy execution started.
        job_session_type (str | Unset): Type of the policy session.
        avg_percentage (float | Unset): Difference between the average and the most recent duration of the policy
            execution (in percent).
        deviation_from_avg_duration (int | Unset): Difference between the average and the most recent duration of the
            policy execution (in ms).
    """

    policy_id: UUID | Unset = UNSET
    policy_name: str | Unset = UNSET
    policy_type: PolicyType | Unset = UNSET
    duration: int | Unset = UNSET
    avg_duration: int | Unset = UNSET
    execution_start_time: datetime.datetime | None | Unset = UNSET
    job_session_type: str | Unset = UNSET
    avg_percentage: float | Unset = UNSET
    deviation_from_avg_duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy_id: str | Unset = UNSET
        if not isinstance(self.policy_id, Unset):
            policy_id = str(self.policy_id)

        policy_name = self.policy_name

        policy_type: str | Unset = UNSET
        if not isinstance(self.policy_type, Unset):
            policy_type = self.policy_type.value

        duration = self.duration

        avg_duration = self.avg_duration

        execution_start_time: None | str | Unset
        if isinstance(self.execution_start_time, Unset):
            execution_start_time = UNSET
        elif isinstance(self.execution_start_time, datetime.datetime):
            execution_start_time = self.execution_start_time.isoformat()
        else:
            execution_start_time = self.execution_start_time

        job_session_type = self.job_session_type

        avg_percentage = self.avg_percentage

        deviation_from_avg_duration = self.deviation_from_avg_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if policy_type is not UNSET:
            field_dict["policyType"] = policy_type
        if duration is not UNSET:
            field_dict["duration"] = duration
        if avg_duration is not UNSET:
            field_dict["avgDuration"] = avg_duration
        if execution_start_time is not UNSET:
            field_dict["executionStartTime"] = execution_start_time
        if job_session_type is not UNSET:
            field_dict["jobSessionType"] = job_session_type
        if avg_percentage is not UNSET:
            field_dict["avgPercentage"] = avg_percentage
        if deviation_from_avg_duration is not UNSET:
            field_dict["deviationFromAvgDuration"] = deviation_from_avg_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _policy_id = d.pop("policyId", UNSET)
        policy_id: UUID | Unset
        if isinstance(_policy_id, Unset):
            policy_id = UNSET
        else:
            policy_id = UUID(_policy_id)

        policy_name = d.pop("policyName", UNSET)

        _policy_type = d.pop("policyType", UNSET)
        policy_type: PolicyType | Unset
        if isinstance(_policy_type, Unset):
            policy_type = UNSET
        else:
            policy_type = PolicyType(_policy_type)

        duration = d.pop("duration", UNSET)

        avg_duration = d.pop("avgDuration", UNSET)

        def _parse_execution_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_start_time_type_0 = isoparse(data)

                return execution_start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        execution_start_time = _parse_execution_start_time(d.pop("executionStartTime", UNSET))

        job_session_type = d.pop("jobSessionType", UNSET)

        avg_percentage = d.pop("avgPercentage", UNSET)

        deviation_from_avg_duration = d.pop("deviationFromAvgDuration", UNSET)

        top_policies_duration_report_item = cls(
            policy_id=policy_id,
            policy_name=policy_name,
            policy_type=policy_type,
            duration=duration,
            avg_duration=avg_duration,
            execution_start_time=execution_start_time,
            job_session_type=job_session_type,
            avg_percentage=avg_percentage,
            deviation_from_avg_duration=deviation_from_avg_duration,
        )

        top_policies_duration_report_item.additional_properties = d
        return top_policies_duration_report_item

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
