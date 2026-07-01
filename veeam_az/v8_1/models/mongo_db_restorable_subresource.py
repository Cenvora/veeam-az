from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mongo_db_throughput_settings import MongoDbThroughputSettings


T = TypeVar("T", bound="MongoDbRestorableSubresource")


@_attrs_define
class MongoDbRestorableSubresource:
    """Specifies information on the database collection.

    Attributes:
        name (str | Unset): Specifies the name of the database collection.
        throughput_settings (MongoDbThroughputSettings | Unset):
    """

    name: str | Unset = UNSET
    throughput_settings: MongoDbThroughputSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        throughput_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.throughput_settings, Unset):
            throughput_settings = self.throughput_settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if throughput_settings is not UNSET:
            field_dict["throughputSettings"] = throughput_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mongo_db_throughput_settings import MongoDbThroughputSettings

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _throughput_settings = d.pop("throughputSettings", UNSET)
        throughput_settings: MongoDbThroughputSettings | Unset
        if isinstance(_throughput_settings, Unset):
            throughput_settings = UNSET
        else:
            throughput_settings = MongoDbThroughputSettings.from_dict(_throughput_settings)

        mongo_db_restorable_subresource = cls(
            name=name,
            throughput_settings=throughput_settings,
        )

        return mongo_db_restorable_subresource
