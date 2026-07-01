from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerNetworkConfigurationExportOptions")


@_attrs_define
class WorkerNetworkConfigurationExportOptions:
    """
    Attributes:
        region_ids (list[str] | None | Unset): Specifies Azure IDs assigned to regions for which the worker
            configurations will be exported.
    """

    region_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        region_ids: list[str] | None | Unset
        if isinstance(self.region_ids, Unset):
            region_ids = UNSET
        elif isinstance(self.region_ids, list):
            region_ids = self.region_ids

        else:
            region_ids = self.region_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if region_ids is not UNSET:
            field_dict["regionIds"] = region_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_region_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                region_ids_type_0 = cast(list[str], data)

                return region_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        region_ids = _parse_region_ids(d.pop("regionIds", UNSET))

        worker_network_configuration_export_options = cls(
            region_ids=region_ids,
        )

        return worker_network_configuration_export_options
