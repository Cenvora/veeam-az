from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetConfigurationBackupExportStatus")


@_attrs_define
class GetConfigurationBackupExportStatus:
    """
    Attributes:
        is_ready_to_download (bool): Defines whether the configuration backup file is ready for download.
    """

    is_ready_to_download: bool

    def to_dict(self) -> dict[str, Any]:
        is_ready_to_download = self.is_ready_to_download

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isReadyToDownload": is_ready_to_download,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_ready_to_download = d.pop("isReadyToDownload")

        get_configuration_backup_export_status = cls(
            is_ready_to_download=is_ready_to_download,
        )

        return get_configuration_backup_export_status
