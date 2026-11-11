from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseExportOptions")


@_attrs_define
class LicenseExportOptions:
    """
    Attributes:
        licensed_resource_ids (list[UUID] | None | Unset): Specifies a list of system IDs assigned in the Veeam Backup
            for Microsoft Azure REST API to the license units consumed by Azure resources.
    """

    licensed_resource_ids: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        licensed_resource_ids: list[str] | None | Unset
        if isinstance(self.licensed_resource_ids, Unset):
            licensed_resource_ids = UNSET
        elif isinstance(self.licensed_resource_ids, list):
            licensed_resource_ids = []
            for licensed_resource_ids_type_0_item_data in self.licensed_resource_ids:
                licensed_resource_ids_type_0_item = str(licensed_resource_ids_type_0_item_data)
                licensed_resource_ids.append(licensed_resource_ids_type_0_item)

        else:
            licensed_resource_ids = self.licensed_resource_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if licensed_resource_ids is not UNSET:
            field_dict["licensedResourceIds"] = licensed_resource_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_licensed_resource_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                licensed_resource_ids_type_0 = []
                _licensed_resource_ids_type_0 = data
                for licensed_resource_ids_type_0_item_data in _licensed_resource_ids_type_0:
                    licensed_resource_ids_type_0_item = UUID(licensed_resource_ids_type_0_item_data)

                    licensed_resource_ids_type_0.append(licensed_resource_ids_type_0_item)

                return licensed_resource_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        licensed_resource_ids = _parse_licensed_resource_ids(d.pop("licensedResourceIds", UNSET))

        license_export_options = cls(
            licensed_resource_ids=licensed_resource_ids,
        )

        return license_export_options
