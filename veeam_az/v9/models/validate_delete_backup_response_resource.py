from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.protected_data_backup_tier_nullable import ProtectedDataBackupTierNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validate_delete_backup_response_restore_point import ValidateDeleteBackupResponseRestorePoint


T = TypeVar("T", bound="ValidateDeleteBackupResponseResource")


@_attrs_define
class ValidateDeleteBackupResponseResource:
    """
    Attributes:
        hash_id (str):
        resource_not_found (bool | None | Unset):
        restore_point_not_found (bool | None | Unset):
        disabled_backups (list[ProtectedDataBackupTierNullable] | None | Unset):
        immutable_restore_points (list[ValidateDeleteBackupResponseRestorePoint] | None | Unset):
    """

    hash_id: str
    resource_not_found: bool | None | Unset = UNSET
    restore_point_not_found: bool | None | Unset = UNSET
    disabled_backups: list[ProtectedDataBackupTierNullable] | None | Unset = UNSET
    immutable_restore_points: list[ValidateDeleteBackupResponseRestorePoint] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        hash_id = self.hash_id

        resource_not_found: bool | None | Unset
        if isinstance(self.resource_not_found, Unset):
            resource_not_found = UNSET
        else:
            resource_not_found = self.resource_not_found

        restore_point_not_found: bool | None | Unset
        if isinstance(self.restore_point_not_found, Unset):
            restore_point_not_found = UNSET
        else:
            restore_point_not_found = self.restore_point_not_found

        disabled_backups: list[str] | None | Unset
        if isinstance(self.disabled_backups, Unset):
            disabled_backups = UNSET
        elif isinstance(self.disabled_backups, list):
            disabled_backups = []
            for disabled_backups_type_0_item_data in self.disabled_backups:
                disabled_backups_type_0_item = disabled_backups_type_0_item_data.value
                disabled_backups.append(disabled_backups_type_0_item)

        else:
            disabled_backups = self.disabled_backups

        immutable_restore_points: list[dict[str, Any]] | None | Unset
        if isinstance(self.immutable_restore_points, Unset):
            immutable_restore_points = UNSET
        elif isinstance(self.immutable_restore_points, list):
            immutable_restore_points = []
            for immutable_restore_points_type_0_item_data in self.immutable_restore_points:
                immutable_restore_points_type_0_item = immutable_restore_points_type_0_item_data.to_dict()
                immutable_restore_points.append(immutable_restore_points_type_0_item)

        else:
            immutable_restore_points = self.immutable_restore_points

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hashId": hash_id,
            }
        )
        if resource_not_found is not UNSET:
            field_dict["resourceNotFound"] = resource_not_found
        if restore_point_not_found is not UNSET:
            field_dict["restorePointNotFound"] = restore_point_not_found
        if disabled_backups is not UNSET:
            field_dict["disabledBackups"] = disabled_backups
        if immutable_restore_points is not UNSET:
            field_dict["immutableRestorePoints"] = immutable_restore_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validate_delete_backup_response_restore_point import ValidateDeleteBackupResponseRestorePoint

        d = dict(src_dict)
        hash_id = d.pop("hashId")

        def _parse_resource_not_found(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        resource_not_found = _parse_resource_not_found(d.pop("resourceNotFound", UNSET))

        def _parse_restore_point_not_found(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restore_point_not_found = _parse_restore_point_not_found(d.pop("restorePointNotFound", UNSET))

        def _parse_disabled_backups(data: object) -> list[ProtectedDataBackupTierNullable] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disabled_backups_type_0 = []
                _disabled_backups_type_0 = data
                for disabled_backups_type_0_item_data in _disabled_backups_type_0:
                    disabled_backups_type_0_item = ProtectedDataBackupTierNullable(disabled_backups_type_0_item_data)

                    disabled_backups_type_0.append(disabled_backups_type_0_item)

                return disabled_backups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProtectedDataBackupTierNullable] | None | Unset, data)

        disabled_backups = _parse_disabled_backups(d.pop("disabledBackups", UNSET))

        def _parse_immutable_restore_points(
            data: object,
        ) -> list[ValidateDeleteBackupResponseRestorePoint] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                immutable_restore_points_type_0 = []
                _immutable_restore_points_type_0 = data
                for immutable_restore_points_type_0_item_data in _immutable_restore_points_type_0:
                    immutable_restore_points_type_0_item = ValidateDeleteBackupResponseRestorePoint.from_dict(
                        immutable_restore_points_type_0_item_data
                    )

                    immutable_restore_points_type_0.append(immutable_restore_points_type_0_item)

                return immutable_restore_points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ValidateDeleteBackupResponseRestorePoint] | None | Unset, data)

        immutable_restore_points = _parse_immutable_restore_points(d.pop("immutableRestorePoints", UNSET))

        validate_delete_backup_response_resource = cls(
            hash_id=hash_id,
            resource_not_found=resource_not_found,
            restore_point_not_found=restore_point_not_found,
            disabled_backups=disabled_backups,
            immutable_restore_points=immutable_restore_points,
        )

        return validate_delete_backup_response_resource
