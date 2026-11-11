from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.flr_session_restore_task_log_item_status_nullable import FlrSessionRestoreTaskLogItemStatusNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlrSessionRestoreTaskLogItem")


@_attrs_define
class FlrSessionRestoreTaskLogItem:
    """
    Attributes:
        message (str | Unset): Description of the performed operation.
        status (FlrSessionRestoreTaskLogItemStatusNullable | Unset): Status of the restore task.
        id (int | None | Unset): System ID assigned to the log record in the Veeam Backup for Microsoft Azure REST API.
        start_time (datetime.datetime | None | Unset): Date and time when the restore task started.
        stop_time (datetime.datetime | None | Unset): Date and time when the restore task finished or stopped.
    """

    message: str | Unset = UNSET
    status: FlrSessionRestoreTaskLogItemStatusNullable | Unset = UNSET
    id: int | None | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    stop_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        stop_time: None | str | Unset
        if isinstance(self.stop_time, Unset):
            stop_time = UNSET
        elif isinstance(self.stop_time, datetime.datetime):
            stop_time = self.stop_time.isoformat()
        else:
            stop_time = self.stop_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if id is not UNSET:
            field_dict["id"] = id
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if stop_time is not UNSET:
            field_dict["stopTime"] = stop_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _status = d.pop("status", UNSET)
        status: FlrSessionRestoreTaskLogItemStatusNullable | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FlrSessionRestoreTaskLogItemStatusNullable(_status)

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_stop_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stop_time_type_0 = isoparse(data)

                return stop_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        stop_time = _parse_stop_time(d.pop("stopTime", UNSET))

        flr_session_restore_task_log_item = cls(
            message=message,
            status=status,
            id=id,
            start_time=start_time,
            stop_time=stop_time,
        )

        return flr_session_restore_task_log_item
