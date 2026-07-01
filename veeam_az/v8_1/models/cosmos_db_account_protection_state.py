from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CosmosDbAccountProtectionState")


@_attrs_define
class CosmosDbAccountProtectionState:
    """
    Attributes:
        restore_point_count (int | Unset):
        last_backup (datetime.datetime | None | Unset):
        has_vb_owned_restore_points (bool | Unset):
        has_continuous_restore_points (bool | Unset):
        policy_ids (list[UUID] | None | Unset):
    """

    restore_point_count: int | Unset = UNSET
    last_backup: datetime.datetime | None | Unset = UNSET
    has_vb_owned_restore_points: bool | Unset = UNSET
    has_continuous_restore_points: bool | Unset = UNSET
    policy_ids: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_count = self.restore_point_count

        last_backup: None | str | Unset
        if isinstance(self.last_backup, Unset):
            last_backup = UNSET
        elif isinstance(self.last_backup, datetime.datetime):
            last_backup = self.last_backup.isoformat()
        else:
            last_backup = self.last_backup

        has_vb_owned_restore_points = self.has_vb_owned_restore_points

        has_continuous_restore_points = self.has_continuous_restore_points

        policy_ids: list[str] | None | Unset
        if isinstance(self.policy_ids, Unset):
            policy_ids = UNSET
        elif isinstance(self.policy_ids, list):
            policy_ids = []
            for policy_ids_type_0_item_data in self.policy_ids:
                policy_ids_type_0_item = str(policy_ids_type_0_item_data)
                policy_ids.append(policy_ids_type_0_item)

        else:
            policy_ids = self.policy_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restore_point_count is not UNSET:
            field_dict["restorePointCount"] = restore_point_count
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup
        if has_vb_owned_restore_points is not UNSET:
            field_dict["hasVbOwnedRestorePoints"] = has_vb_owned_restore_points
        if has_continuous_restore_points is not UNSET:
            field_dict["hasContinuousRestorePoints"] = has_continuous_restore_points
        if policy_ids is not UNSET:
            field_dict["policyIds"] = policy_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restore_point_count = d.pop("restorePointCount", UNSET)

        def _parse_last_backup(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_type_0 = isoparse(data)

                return last_backup_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_backup = _parse_last_backup(d.pop("lastBackup", UNSET))

        has_vb_owned_restore_points = d.pop("hasVbOwnedRestorePoints", UNSET)

        has_continuous_restore_points = d.pop("hasContinuousRestorePoints", UNSET)

        def _parse_policy_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policy_ids_type_0 = []
                _policy_ids_type_0 = data
                for policy_ids_type_0_item_data in _policy_ids_type_0:
                    policy_ids_type_0_item = UUID(policy_ids_type_0_item_data)

                    policy_ids_type_0.append(policy_ids_type_0_item)

                return policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        policy_ids = _parse_policy_ids(d.pop("policyIds", UNSET))

        cosmos_db_account_protection_state = cls(
            restore_point_count=restore_point_count,
            last_backup=last_backup,
            has_vb_owned_restore_points=has_vb_owned_restore_points,
            has_continuous_restore_points=has_continuous_restore_points,
            policy_ids=policy_ids,
        )

        return cosmos_db_account_protection_state
