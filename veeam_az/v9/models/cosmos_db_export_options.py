from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.cosmos_db_account_type_from_client import CosmosDbAccountTypeFromClient
from ..models.protection_status import ProtectionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CosmosDbExportOptions")


@_attrs_define
class CosmosDbExportOptions:
    """
    Attributes:
        subscription_id (None | Unset | UUID): Returns only Cosmos DB accounts managed by a subscription with the
            specified ID.
        tenant_id (None | Unset | UUID): Returns only Cosmos DB accounts that belong to a tenant with the specified ID.
        service_account_id (None | str | Unset): Returns only Cosmos DB accounts to which a service account with the
            specified ID has access.
        search_pattern (None | str | Unset): Returns only those items of a resource collection whose names match the
            specified search pattern in the parameter value.
        region_ids (list[str] | None | Unset): Returns only Cosmos DB accounts that reside in Azure regions with the
            specified IDs.
        cosmos_db_account_ids (list[str] | None | Unset): Specifies Microsoft Azure IDs assigned to Cosmos DB accounts
            whose data will be exported.
        account_types (list[CosmosDbAccountTypeFromClient] | None | Unset): Returns only Cosmos DB accounts of selected
            types.
        soft_deleted (bool | None | Unset): Defines whether to include deleted Cosmos DB accounts into the response.
        cosmos_db_accounts_from_protected_regions (bool | Unset): Defines whether Veeam Backup for Microsoft Azure must
            return only Cosmos DB accounts that reside in regions protected by backup policies.
        protection_status (list[ProtectionStatus] | None | Unset): Returns only Cosmos DB accounts with the specified
            protection statuses.
    """

    subscription_id: None | Unset | UUID = UNSET
    tenant_id: None | Unset | UUID = UNSET
    service_account_id: None | str | Unset = UNSET
    search_pattern: None | str | Unset = UNSET
    region_ids: list[str] | None | Unset = UNSET
    cosmos_db_account_ids: list[str] | None | Unset = UNSET
    account_types: list[CosmosDbAccountTypeFromClient] | None | Unset = UNSET
    soft_deleted: bool | None | Unset = UNSET
    cosmos_db_accounts_from_protected_regions: bool | Unset = UNSET
    protection_status: list[ProtectionStatus] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        elif isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        region_ids: list[str] | None | Unset
        if isinstance(self.region_ids, Unset):
            region_ids = UNSET
        elif isinstance(self.region_ids, list):
            region_ids = self.region_ids

        else:
            region_ids = self.region_ids

        cosmos_db_account_ids: list[str] | None | Unset
        if isinstance(self.cosmos_db_account_ids, Unset):
            cosmos_db_account_ids = UNSET
        elif isinstance(self.cosmos_db_account_ids, list):
            cosmos_db_account_ids = self.cosmos_db_account_ids

        else:
            cosmos_db_account_ids = self.cosmos_db_account_ids

        account_types: list[str] | None | Unset
        if isinstance(self.account_types, Unset):
            account_types = UNSET
        elif isinstance(self.account_types, list):
            account_types = []
            for account_types_type_0_item_data in self.account_types:
                account_types_type_0_item = account_types_type_0_item_data.value
                account_types.append(account_types_type_0_item)

        else:
            account_types = self.account_types

        soft_deleted: bool | None | Unset
        if isinstance(self.soft_deleted, Unset):
            soft_deleted = UNSET
        else:
            soft_deleted = self.soft_deleted

        cosmos_db_accounts_from_protected_regions = self.cosmos_db_accounts_from_protected_regions

        protection_status: list[str] | None | Unset
        if isinstance(self.protection_status, Unset):
            protection_status = UNSET
        elif isinstance(self.protection_status, list):
            protection_status = []
            for protection_status_type_0_item_data in self.protection_status:
                protection_status_type_0_item = protection_status_type_0_item_data.value
                protection_status.append(protection_status_type_0_item)

        else:
            protection_status = self.protection_status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern
        if region_ids is not UNSET:
            field_dict["regionIds"] = region_ids
        if cosmos_db_account_ids is not UNSET:
            field_dict["cosmosDbAccountIds"] = cosmos_db_account_ids
        if account_types is not UNSET:
            field_dict["accountTypes"] = account_types
        if soft_deleted is not UNSET:
            field_dict["softDeleted"] = soft_deleted
        if cosmos_db_accounts_from_protected_regions is not UNSET:
            field_dict["cosmosDbAccountsFromProtectedRegions"] = cosmos_db_accounts_from_protected_regions
        if protection_status is not UNSET:
            field_dict["protectionStatus"] = protection_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_tenant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        def _parse_region_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                region_ids_type_0 = cast(list[str], data)

                return region_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        region_ids = _parse_region_ids(d.pop("regionIds", UNSET))

        def _parse_cosmos_db_account_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cosmos_db_account_ids_type_0 = cast(list[str], data)

                return cosmos_db_account_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cosmos_db_account_ids = _parse_cosmos_db_account_ids(d.pop("cosmosDbAccountIds", UNSET))

        def _parse_account_types(data: object) -> list[CosmosDbAccountTypeFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                account_types_type_0 = []
                _account_types_type_0 = data
                for account_types_type_0_item_data in _account_types_type_0:
                    account_types_type_0_item = CosmosDbAccountTypeFromClient(account_types_type_0_item_data)

                    account_types_type_0.append(account_types_type_0_item)

                return account_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CosmosDbAccountTypeFromClient] | None | Unset, data)

        account_types = _parse_account_types(d.pop("accountTypes", UNSET))

        def _parse_soft_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        soft_deleted = _parse_soft_deleted(d.pop("softDeleted", UNSET))

        cosmos_db_accounts_from_protected_regions = d.pop("cosmosDbAccountsFromProtectedRegions", UNSET)

        def _parse_protection_status(data: object) -> list[ProtectionStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protection_status_type_0 = []
                _protection_status_type_0 = data
                for protection_status_type_0_item_data in _protection_status_type_0:
                    protection_status_type_0_item = ProtectionStatus(protection_status_type_0_item_data)

                    protection_status_type_0.append(protection_status_type_0_item)

                return protection_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProtectionStatus] | None | Unset, data)

        protection_status = _parse_protection_status(d.pop("protectionStatus", UNSET))

        cosmos_db_export_options = cls(
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            search_pattern=search_pattern,
            region_ids=region_ids,
            cosmos_db_account_ids=cosmos_db_account_ids,
            account_types=account_types,
            soft_deleted=soft_deleted,
            cosmos_db_accounts_from_protected_regions=cosmos_db_accounts_from_protected_regions,
            protection_status=protection_status,
        )

        return cosmos_db_export_options
