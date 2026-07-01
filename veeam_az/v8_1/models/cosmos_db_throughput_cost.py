from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CosmosDbThroughputCost")


@_attrs_define
class CosmosDbThroughputCost:
    """
    Attributes:
        min_hourly_price (float | Unset):
        max_hourly_price (float | Unset):
        min_daily_price (float | Unset):
        max_daily_price (float | Unset):
        min_monthly_price (float | Unset):
        max_monthly_price (float | Unset):
        min_throughput (float | Unset):
        max_throughput (float | Unset):
        request_unit_price (float | Unset):
        region_count (int | Unset):
        exceeds_total_throughput (bool | Unset):
    """

    min_hourly_price: float | Unset = UNSET
    max_hourly_price: float | Unset = UNSET
    min_daily_price: float | Unset = UNSET
    max_daily_price: float | Unset = UNSET
    min_monthly_price: float | Unset = UNSET
    max_monthly_price: float | Unset = UNSET
    min_throughput: float | Unset = UNSET
    max_throughput: float | Unset = UNSET
    request_unit_price: float | Unset = UNSET
    region_count: int | Unset = UNSET
    exceeds_total_throughput: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        min_hourly_price = self.min_hourly_price

        max_hourly_price = self.max_hourly_price

        min_daily_price = self.min_daily_price

        max_daily_price = self.max_daily_price

        min_monthly_price = self.min_monthly_price

        max_monthly_price = self.max_monthly_price

        min_throughput = self.min_throughput

        max_throughput = self.max_throughput

        request_unit_price = self.request_unit_price

        region_count = self.region_count

        exceeds_total_throughput = self.exceeds_total_throughput

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if min_hourly_price is not UNSET:
            field_dict["minHourlyPrice"] = min_hourly_price
        if max_hourly_price is not UNSET:
            field_dict["maxHourlyPrice"] = max_hourly_price
        if min_daily_price is not UNSET:
            field_dict["minDailyPrice"] = min_daily_price
        if max_daily_price is not UNSET:
            field_dict["maxDailyPrice"] = max_daily_price
        if min_monthly_price is not UNSET:
            field_dict["minMonthlyPrice"] = min_monthly_price
        if max_monthly_price is not UNSET:
            field_dict["maxMonthlyPrice"] = max_monthly_price
        if min_throughput is not UNSET:
            field_dict["minThroughput"] = min_throughput
        if max_throughput is not UNSET:
            field_dict["maxThroughput"] = max_throughput
        if request_unit_price is not UNSET:
            field_dict["requestUnitPrice"] = request_unit_price
        if region_count is not UNSET:
            field_dict["regionCount"] = region_count
        if exceeds_total_throughput is not UNSET:
            field_dict["exceedsTotalThroughput"] = exceeds_total_throughput

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_hourly_price = d.pop("minHourlyPrice", UNSET)

        max_hourly_price = d.pop("maxHourlyPrice", UNSET)

        min_daily_price = d.pop("minDailyPrice", UNSET)

        max_daily_price = d.pop("maxDailyPrice", UNSET)

        min_monthly_price = d.pop("minMonthlyPrice", UNSET)

        max_monthly_price = d.pop("maxMonthlyPrice", UNSET)

        min_throughput = d.pop("minThroughput", UNSET)

        max_throughput = d.pop("maxThroughput", UNSET)

        request_unit_price = d.pop("requestUnitPrice", UNSET)

        region_count = d.pop("regionCount", UNSET)

        exceeds_total_throughput = d.pop("exceedsTotalThroughput", UNSET)

        cosmos_db_throughput_cost = cls(
            min_hourly_price=min_hourly_price,
            max_hourly_price=max_hourly_price,
            min_daily_price=min_daily_price,
            max_daily_price=max_daily_price,
            min_monthly_price=min_monthly_price,
            max_monthly_price=max_monthly_price,
            min_throughput=min_throughput,
            max_throughput=max_throughput,
            request_unit_price=request_unit_price,
            region_count=region_count,
            exceeds_total_throughput=exceeds_total_throughput,
        )

        return cosmos_db_throughput_cost
