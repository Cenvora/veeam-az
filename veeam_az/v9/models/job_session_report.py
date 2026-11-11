from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.job_session_type import JobSessionType
from ..models.job_status import JobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="JobSessionReport")


@_attrs_define
class JobSessionReport:
    """
    Attributes:
        status (JobStatus): Specifies the status of the performed session.
        id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the session.
        type_ (JobSessionType | Unset): Type of the session.
        localized_type (None | str | Unset):
        execution_start_time (datetime.datetime | None | Unset): Date and time when the session must run.
        execution_stop_time (datetime.datetime | None | Unset): Date and time when the session must stop.
        execution_duration (None | str | Unset): The duration of the session.
        policy_name (None | str | Unset):
        restore_reason (None | str | Unset):
        flr_resource_name (None | str | Unset):
        protected_instances_count (int | None | Unset): Total number of Azure resources protected by the backup session.
        deleted_restore_points_count (int | None | Unset): Total number of Azure resources deleted by the deletion
            session.
        checked_instances_count (int | None | Unset): Total number of Azure resources checked by the healt-check
            session.
        restored_items_count (int | None | Unset): Total number of Azure resources restored by the restore session.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    status: JobStatus
    id: None | str | Unset = UNSET
    type_: JobSessionType | Unset = UNSET
    localized_type: None | str | Unset = UNSET
    execution_start_time: datetime.datetime | None | Unset = UNSET
    execution_stop_time: datetime.datetime | None | Unset = UNSET
    execution_duration: None | str | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    restore_reason: None | str | Unset = UNSET
    flr_resource_name: None | str | Unset = UNSET
    protected_instances_count: int | None | Unset = UNSET
    deleted_restore_points_count: int | None | Unset = UNSET
    checked_instances_count: int | None | Unset = UNSET
    restored_items_count: int | None | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        status = self.status.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        localized_type: None | str | Unset
        if isinstance(self.localized_type, Unset):
            localized_type = UNSET
        else:
            localized_type = self.localized_type

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

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        restore_reason: None | str | Unset
        if isinstance(self.restore_reason, Unset):
            restore_reason = UNSET
        else:
            restore_reason = self.restore_reason

        flr_resource_name: None | str | Unset
        if isinstance(self.flr_resource_name, Unset):
            flr_resource_name = UNSET
        else:
            flr_resource_name = self.flr_resource_name

        protected_instances_count: int | None | Unset
        if isinstance(self.protected_instances_count, Unset):
            protected_instances_count = UNSET
        else:
            protected_instances_count = self.protected_instances_count

        deleted_restore_points_count: int | None | Unset
        if isinstance(self.deleted_restore_points_count, Unset):
            deleted_restore_points_count = UNSET
        else:
            deleted_restore_points_count = self.deleted_restore_points_count

        checked_instances_count: int | None | Unset
        if isinstance(self.checked_instances_count, Unset):
            checked_instances_count = UNSET
        else:
            checked_instances_count = self.checked_instances_count

        restored_items_count: int | None | Unset
        if isinstance(self.restored_items_count, Unset):
            restored_items_count = UNSET
        else:
            restored_items_count = self.restored_items_count

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if localized_type is not UNSET:
            field_dict["localizedType"] = localized_type
        if execution_start_time is not UNSET:
            field_dict["executionStartTime"] = execution_start_time
        if execution_stop_time is not UNSET:
            field_dict["executionStopTime"] = execution_stop_time
        if execution_duration is not UNSET:
            field_dict["executionDuration"] = execution_duration
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if restore_reason is not UNSET:
            field_dict["restoreReason"] = restore_reason
        if flr_resource_name is not UNSET:
            field_dict["flrResourceName"] = flr_resource_name
        if protected_instances_count is not UNSET:
            field_dict["protectedInstancesCount"] = protected_instances_count
        if deleted_restore_points_count is not UNSET:
            field_dict["deletedRestorePointsCount"] = deleted_restore_points_count
        if checked_instances_count is not UNSET:
            field_dict["checkedInstancesCount"] = checked_instances_count
        if restored_items_count is not UNSET:
            field_dict["restoredItemsCount"] = restored_items_count
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)
        status = JobStatus(d.pop("status"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: JobSessionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = JobSessionType(_type_)

        def _parse_localized_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        localized_type = _parse_localized_type(d.pop("localizedType", UNSET))

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

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        def _parse_restore_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        restore_reason = _parse_restore_reason(d.pop("restoreReason", UNSET))

        def _parse_flr_resource_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flr_resource_name = _parse_flr_resource_name(d.pop("flrResourceName", UNSET))

        def _parse_protected_instances_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        protected_instances_count = _parse_protected_instances_count(d.pop("protectedInstancesCount", UNSET))

        def _parse_deleted_restore_points_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deleted_restore_points_count = _parse_deleted_restore_points_count(d.pop("deletedRestorePointsCount", UNSET))

        def _parse_checked_instances_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        checked_instances_count = _parse_checked_instances_count(d.pop("checkedInstancesCount", UNSET))

        def _parse_restored_items_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        restored_items_count = _parse_restored_items_count(d.pop("restoredItemsCount", UNSET))

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        job_session_report = cls(
            status=status,
            id=id,
            type_=type_,
            localized_type=localized_type,
            execution_start_time=execution_start_time,
            execution_stop_time=execution_stop_time,
            execution_duration=execution_duration,
            policy_name=policy_name,
            restore_reason=restore_reason,
            flr_resource_name=flr_resource_name,
            protected_instances_count=protected_instances_count,
            deleted_restore_points_count=deleted_restore_points_count,
            checked_instances_count=checked_instances_count,
            restored_items_count=restored_items_count,
            field_links=field_links,
        )

        return job_session_report
