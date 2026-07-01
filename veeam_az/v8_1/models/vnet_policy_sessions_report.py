from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.job_session_type import JobSessionType
from ..models.job_status import JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="VnetPolicySessionsReport")


@_attrs_define
class VnetPolicySessionsReport:
    """
    Attributes:
        session_id (None | str | Unset):
        status (JobStatus | Unset): Specifies the status of the performed session.
        session_type (JobSessionType | Unset): Type of the session.
        localized_session_type (None | str | Unset):
        execution_start_time (datetime.datetime | None | Unset):
        execution_stop_time (datetime.datetime | None | Unset):
        execution_duration (None | str | Unset):
        changes (str | Unset):
    """

    session_id: None | str | Unset = UNSET
    status: JobStatus | Unset = UNSET
    session_type: JobSessionType | Unset = UNSET
    localized_session_type: None | str | Unset = UNSET
    execution_start_time: datetime.datetime | None | Unset = UNSET
    execution_stop_time: datetime.datetime | None | Unset = UNSET
    execution_duration: None | str | Unset = UNSET
    changes: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        session_type: str | Unset = UNSET
        if not isinstance(self.session_type, Unset):
            session_type = self.session_type.value

        localized_session_type: None | str | Unset
        if isinstance(self.localized_session_type, Unset):
            localized_session_type = UNSET
        else:
            localized_session_type = self.localized_session_type

        execution_start_time: None | str | Unset
        if isinstance(self.execution_start_time, Unset):
            execution_start_time = UNSET
        elif isinstance(self.execution_start_time, datetime.datetime):
            execution_start_time = self.execution_start_time.isoformat()
        else:
            execution_start_time = self.execution_start_time

        execution_stop_time: None | str | Unset
        if isinstance(self.execution_stop_time, Unset):
            execution_stop_time = UNSET
        elif isinstance(self.execution_stop_time, datetime.datetime):
            execution_stop_time = self.execution_stop_time.isoformat()
        else:
            execution_stop_time = self.execution_stop_time

        execution_duration: None | str | Unset
        if isinstance(self.execution_duration, Unset):
            execution_duration = UNSET
        else:
            execution_duration = self.execution_duration

        changes = self.changes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if status is not UNSET:
            field_dict["status"] = status
        if session_type is not UNSET:
            field_dict["sessionType"] = session_type
        if localized_session_type is not UNSET:
            field_dict["localizedSessionType"] = localized_session_type
        if execution_start_time is not UNSET:
            field_dict["executionStartTime"] = execution_start_time
        if execution_stop_time is not UNSET:
            field_dict["executionStopTime"] = execution_stop_time
        if execution_duration is not UNSET:
            field_dict["executionDuration"] = execution_duration
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("sessionId", UNSET))

        _status = d.pop("status", UNSET)
        status: JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        _session_type = d.pop("sessionType", UNSET)
        session_type: JobSessionType | Unset
        if isinstance(_session_type, Unset):
            session_type = UNSET
        else:
            session_type = JobSessionType(_session_type)

        def _parse_localized_session_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        localized_session_type = _parse_localized_session_type(d.pop("localizedSessionType", UNSET))

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

        def _parse_execution_stop_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_stop_time_type_0 = isoparse(data)

                return execution_stop_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        execution_stop_time = _parse_execution_stop_time(d.pop("executionStopTime", UNSET))

        def _parse_execution_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_duration = _parse_execution_duration(d.pop("executionDuration", UNSET))

        changes = d.pop("changes", UNSET)

        vnet_policy_sessions_report = cls(
            session_id=session_id,
            status=status,
            session_type=session_type,
            localized_session_type=localized_session_type,
            execution_start_time=execution_start_time,
            execution_stop_time=execution_stop_time,
            execution_duration=execution_duration,
            changes=changes,
        )

        return vnet_policy_sessions_report
