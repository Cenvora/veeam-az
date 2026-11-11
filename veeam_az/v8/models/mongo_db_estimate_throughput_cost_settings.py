from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.mongo_db_restorable_resource import MongoDbRestorableResource
    from ..models.mongo_db_throughput_settings import MongoDbThroughputSettings


T = TypeVar("T", bound="MongoDbEstimateThroughputCostSettings")


@_attrs_define
class MongoDbEstimateThroughputCostSettings:
    """
    Attributes:
        database_name (str):
        collection_name (str):
        throughput_settings (MongoDbThroughputSettings):
        databases (list[MongoDbRestorableResource]):
    """

    database_name: str
    collection_name: str
    throughput_settings: MongoDbThroughputSettings
    databases: list[MongoDbRestorableResource]

    def to_dict(self) -> dict[str, Any]:
        database_name = self.database_name

        collection_name = self.collection_name

        throughput_settings = self.throughput_settings.to_dict()

        databases = []
        for databases_item_data in self.databases:
            databases_item = databases_item_data.to_dict()
            databases.append(databases_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "databaseName": database_name,
                "collectionName": collection_name,
                "throughputSettings": throughput_settings,
                "databases": databases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mongo_db_restorable_resource import MongoDbRestorableResource
        from ..models.mongo_db_throughput_settings import MongoDbThroughputSettings

        d = dict(src_dict)
        database_name = d.pop("databaseName")

        collection_name = d.pop("collectionName")

        throughput_settings = MongoDbThroughputSettings.from_dict(d.pop("throughputSettings"))

        databases = []
        _databases = d.pop("databases")
        for databases_item_data in _databases:
            databases_item = MongoDbRestorableResource.from_dict(databases_item_data)

            databases.append(databases_item)

        mongo_db_estimate_throughput_cost_settings = cls(
            database_name=database_name,
            collection_name=collection_name,
            throughput_settings=throughput_settings,
            databases=databases,
        )

        return mongo_db_estimate_throughput_cost_settings
