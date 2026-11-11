from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sla_compliance_status import SlaComplianceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaTimeSeriesPoint")


@_attrs_define
class SlaTimeSeriesPoint:
    """
    Attributes:
        from_ (datetime.date | Unset): Date and time when the period started.
        to (datetime.date | Unset): Date and time when the period ended.
        processed_objects (float | None | Unset): Number of protected VMs for which Veeam Backup for Microsoft Azure
            calculated the SLA compliance ratio for the period.
        achieved_sla_percent (float | None | Unset): Average SLA compliance ratio calculated for the period.
        status (SlaComplianceStatus | Unset): SLA compliance status.
    """

    from_: datetime.date | Unset = UNSET
    to: datetime.date | Unset = UNSET
    processed_objects: float | None | Unset = UNSET
    achieved_sla_percent: float | None | Unset = UNSET
    status: SlaComplianceStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        processed_objects: float | None | Unset
        if isinstance(self.processed_objects, Unset):
            processed_objects = UNSET
        else:
            processed_objects = self.processed_objects

        achieved_sla_percent: float | None | Unset
        if isinstance(self.achieved_sla_percent, Unset):
            achieved_sla_percent = UNSET
        else:
            achieved_sla_percent = self.achieved_sla_percent

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if processed_objects is not UNSET:
            field_dict["ProcessedObjects"] = processed_objects
        if achieved_sla_percent is not UNSET:
            field_dict["achievedSlaPercent"] = achieved_sla_percent
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_).date()

        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to).date()

        def _parse_processed_objects(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        processed_objects = _parse_processed_objects(d.pop("ProcessedObjects", UNSET))

        def _parse_achieved_sla_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        achieved_sla_percent = _parse_achieved_sla_percent(d.pop("achievedSlaPercent", UNSET))

        _status = d.pop("status", UNSET)
        status: SlaComplianceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SlaComplianceStatus(_status)

        sla_time_series_point = cls(
            from_=from_,
            to=to,
            processed_objects=processed_objects,
            achieved_sla_percent=achieved_sla_percent,
            status=status,
        )

        sla_time_series_point.additional_properties = d
        return sla_time_series_point

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
