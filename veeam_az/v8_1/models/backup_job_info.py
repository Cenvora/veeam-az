from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.policy_type import PolicyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupJobInfo")


@_attrs_define
class BackupJobInfo:
    """Information on a backup policy.

    Attributes:
        policy_id (None | Unset | UUID): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the
            backup policy.
        policy_name (None | str | Unset): Name of the backup policy.
        policy_type (PolicyType | Unset): Workload type protected by a backup policy.
        protected_instances_count (int | Unset): Total number of Azure resources protected by the backup policy.
        policy_removed (bool | Unset): Defines whether the backup policy is no longer present in the Veeam Backup for
            Microsoft Azure configuration database.
    """

    policy_id: None | Unset | UUID = UNSET
    policy_name: None | str | Unset = UNSET
    policy_type: PolicyType | Unset = UNSET
    protected_instances_count: int | Unset = UNSET
    policy_removed: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        policy_id: None | str | Unset
        if isinstance(self.policy_id, Unset):
            policy_id = UNSET
        elif isinstance(self.policy_id, UUID):
            policy_id = str(self.policy_id)
        else:
            policy_id = self.policy_id

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        policy_type: str | Unset = UNSET
        if not isinstance(self.policy_type, Unset):
            policy_type = self.policy_type.value

        protected_instances_count = self.protected_instances_count

        policy_removed = self.policy_removed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if policy_type is not UNSET:
            field_dict["policyType"] = policy_type
        if protected_instances_count is not UNSET:
            field_dict["protectedInstancesCount"] = protected_instances_count
        if policy_removed is not UNSET:
            field_dict["policyRemoved"] = policy_removed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        _policy_type = d.pop("policyType", UNSET)
        policy_type: PolicyType | Unset
        if isinstance(_policy_type, Unset):
            policy_type = UNSET
        else:
            policy_type = PolicyType(_policy_type)

        protected_instances_count = d.pop("protectedInstancesCount", UNSET)

        policy_removed = d.pop("policyRemoved", UNSET)

        backup_job_info = cls(
            policy_id=policy_id,
            policy_name=policy_name,
            policy_type=policy_type,
            protected_instances_count=protected_instances_count,
            policy_removed=policy_removed,
        )

        return backup_job_info
