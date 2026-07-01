from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mongo_db_restorable_subresource import MongoDbRestorableSubresource
    from ..models.mongo_db_throughput_settings import MongoDbThroughputSettings


T = TypeVar("T", bound="MongoDbRestorableResource")


@_attrs_define
class MongoDbRestorableResource:
    """Specifies information on MongoDB databases and collections that will be restored.

    Attributes:
        name (str | Unset): Specifies the name of a database or collection.
        collections (list[MongoDbRestorableSubresource] | None | Unset): Specifies a list of database collections.
        throughput_settings (MongoDbThroughputSettings | Unset):
    """

    name: str | Unset = UNSET
    collections: list[MongoDbRestorableSubresource] | None | Unset = UNSET
    throughput_settings: MongoDbThroughputSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        collections: list[dict[str, Any]] | None | Unset
        if isinstance(self.collections, Unset):
            collections = UNSET
        elif isinstance(self.collections, list):
            collections = []
            for collections_type_0_item_data in self.collections:
                collections_type_0_item = collections_type_0_item_data.to_dict()
                collections.append(collections_type_0_item)

        else:
            collections = self.collections

        throughput_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.throughput_settings, Unset):
            throughput_settings = self.throughput_settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if collections is not UNSET:
            field_dict["collections"] = collections
        if throughput_settings is not UNSET:
            field_dict["throughputSettings"] = throughput_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mongo_db_restorable_subresource import MongoDbRestorableSubresource
        from ..models.mongo_db_throughput_settings import MongoDbThroughputSettings

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_collections(data: object) -> list[MongoDbRestorableSubresource] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collections_type_0 = []
                _collections_type_0 = data
                for collections_type_0_item_data in _collections_type_0:
                    collections_type_0_item = MongoDbRestorableSubresource.from_dict(collections_type_0_item_data)

                    collections_type_0.append(collections_type_0_item)

                return collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MongoDbRestorableSubresource] | None | Unset, data)

        collections = _parse_collections(d.pop("collections", UNSET))

        _throughput_settings = d.pop("throughputSettings", UNSET)
        throughput_settings: MongoDbThroughputSettings | Unset
        if isinstance(_throughput_settings, Unset):
            throughput_settings = UNSET
        else:
            throughput_settings = MongoDbThroughputSettings.from_dict(_throughput_settings)

        mongo_db_restorable_resource = cls(
            name=name,
            collections=collections,
            throughput_settings=throughput_settings,
        )

        return mongo_db_restorable_resource
