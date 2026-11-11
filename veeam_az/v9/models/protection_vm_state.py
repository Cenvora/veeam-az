from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.backup_destination import BackupDestination
from ..models.data_retrieval_status import DataRetrievalStatus
from ..models.storage_tier_nullable import StorageTierNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionVMState")


@_attrs_define
class ProtectionVMState:
    """
    Attributes:
        restore_point_count (int):
        data_retrieval_status (DataRetrievalStatus): State of the data retrieval process.
        destinations (list[BackupDestination] | None | Unset):
        storage_tiers (list[StorageTierNullable] | None | Unset):
    """

    restore_point_count: int
    data_retrieval_status: DataRetrievalStatus
    destinations: list[BackupDestination] | None | Unset = UNSET
    storage_tiers: list[StorageTierNullable] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_count = self.restore_point_count

        data_retrieval_status = self.data_retrieval_status.value

        destinations: list[str] | None | Unset
        if isinstance(self.destinations, Unset):
            destinations = UNSET
        elif isinstance(self.destinations, list):
            destinations = []
            for destinations_type_0_item_data in self.destinations:
                destinations_type_0_item = destinations_type_0_item_data.value
                destinations.append(destinations_type_0_item)

        else:
            destinations = self.destinations

        storage_tiers: list[str] | None | Unset
        if isinstance(self.storage_tiers, Unset):
            storage_tiers = UNSET
        elif isinstance(self.storage_tiers, list):
            storage_tiers = []
            for storage_tiers_type_0_item_data in self.storage_tiers:
                storage_tiers_type_0_item = storage_tiers_type_0_item_data.value
                storage_tiers.append(storage_tiers_type_0_item)

        else:
            storage_tiers = self.storage_tiers

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "restorePointCount": restore_point_count,
                "dataRetrievalStatus": data_retrieval_status,
            }
        )
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if storage_tiers is not UNSET:
            field_dict["storageTiers"] = storage_tiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restore_point_count = d.pop("restorePointCount")

        data_retrieval_status = DataRetrievalStatus(d.pop("dataRetrievalStatus"))

        def _parse_destinations(data: object) -> list[BackupDestination] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                destinations_type_0 = []
                _destinations_type_0 = data
                for destinations_type_0_item_data in _destinations_type_0:
                    destinations_type_0_item = BackupDestination(destinations_type_0_item_data)

                    destinations_type_0.append(destinations_type_0_item)

                return destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BackupDestination] | None | Unset, data)

        destinations = _parse_destinations(d.pop("destinations", UNSET))

        def _parse_storage_tiers(data: object) -> list[StorageTierNullable] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                storage_tiers_type_0 = []
                _storage_tiers_type_0 = data
                for storage_tiers_type_0_item_data in _storage_tiers_type_0:
                    storage_tiers_type_0_item = StorageTierNullable(storage_tiers_type_0_item_data)

                    storage_tiers_type_0.append(storage_tiers_type_0_item)

                return storage_tiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StorageTierNullable] | None | Unset, data)

        storage_tiers = _parse_storage_tiers(d.pop("storageTiers", UNSET))

        protection_vm_state = cls(
            restore_point_count=restore_point_count,
            data_retrieval_status=data_retrieval_status,
            destinations=destinations,
            storage_tiers=storage_tiers,
        )

        return protection_vm_state
