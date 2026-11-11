from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaSessionTaskReportRow")


@_attrs_define
class SlaSessionTaskReportRow:
    """
    Attributes:
        session_task_id (UUID | Unset): System ID assigned to a session task in the Veeam Backup for Microsoft Azure
            REST API.
        session_task_name (str | Unset): Name of the session task.
        status (JobStatus | Unset): Specifies the status of the performed session.
        local_start_time (datetime.datetime | None | Unset): Date and time (in the time zone of the Azure region in
            which the protected VM resides) when the task started.
        start_time (datetime.datetime | None | Unset): Date and time (in UTC) when the task started.
    """

    session_task_id: UUID | Unset = UNSET
    session_task_name: str | Unset = UNSET
    status: JobStatus | Unset = UNSET
    local_start_time: datetime.datetime | None | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_task_id: str | Unset = UNSET
        if not isinstance(self.session_task_id, Unset):
            session_task_id = str(self.session_task_id)

        session_task_name = self.session_task_name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        local_start_time: None | str | Unset
        if isinstance(self.local_start_time, Unset):
            local_start_time = UNSET
        elif isinstance(self.local_start_time, datetime.datetime):
            local_start_time = self.local_start_time.isoformat()
        else:
            local_start_time = self.local_start_time

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_task_id is not UNSET:
            field_dict["sessionTaskId"] = session_task_id
        if session_task_name is not UNSET:
            field_dict["sessionTaskName"] = session_task_name
        if status is not UNSET:
            field_dict["status"] = status
        if local_start_time is not UNSET:
            field_dict["localStartTime"] = local_start_time
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _session_task_id = d.pop("sessionTaskId", UNSET)
        session_task_id: UUID | Unset
        if isinstance(_session_task_id, Unset):
            session_task_id = UNSET
        else:
            session_task_id = UUID(_session_task_id)

        session_task_name = d.pop("sessionTaskName", UNSET)

        _status = d.pop("status", UNSET)
        status: JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        def _parse_local_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                local_start_time_type_0 = isoparse(data)

                return local_start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        local_start_time = _parse_local_start_time(d.pop("localStartTime", UNSET))

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        sla_session_task_report_row = cls(
            session_task_id=session_task_id,
            session_task_name=session_task_name,
            status=status,
            local_start_time=local_start_time,
            start_time=start_time,
        )

        sla_session_task_report_row.additional_properties = d
        return sla_session_task_report_row

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
