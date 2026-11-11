from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.file_share_backup_destination import FileShareBackupDestination
from ..models.protection_status import ProtectionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_share_policy_link import FileSharePolicyLink
    from ..models.file_share_restore_point_link import FileShareRestorePointLink


T = TypeVar("T", bound="FileShareProtectionState")


@_attrs_define
class FileShareProtectionState:
    """
    Attributes:
        protection_status (ProtectionStatus | Unset):
        destinations (list[FileShareBackupDestination] | None | Unset):
        policy_name (None | str | Unset):
        policies (list[FileSharePolicyLink] | None | Unset):
        restore_points (list[FileShareRestorePointLink] | None | Unset):
        has_vb_owned_restore_points (bool | Unset):
        restore_point_count (int | Unset):
        last_backup (datetime.datetime | None | Unset):
    """

    protection_status: ProtectionStatus | Unset = UNSET
    destinations: list[FileShareBackupDestination] | None | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    policies: list[FileSharePolicyLink] | None | Unset = UNSET
    restore_points: list[FileShareRestorePointLink] | None | Unset = UNSET
    has_vb_owned_restore_points: bool | Unset = UNSET
    restore_point_count: int | Unset = UNSET
    last_backup: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        protection_status: str | Unset = UNSET
        if not isinstance(self.protection_status, Unset):
            protection_status = self.protection_status.value

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

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        policies: list[dict[str, Any]] | None | Unset
        if isinstance(self.policies, Unset):
            policies = UNSET
        elif isinstance(self.policies, list):
            policies = []
            for policies_type_0_item_data in self.policies:
                policies_type_0_item = policies_type_0_item_data.to_dict()
                policies.append(policies_type_0_item)

        else:
            policies = self.policies

        restore_points: list[dict[str, Any]] | None | Unset
        if isinstance(self.restore_points, Unset):
            restore_points = UNSET
        elif isinstance(self.restore_points, list):
            restore_points = []
            for restore_points_type_0_item_data in self.restore_points:
                restore_points_type_0_item = restore_points_type_0_item_data.to_dict()
                restore_points.append(restore_points_type_0_item)

        else:
            restore_points = self.restore_points

        has_vb_owned_restore_points = self.has_vb_owned_restore_points

        restore_point_count = self.restore_point_count

        last_backup: None | str | Unset
        if isinstance(self.last_backup, Unset):
            last_backup = UNSET
        elif isinstance(self.last_backup, datetime.datetime):
            last_backup = self.last_backup.isoformat()
        else:
            last_backup = self.last_backup

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if protection_status is not UNSET:
            field_dict["protectionStatus"] = protection_status
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if policies is not UNSET:
            field_dict["policies"] = policies
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if has_vb_owned_restore_points is not UNSET:
            field_dict["hasVbOwnedRestorePoints"] = has_vb_owned_restore_points
        if restore_point_count is not UNSET:
            field_dict["restorePointCount"] = restore_point_count
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_share_policy_link import FileSharePolicyLink
        from ..models.file_share_restore_point_link import FileShareRestorePointLink

        d = dict(src_dict)
        _protection_status = d.pop("protectionStatus", UNSET)
        protection_status: ProtectionStatus | Unset
        if isinstance(_protection_status, Unset):
            protection_status = UNSET
        else:
            protection_status = ProtectionStatus(_protection_status)

        def _parse_destinations(data: object) -> list[FileShareBackupDestination] | None | Unset:
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
                    destinations_type_0_item = FileShareBackupDestination(destinations_type_0_item_data)

                    destinations_type_0.append(destinations_type_0_item)

                return destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileShareBackupDestination] | None | Unset, data)

        destinations = _parse_destinations(d.pop("destinations", UNSET))

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        def _parse_policies(data: object) -> list[FileSharePolicyLink] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policies_type_0 = []
                _policies_type_0 = data
                for policies_type_0_item_data in _policies_type_0:
                    policies_type_0_item = FileSharePolicyLink.from_dict(policies_type_0_item_data)

                    policies_type_0.append(policies_type_0_item)

                return policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileSharePolicyLink] | None | Unset, data)

        policies = _parse_policies(d.pop("policies", UNSET))

        def _parse_restore_points(data: object) -> list[FileShareRestorePointLink] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                restore_points_type_0 = []
                _restore_points_type_0 = data
                for restore_points_type_0_item_data in _restore_points_type_0:
                    restore_points_type_0_item = FileShareRestorePointLink.from_dict(restore_points_type_0_item_data)

                    restore_points_type_0.append(restore_points_type_0_item)

                return restore_points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileShareRestorePointLink] | None | Unset, data)

        restore_points = _parse_restore_points(d.pop("restorePoints", UNSET))

        has_vb_owned_restore_points = d.pop("hasVbOwnedRestorePoints", UNSET)

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

        file_share_protection_state = cls(
            protection_status=protection_status,
            destinations=destinations,
            policy_name=policy_name,
            policies=policies,
            restore_points=restore_points,
            has_vb_owned_restore_points=has_vb_owned_restore_points,
            restore_point_count=restore_point_count,
            last_backup=last_backup,
        )

        return file_share_protection_state
