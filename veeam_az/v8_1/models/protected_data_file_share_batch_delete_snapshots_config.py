from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProtectedDataFileShareBatchDeleteSnapshotsConfig")


@_attrs_define
class ProtectedDataFileShareBatchDeleteSnapshotsConfig:
    """Information on the snapshots that will be removed.

    Attributes:
        ids (list[str]): Specifies a comma-separated list of internal IDs assigned in the Veeam Backup for Microsoft
            Azure REST API to Azure FileShares whose snapshots will be removed.
    """

    ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ids": ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        protected_data_file_share_batch_delete_snapshots_config = cls(
            ids=ids,
        )

        return protected_data_file_share_batch_delete_snapshots_config
