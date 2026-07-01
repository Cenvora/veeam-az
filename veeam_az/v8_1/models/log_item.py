from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LogItem")


@_attrs_define
class LogItem:
    """
    Attributes:
        log_time (datetime.datetime | Unset): Date and time of the operation performed during the session.
        status (JobStatus | Unset): Specifies the status of the performed session.
        message (None | str | Unset): Description of the performed operation.
        resource_hash_id (None | str | Unset): Internal ID assigned to the processed resource in the Veeam Backup for
            Microsoft Azure REST API.
        execution_start_time (datetime.datetime | None | Unset): Date and time when the session started.
        execution_duration (None | str | Unset): Time taken to complete the operation.
    """

    log_time: datetime.datetime | Unset = UNSET
    status: JobStatus | Unset = UNSET
    message: None | str | Unset = UNSET
    resource_hash_id: None | str | Unset = UNSET
    execution_start_time: datetime.datetime | None | Unset = UNSET
    execution_duration: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        log_time: str | Unset = UNSET
        if not isinstance(self.log_time, Unset):
            log_time = self.log_time.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        resource_hash_id: None | str | Unset
        if isinstance(self.resource_hash_id, Unset):
            resource_hash_id = UNSET
        else:
            resource_hash_id = self.resource_hash_id

        execution_start_time: None | str | Unset
        if isinstance(self.execution_start_time, Unset):
            execution_start_time = UNSET
        elif isinstance(self.execution_start_time, datetime.datetime):
            execution_start_time = self.execution_start_time.isoformat()
        else:
            execution_start_time = self.execution_start_time

        execution_duration: None | str | Unset
        if isinstance(self.execution_duration, Unset):
            execution_duration = UNSET
        else:
            execution_duration = self.execution_duration

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if log_time is not UNSET:
            field_dict["logTime"] = log_time
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if resource_hash_id is not UNSET:
            field_dict["resourceHashId"] = resource_hash_id
        if execution_start_time is not UNSET:
            field_dict["executionStartTime"] = execution_start_time
        if execution_duration is not UNSET:
            field_dict["executionDuration"] = execution_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _log_time = d.pop("logTime", UNSET)
        log_time: datetime.datetime | Unset
        if isinstance(_log_time, Unset):
            log_time = UNSET
        else:
            log_time = isoparse(_log_time)

        _status = d.pop("status", UNSET)
        status: JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_resource_hash_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_hash_id = _parse_resource_hash_id(d.pop("resourceHashId", UNSET))

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

        def _parse_execution_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_duration = _parse_execution_duration(d.pop("executionDuration", UNSET))

        log_item = cls(
            log_time=log_time,
            status=status,
            message=message,
            resource_hash_id=resource_hash_id,
            execution_start_time=execution_start_time,
            execution_duration=execution_duration,
        )

        return log_item
