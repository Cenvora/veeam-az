from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationBackupExportRequest")


@_attrs_define
class ConfigurationBackupExportRequest:
    """
    Attributes:
        restore_point_id (UUID): System ID assigned in the Veeam backup for Microsoft Azure REST API to a restore point
            where the configuration backup file will be exported.
        password (str): Specifies a password that will be used for configuration backup export.
        password_hint (str | Unset): Specifies a hint to the password.
    """

    restore_point_id: UUID
    password: str
    password_hint: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_id = str(self.restore_point_id)

        password = self.password

        password_hint = self.password_hint

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "restorePointId": restore_point_id,
                "password": password,
            }
        )
        if password_hint is not UNSET:
            field_dict["passwordHint"] = password_hint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restore_point_id = UUID(d.pop("restorePointId"))

        password = d.pop("password")

        password_hint = d.pop("passwordHint", UNSET)

        configuration_backup_export_request = cls(
            restore_point_id=restore_point_id,
            password=password,
            password_hint=password_hint,
        )

        return configuration_backup_export_request
