from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.data_retrieval_status import DataRetrievalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_backup_destination_with_tier import SqlBackupDestinationWithTier


T = TypeVar("T", bound="ProtectionDatabaseState")


@_attrs_define
class ProtectionDatabaseState:
    """
    Attributes:
        restore_point_count (int):
        data_retrieval_status (DataRetrievalStatus): State of the data retrieval process.
        destinations (list[SqlBackupDestinationWithTier] | None | Unset):
    """

    restore_point_count: int
    data_retrieval_status: DataRetrievalStatus
    destinations: list[SqlBackupDestinationWithTier] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_count = self.restore_point_count

        data_retrieval_status = self.data_retrieval_status.value

        destinations: list[dict[str, Any]] | None | Unset
        if isinstance(self.destinations, Unset):
            destinations = UNSET
        elif isinstance(self.destinations, list):
            destinations = []
            for destinations_type_0_item_data in self.destinations:
                destinations_type_0_item = destinations_type_0_item_data.to_dict()
                destinations.append(destinations_type_0_item)

        else:
            destinations = self.destinations

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "restorePointCount": restore_point_count,
                "dataRetrievalStatus": data_retrieval_status,
            }
        )
        if destinations is not UNSET:
            field_dict["destinations"] = destinations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sql_backup_destination_with_tier import SqlBackupDestinationWithTier

        d = dict(src_dict)
        restore_point_count = d.pop("restorePointCount")

        data_retrieval_status = DataRetrievalStatus(d.pop("dataRetrievalStatus"))

        def _parse_destinations(data: object) -> list[SqlBackupDestinationWithTier] | None | Unset:
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
                    destinations_type_0_item = SqlBackupDestinationWithTier.from_dict(destinations_type_0_item_data)

                    destinations_type_0.append(destinations_type_0_item)

                return destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SqlBackupDestinationWithTier] | None | Unset, data)

        destinations = _parse_destinations(d.pop("destinations", UNSET))

        protection_database_state = cls(
            restore_point_count=restore_point_count,
            data_retrieval_status=data_retrieval_status,
            destinations=destinations,
        )

        return protection_database_state
