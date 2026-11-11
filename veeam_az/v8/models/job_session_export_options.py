from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.job_status import JobStatus
from ..models.session_type import SessionType
from ..models.workload_type import WorkloadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobSessionExportOptions")


@_attrs_define
class JobSessionExportOptions:
    """
    Attributes:
        job_session_ids (list[str] | None | Unset): Specifies system IDs assigned in the Veeam Backup for Microsoft
            Azure REST API to sessions whose data will be exported.
        policy_id (None | Unset | UUID): Exports only statistics on sessions related to a backup policy with the
            specified system ID.
        filter_ (None | str | Unset): Exports only statistics on sessions related to a backup policy with the specified
            name.
        status (list[JobStatus] | None | Unset): Exports only statistics on sessions with the specified statuses.
        session_types (list[SessionType] | None | Unset): Exports only statistics on sessions of the specified types.
        workload_types (list[WorkloadType] | None | Unset): Exports only statistics on sessions related to the specified
            workload types.
        from_utc (datetime.datetime | None | Unset): Exports only statistics on sessions launched after the specified
            date and time. **Note**&#58; The property value must be specified in the UTC time zone in the following
            format&#58; YYYY-MM-DDTHH:MM:SSZ.
        to_utc (datetime.datetime | None | Unset): Exports only statistics on sessions launched before the specified
            date and time. **Note**&#58; The property value must be specified in the UTC time zone in the following
            format&#58; YYYY-MM-DDTHH:MM:SSZ.
    """

    job_session_ids: list[str] | None | Unset = UNSET
    policy_id: None | Unset | UUID = UNSET
    filter_: None | str | Unset = UNSET
    status: list[JobStatus] | None | Unset = UNSET
    session_types: list[SessionType] | None | Unset = UNSET
    workload_types: list[WorkloadType] | None | Unset = UNSET
    from_utc: datetime.datetime | None | Unset = UNSET
    to_utc: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        job_session_ids: list[str] | None | Unset
        if isinstance(self.job_session_ids, Unset):
            job_session_ids = UNSET
        elif isinstance(self.job_session_ids, list):
            job_session_ids = self.job_session_ids

        else:
            job_session_ids = self.job_session_ids

        policy_id: None | str | Unset
        if isinstance(self.policy_id, Unset):
            policy_id = UNSET
        elif isinstance(self.policy_id, UUID):
            policy_id = str(self.policy_id)
        else:
            policy_id = self.policy_id

        filter_: None | str | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = self.filter_

        status: list[str] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, list):
            status = []
            for status_type_0_item_data in self.status:
                status_type_0_item = status_type_0_item_data.value
                status.append(status_type_0_item)

        else:
            status = self.status

        session_types: list[str] | None | Unset
        if isinstance(self.session_types, Unset):
            session_types = UNSET
        elif isinstance(self.session_types, list):
            session_types = []
            for session_types_type_0_item_data in self.session_types:
                session_types_type_0_item = session_types_type_0_item_data.value
                session_types.append(session_types_type_0_item)

        else:
            session_types = self.session_types

        workload_types: list[str] | None | Unset
        if isinstance(self.workload_types, Unset):
            workload_types = UNSET
        elif isinstance(self.workload_types, list):
            workload_types = []
            for workload_types_type_0_item_data in self.workload_types:
                workload_types_type_0_item = workload_types_type_0_item_data.value
                workload_types.append(workload_types_type_0_item)

        else:
            workload_types = self.workload_types

        from_utc: None | str | Unset
        if isinstance(self.from_utc, Unset):
            from_utc = UNSET
        elif isinstance(self.from_utc, datetime.datetime):
            from_utc = self.from_utc.isoformat()
        else:
            from_utc = self.from_utc

        to_utc: None | str | Unset
        if isinstance(self.to_utc, Unset):
            to_utc = UNSET
        elif isinstance(self.to_utc, datetime.datetime):
            to_utc = self.to_utc.isoformat()
        else:
            to_utc = self.to_utc

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if job_session_ids is not UNSET:
            field_dict["jobSessionIds"] = job_session_ids
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if status is not UNSET:
            field_dict["status"] = status
        if session_types is not UNSET:
            field_dict["sessionTypes"] = session_types
        if workload_types is not UNSET:
            field_dict["workloadTypes"] = workload_types
        if from_utc is not UNSET:
            field_dict["fromUtc"] = from_utc
        if to_utc is not UNSET:
            field_dict["toUtc"] = to_utc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_job_session_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_session_ids_type_0 = cast(list[str], data)

                return job_session_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        job_session_ids = _parse_job_session_ids(d.pop("jobSessionIds", UNSET))

        def _parse_policy_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                policy_id_type_0 = UUID(data)

                return policy_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        policy_id = _parse_policy_id(d.pop("policyId", UNSET))

        def _parse_filter_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        def _parse_status(data: object) -> list[JobStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                status_type_0 = []
                _status_type_0 = data
                for status_type_0_item_data in _status_type_0:
                    status_type_0_item = JobStatus(status_type_0_item_data)

                    status_type_0.append(status_type_0_item)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobStatus] | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_session_types(data: object) -> list[SessionType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                session_types_type_0 = []
                _session_types_type_0 = data
                for session_types_type_0_item_data in _session_types_type_0:
                    session_types_type_0_item = SessionType(session_types_type_0_item_data)

                    session_types_type_0.append(session_types_type_0_item)

                return session_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SessionType] | None | Unset, data)

        session_types = _parse_session_types(d.pop("sessionTypes", UNSET))

        def _parse_workload_types(data: object) -> list[WorkloadType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                workload_types_type_0 = []
                _workload_types_type_0 = data
                for workload_types_type_0_item_data in _workload_types_type_0:
                    workload_types_type_0_item = WorkloadType(workload_types_type_0_item_data)

                    workload_types_type_0.append(workload_types_type_0_item)

                return workload_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WorkloadType] | None | Unset, data)

        workload_types = _parse_workload_types(d.pop("workloadTypes", UNSET))

        def _parse_from_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_utc_type_0 = isoparse(data)

                return from_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_utc = _parse_from_utc(d.pop("fromUtc", UNSET))

        def _parse_to_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_utc_type_0 = isoparse(data)

                return to_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        to_utc = _parse_to_utc(d.pop("toUtc", UNSET))

        job_session_export_options = cls(
            job_session_ids=job_session_ids,
            policy_id=policy_id,
            filter_=filter_,
            status=status,
            session_types=session_types,
            workload_types=workload_types,
            from_utc=from_utc,
            to_utc=to_utc,
        )

        return job_session_export_options
