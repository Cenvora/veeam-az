from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.sql_backup_destination import SqlBackupDestination
from ..models.storage_tier_nullable import StorageTierNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlBackupDestinationWithTier")


@_attrs_define
class SqlBackupDestinationWithTier:
    """
    Attributes:
        destination (SqlBackupDestination | Unset): Type of the backup destination.
        storage_tier (StorageTierNullable | Unset): Specifies the access tier.
    """

    destination: SqlBackupDestination | Unset = UNSET
    storage_tier: StorageTierNullable | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        destination: str | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.value

        storage_tier: str | Unset = UNSET
        if not isinstance(self.storage_tier, Unset):
            storage_tier = self.storage_tier.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if storage_tier is not UNSET:
            field_dict["storageTier"] = storage_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _destination = d.pop("destination", UNSET)
        destination: SqlBackupDestination | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = SqlBackupDestination(_destination)

        _storage_tier = d.pop("storageTier", UNSET)
        storage_tier: StorageTierNullable | Unset
        if isinstance(_storage_tier, Unset):
            storage_tier = UNSET
        else:
            storage_tier = StorageTierNullable(_storage_tier)

        sql_backup_destination_with_tier = cls(
            destination=destination,
            storage_tier=storage_tier,
        )

        return sql_backup_destination_with_tier
