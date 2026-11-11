from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyInstancesReport")


@_attrs_define
class PolicyInstancesReport:
    """
    Attributes:
        status (JobStatus | Unset): Specifies the status of the performed session.
        instance_id (None | str | Unset):
        instance_name (None | str | Unset):
    """

    status: JobStatus | Unset = UNSET
    instance_id: None | str | Unset = UNSET
    instance_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        instance_id: None | str | Unset
        if isinstance(self.instance_id, Unset):
            instance_id = UNSET
        else:
            instance_id = self.instance_id

        instance_name: None | str | Unset
        if isinstance(self.instance_name, Unset):
            instance_name = UNSET
        else:
            instance_name = self.instance_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        def _parse_instance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance_id = _parse_instance_id(d.pop("instanceId", UNSET))

        def _parse_instance_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance_name = _parse_instance_name(d.pop("instanceName", UNSET))

        policy_instances_report = cls(
            status=status,
            instance_id=instance_id,
            instance_name=instance_name,
        )

        return policy_instances_report
