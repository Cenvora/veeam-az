from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.price import Price


T = TypeVar("T", bound="VmSize")


@_attrs_define
class VmSize:
    """
    Attributes:
        name (None | str | Unset): Name of the Azure VM size with predefined configuration options.
        subscription_id (None | str | Unset): Microsoft Azure ID assigned to the subscription for which the Azure VM
            size is available.
        max_data_disk_count (int | Unset): Maximum number of data disks available for the Azure VM size.
        memory_in_mb (int | Unset): Memory available for the Azure VM size (in MB).
        number_of_cores (int | Unset): Number of cores for the Azure VM size.
        os_disk_size_in_mb (int | Unset): Maximum capacity of an OS disk for the Azure VM size (in MB).
        resource_disk_size_in_mb (int | Unset): Capacity of a resource disk for the Azure VM size (in MB).
        price_per_hour (Price | Unset): Information on the price per hour for the Azure VM size.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    name: None | str | Unset = UNSET
    subscription_id: None | str | Unset = UNSET
    max_data_disk_count: int | Unset = UNSET
    memory_in_mb: int | Unset = UNSET
    number_of_cores: int | Unset = UNSET
    os_disk_size_in_mb: int | Unset = UNSET
    resource_disk_size_in_mb: int | Unset = UNSET
    price_per_hour: Price | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = self.subscription_id

        max_data_disk_count = self.max_data_disk_count

        memory_in_mb = self.memory_in_mb

        number_of_cores = self.number_of_cores

        os_disk_size_in_mb = self.os_disk_size_in_mb

        resource_disk_size_in_mb = self.resource_disk_size_in_mb

        price_per_hour: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price_per_hour, Unset):
            price_per_hour = self.price_per_hour.to_dict()

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if max_data_disk_count is not UNSET:
            field_dict["maxDataDiskCount"] = max_data_disk_count
        if memory_in_mb is not UNSET:
            field_dict["memoryInMB"] = memory_in_mb
        if number_of_cores is not UNSET:
            field_dict["numberOfCores"] = number_of_cores
        if os_disk_size_in_mb is not UNSET:
            field_dict["osDiskSizeInMB"] = os_disk_size_in_mb
        if resource_disk_size_in_mb is not UNSET:
            field_dict["resourceDiskSizeInMB"] = resource_disk_size_in_mb
        if price_per_hour is not UNSET:
            field_dict["pricePerHour"] = price_per_hour
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.price import Price

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_subscription_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        max_data_disk_count = d.pop("maxDataDiskCount", UNSET)

        memory_in_mb = d.pop("memoryInMB", UNSET)

        number_of_cores = d.pop("numberOfCores", UNSET)

        os_disk_size_in_mb = d.pop("osDiskSizeInMB", UNSET)

        resource_disk_size_in_mb = d.pop("resourceDiskSizeInMB", UNSET)

        _price_per_hour = d.pop("pricePerHour", UNSET)
        price_per_hour: Price | Unset
        if isinstance(_price_per_hour, Unset):
            price_per_hour = UNSET
        else:
            price_per_hour = Price.from_dict(_price_per_hour)

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        vm_size = cls(
            name=name,
            subscription_id=subscription_id,
            max_data_disk_count=max_data_disk_count,
            memory_in_mb=memory_in_mb,
            number_of_cores=number_of_cores,
            os_disk_size_in_mb=os_disk_size_in_mb,
            resource_disk_size_in_mb=resource_disk_size_in_mb,
            price_per_hour=price_per_hour,
            field_links=field_links,
        )

        return vm_size
