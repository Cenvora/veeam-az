from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.job_status import JobStatus
from ..models.policy_status import PolicyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualMachinePoliciesExportOptions")


@_attrs_define
class VirtualMachinePoliciesExportOptions:
    """
    Attributes:
        policy_ids (list[UUID] | None | Unset): Specifies system IDs assigned in the Veeam Backup for Microsoft Azure
            REST API to Azure VM schedule-based backup policies whose data will be exported.
        policy_name (None | str | Unset): Exports only data on a backup policy with the specified name.
        last_job_status (list[JobStatus] | None | Unset): Exports only data on backup policies with the specified latest
            backup session statuses.
        policy_status (list[PolicyStatus] | None | Unset): Exports only data on backup policies with the specified
            statuses.
    """

    policy_ids: list[UUID] | None | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    last_job_status: list[JobStatus] | None | Unset = UNSET
    policy_status: list[PolicyStatus] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        policy_ids: list[str] | None | Unset
        if isinstance(self.policy_ids, Unset):
            policy_ids = UNSET
        elif isinstance(self.policy_ids, list):
            policy_ids = []
            for policy_ids_type_0_item_data in self.policy_ids:
                policy_ids_type_0_item = str(policy_ids_type_0_item_data)
                policy_ids.append(policy_ids_type_0_item)

        else:
            policy_ids = self.policy_ids

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        last_job_status: list[str] | None | Unset
        if isinstance(self.last_job_status, Unset):
            last_job_status = UNSET
        elif isinstance(self.last_job_status, list):
            last_job_status = []
            for last_job_status_type_0_item_data in self.last_job_status:
                last_job_status_type_0_item = last_job_status_type_0_item_data.value
                last_job_status.append(last_job_status_type_0_item)

        else:
            last_job_status = self.last_job_status

        policy_status: list[str] | None | Unset
        if isinstance(self.policy_status, Unset):
            policy_status = UNSET
        elif isinstance(self.policy_status, list):
            policy_status = []
            for policy_status_type_0_item_data in self.policy_status:
                policy_status_type_0_item = policy_status_type_0_item_data.value
                policy_status.append(policy_status_type_0_item)

        else:
            policy_status = self.policy_status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if policy_ids is not UNSET:
            field_dict["policyIds"] = policy_ids
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if last_job_status is not UNSET:
            field_dict["lastJobStatus"] = last_job_status
        if policy_status is not UNSET:
            field_dict["policyStatus"] = policy_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_policy_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policy_ids_type_0 = []
                _policy_ids_type_0 = data
                for policy_ids_type_0_item_data in _policy_ids_type_0:
                    policy_ids_type_0_item = UUID(policy_ids_type_0_item_data)

                    policy_ids_type_0.append(policy_ids_type_0_item)

                return policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        policy_ids = _parse_policy_ids(d.pop("policyIds", UNSET))

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        def _parse_last_job_status(data: object) -> list[JobStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                last_job_status_type_0 = []
                _last_job_status_type_0 = data
                for last_job_status_type_0_item_data in _last_job_status_type_0:
                    last_job_status_type_0_item = JobStatus(last_job_status_type_0_item_data)

                    last_job_status_type_0.append(last_job_status_type_0_item)

                return last_job_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobStatus] | None | Unset, data)

        last_job_status = _parse_last_job_status(d.pop("lastJobStatus", UNSET))

        def _parse_policy_status(data: object) -> list[PolicyStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policy_status_type_0 = []
                _policy_status_type_0 = data
                for policy_status_type_0_item_data in _policy_status_type_0:
                    policy_status_type_0_item = PolicyStatus(policy_status_type_0_item_data)

                    policy_status_type_0.append(policy_status_type_0_item)

                return policy_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolicyStatus] | None | Unset, data)

        policy_status = _parse_policy_status(d.pop("policyStatus", UNSET))

        virtual_machine_policies_export_options = cls(
            policy_ids=policy_ids,
            policy_name=policy_name,
            last_job_status=last_job_status,
            policy_status=policy_status,
        )

        return virtual_machine_policies_export_options
