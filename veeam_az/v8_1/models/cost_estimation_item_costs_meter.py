from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.price_list_item_unit import PriceListItemUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimation_meter_resource import CostEstimationMeterResource


T = TypeVar("T", bound="CostEstimationItemCostsMeter")


@_attrs_define
class CostEstimationItemCostsMeter:
    """Information on each billing meter.

    Attributes:
        resource (CostEstimationMeterResource | Unset): Information on the disk used by the backup policy.
        meter_id (UUID | Unset): Microsoft Azure ID assigned to the billing meter used for the protected resource.
        description (None | str | Unset): Description automatically added in accordance with the data from Microsoft
            Azure.
        unit_price (float | None | Unset): Price per unit.
        unit (PriceListItemUnit | Unset): Unit of price and quantity.
        quantity_used (float | Unset): Quantity of the disk space used by the protected resource.
    """

    resource: CostEstimationMeterResource | Unset = UNSET
    meter_id: UUID | Unset = UNSET
    description: None | str | Unset = UNSET
    unit_price: float | None | Unset = UNSET
    unit: PriceListItemUnit | Unset = UNSET
    quantity_used: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        meter_id: str | Unset = UNSET
        if not isinstance(self.meter_id, Unset):
            meter_id = str(self.meter_id)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        unit_price: float | None | Unset
        if isinstance(self.unit_price, Unset):
            unit_price = UNSET
        else:
            unit_price = self.unit_price

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        quantity_used = self.quantity_used

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource is not UNSET:
            field_dict["resource"] = resource
        if meter_id is not UNSET:
            field_dict["meterId"] = meter_id
        if description is not UNSET:
            field_dict["description"] = description
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if unit is not UNSET:
            field_dict["unit"] = unit
        if quantity_used is not UNSET:
            field_dict["quantityUsed"] = quantity_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_estimation_meter_resource import CostEstimationMeterResource

        d = dict(src_dict)
        _resource = d.pop("resource", UNSET)
        resource: CostEstimationMeterResource | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = CostEstimationMeterResource.from_dict(_resource)

        _meter_id = d.pop("meterId", UNSET)
        meter_id: UUID | Unset
        if isinstance(_meter_id, Unset):
            meter_id = UNSET
        else:
            meter_id = UUID(_meter_id)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_unit_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unit_price = _parse_unit_price(d.pop("unitPrice", UNSET))

        _unit = d.pop("unit", UNSET)
        unit: PriceListItemUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = PriceListItemUnit(_unit)

        quantity_used = d.pop("quantityUsed", UNSET)

        cost_estimation_item_costs_meter = cls(
            resource=resource,
            meter_id=meter_id,
            description=description,
            unit_price=unit_price,
            unit=unit,
            quantity_used=quantity_used,
        )

        return cost_estimation_item_costs_meter
