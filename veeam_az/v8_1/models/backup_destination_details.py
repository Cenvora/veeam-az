from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.backup_destination import BackupDestination
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupDestinationDetails")


@_attrs_define
class BackupDestinationDetails:
    """
    Attributes:
        destinations (list[BackupDestination] | None | Unset):
        repositories (list[str] | None | Unset):
    """

    destinations: list[BackupDestination] | None | Unset = UNSET
    repositories: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        repositories: list[str] | None | Unset
        if isinstance(self.repositories, Unset):
            repositories = UNSET
        elif isinstance(self.repositories, list):
            repositories = self.repositories

        else:
            repositories = self.repositories

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if repositories is not UNSET:
            field_dict["repositories"] = repositories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_repositories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repositories_type_0 = cast(list[str], data)

                return repositories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        repositories = _parse_repositories(d.pop("repositories", UNSET))

        backup_destination_details = cls(
            destinations=destinations,
            repositories=repositories,
        )

        return backup_destination_details
