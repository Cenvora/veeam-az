from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileShareRestorePointIndexingConfig")


@_attrs_define
class FileShareRestorePointIndexingConfig:
    """Specifies the settings to perform indexing.

    Attributes:
        restore_point_ids (list[str]): Specifies a comma-separated list of system IDs assigned in the Veeam Backup for
            Microsoft Azure REST API to restore points for which indexing will be performed.
        service_account_id (str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST
            API to a service account whose permissions will be used to perform indexing.
    """

    restore_point_ids: list[str]
    service_account_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_ids = self.restore_point_ids

        service_account_id = self.service_account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "restorePointIds": restore_point_ids,
            }
        )
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restore_point_ids = cast(list[str], d.pop("restorePointIds"))

        service_account_id = d.pop("serviceAccountId", UNSET)

        file_share_restore_point_indexing_config = cls(
            restore_point_ids=restore_point_ids,
            service_account_id=service_account_id,
        )

        return file_share_restore_point_indexing_config
