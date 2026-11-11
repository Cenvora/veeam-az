from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Rates")


@_attrs_define
class Rates:
    """Statistics on the data processed by the backup policy.

    Attributes:
        total_data_bytes (int | Unset): Total size of all protected items.
        read_data_bytes (int | Unset): Amount of the read data (in bytes).
        processed_data_bytes (int | Unset): Amount of the processed data (in bytes).
        transferred_data_bytes (int | Unset): Amount of the transferred data (in bytes).
        processing_rate_bytes_per_second (int | Unset): Amount of processed data per second.
    """

    total_data_bytes: int | Unset = UNSET
    read_data_bytes: int | Unset = UNSET
    processed_data_bytes: int | Unset = UNSET
    transferred_data_bytes: int | Unset = UNSET
    processing_rate_bytes_per_second: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_data_bytes = self.total_data_bytes

        read_data_bytes = self.read_data_bytes

        processed_data_bytes = self.processed_data_bytes

        transferred_data_bytes = self.transferred_data_bytes

        processing_rate_bytes_per_second = self.processing_rate_bytes_per_second

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_data_bytes is not UNSET:
            field_dict["totalDataBytes"] = total_data_bytes
        if read_data_bytes is not UNSET:
            field_dict["readDataBytes"] = read_data_bytes
        if processed_data_bytes is not UNSET:
            field_dict["processedDataBytes"] = processed_data_bytes
        if transferred_data_bytes is not UNSET:
            field_dict["transferredDataBytes"] = transferred_data_bytes
        if processing_rate_bytes_per_second is not UNSET:
            field_dict["processingRateBytesPerSecond"] = processing_rate_bytes_per_second

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_data_bytes = d.pop("totalDataBytes", UNSET)

        read_data_bytes = d.pop("readDataBytes", UNSET)

        processed_data_bytes = d.pop("processedDataBytes", UNSET)

        transferred_data_bytes = d.pop("transferredDataBytes", UNSET)

        processing_rate_bytes_per_second = d.pop("processingRateBytesPerSecond", UNSET)

        rates = cls(
            total_data_bytes=total_data_bytes,
            read_data_bytes=read_data_bytes,
            processed_data_bytes=processed_data_bytes,
            transferred_data_bytes=transferred_data_bytes,
            processing_rate_bytes_per_second=processing_rate_bytes_per_second,
        )

        return rates
