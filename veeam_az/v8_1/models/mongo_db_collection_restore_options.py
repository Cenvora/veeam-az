from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mongo_db_throughput_settings import MongoDbThroughputSettings


T = TypeVar("T", bound="MongoDbCollectionRestoreOptions")


@_attrs_define
class MongoDbCollectionRestoreOptions:
    """
    Attributes:
        name (str | Unset):
        new_name (None | str | Unset):
        throughput_settings (MongoDbThroughputSettings | Unset):
    """

    name: str | Unset = UNSET
    new_name: None | str | Unset = UNSET
    throughput_settings: MongoDbThroughputSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        new_name: None | str | Unset
        if isinstance(self.new_name, Unset):
            new_name = UNSET
        else:
            new_name = self.new_name

        throughput_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.throughput_settings, Unset):
            throughput_settings = self.throughput_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if new_name is not UNSET:
            field_dict["NewName"] = new_name
        if throughput_settings is not UNSET:
            field_dict["ThroughputSettings"] = throughput_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mongo_db_throughput_settings import MongoDbThroughputSettings

        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        def _parse_new_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_name = _parse_new_name(d.pop("NewName", UNSET))

        _throughput_settings = d.pop("ThroughputSettings", UNSET)
        throughput_settings: MongoDbThroughputSettings | Unset
        if isinstance(_throughput_settings, Unset):
            throughput_settings = UNSET
        else:
            throughput_settings = MongoDbThroughputSettings.from_dict(_throughput_settings)

        mongo_db_collection_restore_options = cls(
            name=name,
            new_name=new_name,
            throughput_settings=throughput_settings,
        )

        mongo_db_collection_restore_options.additional_properties = d
        return mongo_db_collection_restore_options

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
