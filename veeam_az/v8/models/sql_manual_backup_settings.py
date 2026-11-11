from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlManualBackupSettings")


@_attrs_define
class SqlManualBackupSettings:
    """
    Attributes:
        database_ids (list[str]): Specifies the system IDs assigned to the Azure SQL databases in the Veeam Backup for
            Microsoft Azure REST API.
        repository_id (str): Specifies the system ID assigned to the target repository in the Veeam Backup for Microsoft
            Azure REST API.
        tenant_id (None | UUID): Specifies the Microsoft Azure ID assigned to the tenant associated with a service
            account whose permissions will be used to manage Azure SQL databases.
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            a service account whose permissions will be used to manage Azure SQL databases.
        managed_staging_server_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a staging server
            configured for the unmanaged instances.
        staging_server_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a staging server configured
            for the managed instances.
    """

    database_ids: list[str]
    repository_id: str
    tenant_id: None | UUID
    service_account_id: UUID
    managed_staging_server_id: None | str | Unset = UNSET
    staging_server_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        database_ids = self.database_ids

        repository_id = self.repository_id

        tenant_id: None | str
        if isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        service_account_id = str(self.service_account_id)

        managed_staging_server_id: None | str | Unset
        if isinstance(self.managed_staging_server_id, Unset):
            managed_staging_server_id = UNSET
        else:
            managed_staging_server_id = self.managed_staging_server_id

        staging_server_id: None | str | Unset
        if isinstance(self.staging_server_id, Unset):
            staging_server_id = UNSET
        else:
            staging_server_id = self.staging_server_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "databaseIds": database_ids,
                "repositoryId": repository_id,
                "tenantId": tenant_id,
                "serviceAccountId": service_account_id,
            }
        )
        if managed_staging_server_id is not UNSET:
            field_dict["managedStagingServerId"] = managed_staging_server_id
        if staging_server_id is not UNSET:
            field_dict["stagingServerId"] = staging_server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database_ids = cast(list[str], d.pop("databaseIds"))

        repository_id = d.pop("repositoryId")

        def _parse_tenant_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId"))

        service_account_id = UUID(d.pop("serviceAccountId"))

        def _parse_managed_staging_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_staging_server_id = _parse_managed_staging_server_id(d.pop("managedStagingServerId", UNSET))

        def _parse_staging_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        staging_server_id = _parse_staging_server_id(d.pop("stagingServerId", UNSET))

        sql_manual_backup_settings = cls(
            database_ids=database_ids,
            repository_id=repository_id,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            managed_staging_server_id=managed_staging_server_id,
            staging_server_id=staging_server_id,
        )

        return sql_manual_backup_settings
