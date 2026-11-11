from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="ValidateDeleteBackupResponseRestorePoint")


@_attrs_define
class ValidateDeleteBackupResponseRestorePoint:
    """
    Attributes:
        restore_point_id (str):
        backup_id (str):
        repository_id (str):
        immutable_till (datetime.datetime):
    """

    restore_point_id: str
    backup_id: str
    repository_id: str
    immutable_till: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        restore_point_id = self.restore_point_id

        backup_id = self.backup_id

        repository_id = self.repository_id

        immutable_till = self.immutable_till.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "restorePointId": restore_point_id,
                "backupId": backup_id,
                "repositoryId": repository_id,
                "immutableTill": immutable_till,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restore_point_id = d.pop("restorePointId")

        backup_id = d.pop("backupId")

        repository_id = d.pop("repositoryId")

        immutable_till = isoparse(d.pop("immutableTill"))

        validate_delete_backup_response_restore_point = cls(
            restore_point_id=restore_point_id,
            backup_id=backup_id,
            repository_id=repository_id,
            immutable_till=immutable_till,
        )

        return validate_delete_backup_response_restore_point
