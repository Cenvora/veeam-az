from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerConfigurationDeletionResult")


@_attrs_define
class WorkerConfigurationDeletionResult:
    """
    Attributes:
        busy_workers_exists (bool | Unset):
        remaining_network_interface_ids (list[str] | None | Unset):
        deletion_successfull (bool | Unset):
        virtual_network_name (None | str | Unset):
    """

    busy_workers_exists: bool | Unset = UNSET
    remaining_network_interface_ids: list[str] | None | Unset = UNSET
    deletion_successfull: bool | Unset = UNSET
    virtual_network_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        busy_workers_exists = self.busy_workers_exists

        remaining_network_interface_ids: list[str] | None | Unset
        if isinstance(self.remaining_network_interface_ids, Unset):
            remaining_network_interface_ids = UNSET
        elif isinstance(self.remaining_network_interface_ids, list):
            remaining_network_interface_ids = self.remaining_network_interface_ids

        else:
            remaining_network_interface_ids = self.remaining_network_interface_ids

        deletion_successfull = self.deletion_successfull

        virtual_network_name: None | str | Unset
        if isinstance(self.virtual_network_name, Unset):
            virtual_network_name = UNSET
        else:
            virtual_network_name = self.virtual_network_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if busy_workers_exists is not UNSET:
            field_dict["busyWorkersExists"] = busy_workers_exists
        if remaining_network_interface_ids is not UNSET:
            field_dict["remainingNetworkInterfaceIds"] = remaining_network_interface_ids
        if deletion_successfull is not UNSET:
            field_dict["deletionSuccessfull"] = deletion_successfull
        if virtual_network_name is not UNSET:
            field_dict["virtualNetworkName"] = virtual_network_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        busy_workers_exists = d.pop("busyWorkersExists", UNSET)

        def _parse_remaining_network_interface_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                remaining_network_interface_ids_type_0 = cast(list[str], data)

                return remaining_network_interface_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        remaining_network_interface_ids = _parse_remaining_network_interface_ids(
            d.pop("remainingNetworkInterfaceIds", UNSET)
        )

        deletion_successfull = d.pop("deletionSuccessfull", UNSET)

        def _parse_virtual_network_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_network_name = _parse_virtual_network_name(d.pop("virtualNetworkName", UNSET))

        worker_configuration_deletion_result = cls(
            busy_workers_exists=busy_workers_exists,
            remaining_network_interface_ids=remaining_network_interface_ids,
            deletion_successfull=deletion_successfull,
            virtual_network_name=virtual_network_name,
        )

        return worker_configuration_deletion_result
