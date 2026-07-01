from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileLevelRestoredItem")


@_attrs_define
class FileLevelRestoredItem:
    """Information on each recovered file.

    Attributes:
        file_path (None | str | Unset): Path to the directory where the recovered file will be stored.
        virtual_machine_name (None | str | Unset): Name of the Azure VM added to the Fie-Level restore policy.
        resource_group_name (None | str | Unset): Name of a resource group where the restored Azure VM belongs.
        region_name (None | str | Unset): Name of the Azure region where the restored Azure VM resides.
    """

    file_path: None | str | Unset = UNSET
    virtual_machine_name: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_path: None | str | Unset
        if isinstance(self.file_path, Unset):
            file_path = UNSET
        else:
            file_path = self.file_path

        virtual_machine_name: None | str | Unset
        if isinstance(self.virtual_machine_name, Unset):
            virtual_machine_name = UNSET
        else:
            virtual_machine_name = self.virtual_machine_name

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_path is not UNSET:
            field_dict["filePath"] = file_path
        if virtual_machine_name is not UNSET:
            field_dict["virtualMachineName"] = virtual_machine_name
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if region_name is not UNSET:
            field_dict["regionName"] = region_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_path = _parse_file_path(d.pop("filePath", UNSET))

        def _parse_virtual_machine_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_machine_name = _parse_virtual_machine_name(d.pop("virtualMachineName", UNSET))

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        file_level_restored_item = cls(
            file_path=file_path,
            virtual_machine_name=virtual_machine_name,
            resource_group_name=resource_group_name,
            region_name=region_name,
        )

        return file_level_restored_item
