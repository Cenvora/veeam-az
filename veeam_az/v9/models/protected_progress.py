from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rates import Rates


T = TypeVar("T", bound="ProtectedProgress")


@_attrs_define
class ProtectedProgress:
    """Information on the backup policy.

    Attributes:
        job_session_id (None | str | Unset): System ID assigned to a backup policy in the Veeam Backup for Microsoft
            Azure REST API.
        status (JobStatus | Unset): Specifies the status of the performed session.
        start_time (datetime.datetime | Unset): Date and time when the policy started.
        end_time (datetime.datetime | None | Unset): Date and time when the policy finished or stopped.
        rates (Rates | Unset): Statistics on the data processed by the backup policy.
    """

    job_session_id: None | str | Unset = UNSET
    status: JobStatus | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    rates: Rates | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        job_session_id: None | str | Unset
        if isinstance(self.job_session_id, Unset):
            job_session_id = UNSET
        else:
            job_session_id = self.job_session_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        rates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rates, Unset):
            rates = self.rates.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if job_session_id is not UNSET:
            field_dict["jobSessionId"] = job_session_id
        if status is not UNSET:
            field_dict["status"] = status
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rates import Rates

        d = dict(src_dict)

        def _parse_job_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_session_id = _parse_job_session_id(d.pop("jobSessionId", UNSET))

        _status = d.pop("status", UNSET)
        status: JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        _rates = d.pop("rates", UNSET)
        rates: Rates | Unset
        if isinstance(_rates, Unset):
            rates = UNSET
        else:
            rates = Rates.from_dict(_rates)

        protected_progress = cls(
            job_session_id=job_session_id,
            status=status,
            start_time=start_time,
            end_time=end_time,
            rates=rates,
        )

        return protected_progress
