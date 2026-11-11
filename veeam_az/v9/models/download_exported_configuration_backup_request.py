from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="DownloadExportedConfigurationBackupRequest")


@_attrs_define
class DownloadExportedConfigurationBackupRequest:
    """
    Attributes:
        session_id (UUID): System ID assigned in the Veeam backup for Microsoft Azure REST API to the configuration
            backup export session.
    """

    session_id: UUID

    def to_dict(self) -> dict[str, Any]:
        session_id = str(self.session_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sessionId": session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = UUID(d.pop("sessionId"))

        download_exported_configuration_backup_request = cls(
            session_id=session_id,
        )

        return download_exported_configuration_backup_request
