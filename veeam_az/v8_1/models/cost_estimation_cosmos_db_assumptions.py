from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CostEstimationCosmosDbAssumptions")


@_attrs_define
class CostEstimationCosmosDbAssumptions:
    """Assumptions used to calculate the cost.

    Attributes:
        data_compression_ratio (float): Ratio between the uncompressed and compressed size.
    """

    data_compression_ratio: float

    def to_dict(self) -> dict[str, Any]:
        data_compression_ratio = self.data_compression_ratio

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dataCompressionRatio": data_compression_ratio,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_compression_ratio = d.pop("dataCompressionRatio")

        cost_estimation_cosmos_db_assumptions = cls(
            data_compression_ratio=data_compression_ratio,
        )

        return cost_estimation_cosmos_db_assumptions
