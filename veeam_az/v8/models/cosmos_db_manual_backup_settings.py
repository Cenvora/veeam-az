from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cosmos_db_processing_credentials_type_0 import CosmosDbProcessingCredentialsType0


T = TypeVar("T", bound="CosmosDbManualBackupSettings")


@_attrs_define
class CosmosDbManualBackupSettings:
    """
    Attributes:
        cosmos_db_account_ids (list[str]): Specifies Microsoft Azure IDs assigned to Cosmos DB accounts that will be
            backed up.
        repository_id (str): Specifies the system ID assigned to the target repository in the Veeam Backup for Microsoft
            Azure REST API.
        tenant_id (None | UUID): Specifies a Microsoft Azure ID assigned to a tenant to which the protected Cosmos DB
            accounts belong.
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to
            the service account whose permissions will be used to protect Cosmos DB accounts.
        credentials_list (CosmosDbProcessingCredentialsType0 | None | Unset): Specifies a list of credentials that will
            be used to connect to the databases of the specified Cosmos DB accounts.
    """

    cosmos_db_account_ids: list[str]
    repository_id: str
    tenant_id: None | UUID
    service_account_id: UUID
    credentials_list: CosmosDbProcessingCredentialsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cosmos_db_processing_credentials_type_0 import CosmosDbProcessingCredentialsType0

        cosmos_db_account_ids = self.cosmos_db_account_ids

        repository_id = self.repository_id

        tenant_id: None | str
        if isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        service_account_id = str(self.service_account_id)

        credentials_list: dict[str, Any] | None | Unset
        if isinstance(self.credentials_list, Unset):
            credentials_list = UNSET
        elif isinstance(self.credentials_list, CosmosDbProcessingCredentialsType0):
            credentials_list = self.credentials_list.to_dict()
        else:
            credentials_list = self.credentials_list

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cosmosDbAccountIds": cosmos_db_account_ids,
                "repositoryId": repository_id,
                "tenantId": tenant_id,
                "serviceAccountId": service_account_id,
            }
        )
        if credentials_list is not UNSET:
            field_dict["credentialsList"] = credentials_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cosmos_db_processing_credentials_type_0 import CosmosDbProcessingCredentialsType0

        d = dict(src_dict)
        cosmos_db_account_ids = cast(list[str], d.pop("cosmosDbAccountIds"))

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

        def _parse_credentials_list(data: object) -> CosmosDbProcessingCredentialsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cosmos_db_processing_credentials_type_0 = (
                    CosmosDbProcessingCredentialsType0.from_dict(data)
                )

                return componentsschemas_cosmos_db_processing_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CosmosDbProcessingCredentialsType0 | None | Unset, data)

        credentials_list = _parse_credentials_list(d.pop("credentialsList", UNSET))

        cosmos_db_manual_backup_settings = cls(
            cosmos_db_account_ids=cosmos_db_account_ids,
            repository_id=repository_id,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            credentials_list=credentials_list,
        )

        return cosmos_db_manual_backup_settings
