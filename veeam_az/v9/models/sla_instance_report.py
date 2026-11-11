from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sla_instance_report_row import SlaInstanceReportRow
    from ..models.sla_statistic_report import SlaStatisticReport


T = TypeVar("T", bound="SlaInstanceReport")


@_attrs_define
class SlaInstanceReport:
    """
    Attributes:
        statistic (SlaStatisticReport | Unset): Information on SLA compliance for all Azure VMs included into the backup
            scope of the policy.
        items (list[SlaInstanceReportRow] | Unset): Information on SLA compliance for each VM included into the backup
            scope of the policy.
    """

    statistic: SlaStatisticReport | Unset = UNSET
    items: list[SlaInstanceReportRow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statistic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistic, Unset):
            statistic = self.statistic.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statistic is not UNSET:
            field_dict["statistic"] = statistic
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sla_instance_report_row import SlaInstanceReportRow
        from ..models.sla_statistic_report import SlaStatisticReport

        d = dict(src_dict)
        _statistic = d.pop("statistic", UNSET)
        statistic: SlaStatisticReport | Unset
        if isinstance(_statistic, Unset):
            statistic = UNSET
        else:
            statistic = SlaStatisticReport.from_dict(_statistic)

        _items = d.pop("items", UNSET)
        items: list[SlaInstanceReportRow] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = SlaInstanceReportRow.from_dict(items_item_data)

                items.append(items_item)

        sla_instance_report = cls(
            statistic=statistic,
            items=items,
        )

        sla_instance_report.additional_properties = d
        return sla_instance_report

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
