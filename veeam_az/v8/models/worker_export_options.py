from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerExportOptions")


@_attrs_define
class WorkerExportOptions:
    """
    Attributes:
        vm_names (list[str] | None | Unset): Specifies the Azure VM names of worker instances whose details will be
            exported.
    """

    vm_names: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        vm_names: list[str] | None | Unset
        if isinstance(self.vm_names, Unset):
            vm_names = UNSET
        elif isinstance(self.vm_names, list):
            vm_names = self.vm_names

        else:
            vm_names = self.vm_names

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if vm_names is not UNSET:
            field_dict["vmNames"] = vm_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_vm_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                vm_names_type_0 = cast(list[str], data)

                return vm_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        vm_names = _parse_vm_names(d.pop("vmNames", UNSET))

        worker_export_options = cls(
            vm_names=vm_names,
        )

        return worker_export_options
