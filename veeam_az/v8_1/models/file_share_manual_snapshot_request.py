from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="FileShareManualSnapshotRequest")


@_attrs_define
class FileShareManualSnapshotRequest:
    """
    Attributes:
        file_share_ids (list[str]): Specifies system IDs assigned in the Veeam Backup for Microsoft Azure REST API to
            the Azure file shares whose snapshots will be created.
        tenant_id (UUID): Specifies a Microsoft Azure ID assigned to a tenant where snapshots will be created.
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            a service account whose permissions will be used to create snapshots of Azure file shares.
    """

    file_share_ids: list[str]
    tenant_id: UUID
    service_account_id: UUID

    def to_dict(self) -> dict[str, Any]:
        file_share_ids = self.file_share_ids

        tenant_id = str(self.tenant_id)

        service_account_id = str(self.service_account_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fileShareIds": file_share_ids,
                "tenantId": tenant_id,
                "serviceAccountId": service_account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_share_ids = cast(list[str], d.pop("fileShareIds"))

        tenant_id = UUID(d.pop("tenantId"))

        service_account_id = UUID(d.pop("serviceAccountId"))

        file_share_manual_snapshot_request = cls(
            file_share_ids=file_share_ids,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
        )

        return file_share_manual_snapshot_request
