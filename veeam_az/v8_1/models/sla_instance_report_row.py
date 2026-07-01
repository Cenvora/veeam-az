from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sla_compliance_status import SlaComplianceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaInstanceReportRow")


@_attrs_define
class SlaInstanceReportRow:
    """Information on SLA compliance for each Azure VM included into the backup scope of the policy.

    Attributes:
        instance_id (str | Unset): Resource ID assigned to a VM in Microsoft Azure.
        instance_name (str | Unset): Name of the VM.
        status (SlaComplianceStatus | Unset): SLA compliance status.
        achieved_sla_percent (float | Unset): SLA compliance ratio achieved for the VM; that is, a percentage of
            successfully created restore points out of the total number of restore points expected to be produced by the
            policy.
        planned (float | Unset): Total number of restore points expected to be produced for the VM.
        successful (float | Unset): Number of restore points successfully created for the VM.
        missed (float | Unset): Number of restore points failed to be created for the VM.
    """

    instance_id: str | Unset = UNSET
    instance_name: str | Unset = UNSET
    status: SlaComplianceStatus | Unset = UNSET
    achieved_sla_percent: float | Unset = UNSET
    planned: float | Unset = UNSET
    successful: float | Unset = UNSET
    missed: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_id = self.instance_id

        instance_name = self.instance_name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        achieved_sla_percent = self.achieved_sla_percent

        planned = self.planned

        successful = self.successful

        missed = self.missed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name
        if status is not UNSET:
            field_dict["status"] = status
        if achieved_sla_percent is not UNSET:
            field_dict["achievedSlaPercent"] = achieved_sla_percent
        if planned is not UNSET:
            field_dict["planned"] = planned
        if successful is not UNSET:
            field_dict["successful"] = successful
        if missed is not UNSET:
            field_dict["missed"] = missed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_id = d.pop("instanceId", UNSET)

        instance_name = d.pop("instanceName", UNSET)

        _status = d.pop("status", UNSET)
        status: SlaComplianceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SlaComplianceStatus(_status)

        achieved_sla_percent = d.pop("achievedSlaPercent", UNSET)

        planned = d.pop("planned", UNSET)

        successful = d.pop("successful", UNSET)

        missed = d.pop("missed", UNSET)

        sla_instance_report_row = cls(
            instance_id=instance_id,
            instance_name=instance_name,
            status=status,
            achieved_sla_percent=achieved_sla_percent,
            planned=planned,
            successful=successful,
            missed=missed,
        )

        sla_instance_report_row.additional_properties = d
        return sla_instance_report_row

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
