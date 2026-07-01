from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.protection_policy_sla_compliance_status import ProtectionPolicySlaComplianceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionPolicySlaReport")


@_attrs_define
class ProtectionPolicySlaReport:
    """SLA compliance report for each schedule type.

    Attributes:
        status (ProtectionPolicySlaComplianceStatus | Unset): SLA compliance status.
        achieved_sla_percent (float | None | Unset): Average SLA compliance ratio reached by the policy for the schedule
            type.
    """

    status: ProtectionPolicySlaComplianceStatus | Unset = UNSET
    achieved_sla_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        achieved_sla_percent: float | None | Unset
        if isinstance(self.achieved_sla_percent, Unset):
            achieved_sla_percent = UNSET
        else:
            achieved_sla_percent = self.achieved_sla_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if achieved_sla_percent is not UNSET:
            field_dict["achievedSlaPercent"] = achieved_sla_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ProtectionPolicySlaComplianceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProtectionPolicySlaComplianceStatus(_status)

        def _parse_achieved_sla_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        achieved_sla_percent = _parse_achieved_sla_percent(d.pop("achievedSlaPercent", UNSET))

        protection_policy_sla_report = cls(
            status=status,
            achieved_sla_percent=achieved_sla_percent,
        )

        protection_policy_sla_report.additional_properties = d
        return protection_policy_sla_report

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
