from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sla_session_status import SlaSessionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaSessionReportRow")


@_attrs_define
class SlaSessionReportRow:
    """
    Attributes:
        session_id (UUID | Unset): System ID assigned to a session in the Veeam Backup for Microsoft Azure REST API.
        session_name (str | Unset): Name of the session.
        status (SlaSessionStatus | Unset): Session status.
        local_start_time (datetime.datetime | Unset): Date and time (in the time zone of the Azure region in which the
            protected VM resides) when the session started.
        start_time (datetime.datetime | Unset): Date and time (in UTC) when the session started.
    """

    session_id: UUID | Unset = UNSET
    session_name: str | Unset = UNSET
    status: SlaSessionStatus | Unset = UNSET
    local_start_time: datetime.datetime | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id: str | Unset = UNSET
        if not isinstance(self.session_id, Unset):
            session_id = str(self.session_id)

        session_name = self.session_name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        local_start_time: str | Unset = UNSET
        if not isinstance(self.local_start_time, Unset):
            local_start_time = self.local_start_time.isoformat()

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if session_name is not UNSET:
            field_dict["sessionName"] = session_name
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
        _session_id = d.pop("sessionId", UNSET)
        session_id: UUID | Unset
        if isinstance(_session_id, Unset):
            session_id = UNSET
        else:
            session_id = UUID(_session_id)

        session_name = d.pop("sessionName", UNSET)

        _status = d.pop("status", UNSET)
        status: SlaSessionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SlaSessionStatus(_status)

        _local_start_time = d.pop("localStartTime", UNSET)
        local_start_time: datetime.datetime | Unset
        if isinstance(_local_start_time, Unset):
            local_start_time = UNSET
        else:
            local_start_time = isoparse(_local_start_time)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        sla_session_report_row = cls(
            session_id=session_id,
            session_name=session_name,
            status=status,
            local_start_time=local_start_time,
            start_time=start_time,
        )

        sla_session_report_row.additional_properties = d
        return sla_session_report_row

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
