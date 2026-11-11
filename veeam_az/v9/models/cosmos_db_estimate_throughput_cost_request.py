from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mongo_db_estimate_throughput_cost_settings import MongoDbEstimateThroughputCostSettings


T = TypeVar("T", bound="CosmosDbEstimateThroughputCostRequest")


@_attrs_define
class CosmosDbEstimateThroughputCostRequest:
    """
    Attributes:
        mongo_db_settings (MongoDbEstimateThroughputCostSettings | Unset):
    """

    mongo_db_settings: MongoDbEstimateThroughputCostSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mongo_db_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mongo_db_settings, Unset):
            mongo_db_settings = self.mongo_db_settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mongo_db_settings is not UNSET:
            field_dict["mongoDbSettings"] = mongo_db_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mongo_db_estimate_throughput_cost_settings import MongoDbEstimateThroughputCostSettings

        d = dict(src_dict)
        _mongo_db_settings = d.pop("mongoDbSettings", UNSET)
        mongo_db_settings: MongoDbEstimateThroughputCostSettings | Unset
        if isinstance(_mongo_db_settings, Unset):
            mongo_db_settings = UNSET
        else:
            mongo_db_settings = MongoDbEstimateThroughputCostSettings.from_dict(_mongo_db_settings)

        cosmos_db_estimate_throughput_cost_request = cls(
            mongo_db_settings=mongo_db_settings,
        )

        return cosmos_db_estimate_throughput_cost_request
