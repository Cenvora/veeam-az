from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.protection_status import ProtectionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_destination_details import BackupDestinationDetails
    from ..models.policy_link import PolicyLink


T = TypeVar("T", bound="ProtectionState")


@_attrs_define
class ProtectionState:
    """
    Attributes:
        protection_status (ProtectionStatus | Unset):
        backup_destination_details (BackupDestinationDetails | Unset):
        policy_name (None | str | Unset):
        policies (list[PolicyLink] | None | Unset):
        restore_point_count (int | Unset):
        has_vb_owned_restore_points (bool | Unset):
        last_backup (datetime.datetime | None | Unset):
    """

    protection_status: ProtectionStatus | Unset = UNSET
    backup_destination_details: BackupDestinationDetails | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    policies: list[PolicyLink] | None | Unset = UNSET
    restore_point_count: int | Unset = UNSET
    has_vb_owned_restore_points: bool | Unset = UNSET
    last_backup: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        protection_status: str | Unset = UNSET
        if not isinstance(self.protection_status, Unset):
            protection_status = self.protection_status.value

        backup_destination_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_destination_details, Unset):
            backup_destination_details = self.backup_destination_details.to_dict()

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

        restore_point_count = self.restore_point_count

        has_vb_owned_restore_points = self.has_vb_owned_restore_points

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
        if backup_destination_details is not UNSET:
            field_dict["backupDestinationDetails"] = backup_destination_details
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if policies is not UNSET:
            field_dict["policies"] = policies
        if restore_point_count is not UNSET:
            field_dict["restorePointCount"] = restore_point_count
        if has_vb_owned_restore_points is not UNSET:
            field_dict["hasVbOwnedRestorePoints"] = has_vb_owned_restore_points
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_destination_details import BackupDestinationDetails
        from ..models.policy_link import PolicyLink

        d = dict(src_dict)
        _protection_status = d.pop("protectionStatus", UNSET)
        protection_status: ProtectionStatus | Unset
        if isinstance(_protection_status, Unset):
            protection_status = UNSET
        else:
            protection_status = ProtectionStatus(_protection_status)

        _backup_destination_details = d.pop("backupDestinationDetails", UNSET)
        backup_destination_details: BackupDestinationDetails | Unset
        if isinstance(_backup_destination_details, Unset):
            backup_destination_details = UNSET
        else:
            backup_destination_details = BackupDestinationDetails.from_dict(_backup_destination_details)

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        def _parse_policies(data: object) -> list[PolicyLink] | None | Unset:
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
                    policies_type_0_item = PolicyLink.from_dict(policies_type_0_item_data)

                    policies_type_0.append(policies_type_0_item)

                return policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolicyLink] | None | Unset, data)

        policies = _parse_policies(d.pop("policies", UNSET))

        restore_point_count = d.pop("restorePointCount", UNSET)

        has_vb_owned_restore_points = d.pop("hasVbOwnedRestorePoints", UNSET)

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

        protection_state = cls(
            protection_status=protection_status,
            backup_destination_details=backup_destination_details,
            policy_name=policy_name,
            policies=policies,
            restore_point_count=restore_point_count,
            has_vb_owned_restore_points=has_vb_owned_restore_points,
            last_backup=last_backup,
        )

        return protection_state
