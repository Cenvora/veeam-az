from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthCheckJobInfo")


@_attrs_define
class HealthCheckJobInfo:
    r"""\[Applies only if backup creation is enabled for the backup policy] Health check schedule settings configured for
    the backup policy.

        Attributes:
            policy_id (UUID | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the backup
                policy.
            policy_name (str | Unset): Name of the backup policy.
            checked_instances_count (int | Unset): Total count of the health checked resources.
            policy_removed (bool | Unset): Defines whether the backup policy is no longer present in the Veeam Backup for
                Microsoft Azure configuration database.
    """

    policy_id: UUID | Unset = UNSET
    policy_name: str | Unset = UNSET
    checked_instances_count: int | Unset = UNSET
    policy_removed: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        policy_id: str | Unset = UNSET
        if not isinstance(self.policy_id, Unset):
            policy_id = str(self.policy_id)

        policy_name = self.policy_name

        checked_instances_count = self.checked_instances_count

        policy_removed = self.policy_removed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if checked_instances_count is not UNSET:
            field_dict["checkedInstancesCount"] = checked_instances_count
        if policy_removed is not UNSET:
            field_dict["policyRemoved"] = policy_removed

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

        checked_instances_count = d.pop("checkedInstancesCount", UNSET)

        policy_removed = d.pop("policyRemoved", UNSET)

        health_check_job_info = cls(
            policy_id=policy_id,
            policy_name=policy_name,
            checked_instances_count=checked_instances_count,
            policy_removed=policy_removed,
        )

        return health_check_job_info
