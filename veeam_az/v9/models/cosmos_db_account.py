from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.cosmos_db_account_status import CosmosDbAccountStatus
from ..models.cosmos_db_account_type import CosmosDbAccountType
from ..models.cosmos_db_capacity_mode import CosmosDbCapacityMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="CosmosDbAccount")


@_attrs_define
class CosmosDbAccount:
    r"""Information on a Cosmos DB account.

    Attributes:
        id (None | str | Unset): System ID assigned to the Cosmos DB account in the Veeam Backup for Microsoft Azure
            REST API.
        azure_id (None | str | Unset): Resource ID assigned to the Cosmos DB account in Microsoft Azure.
        name (None | str | Unset): Name of the Cosmos DB account.
        status (CosmosDbAccountStatus | Unset): Status of the protected Cosmos DB account.
        account_type (CosmosDbAccountType | Unset): Kind of the protected Cosmos DB account.
        latest_restorable_timestamp (datetime.datetime | None | Unset): The most recent date and time to which the
            Cosmos DB account can be restored.
        source_size_bytes (int | None | Unset): Total size of the Cosmos DB account data.
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to a subscription that manages the Cosmos DB
            account.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region in which the Cosmos DB account resides.
        region_name (None | str | Unset): Name of the region in which the Cosmos DB account resides.
        resource_group_name (None | str | Unset): Name of the resource group to which the Cosmos DB account belongs.
        postgres_version (None | str | Unset): \[Applies to Cosmos DB for PostgreSQL accounts only] PostgreSQL version
            of the Cosmos DB for PostgreSQL cluster.
        mongo_db_server_version (None | str | Unset):
        is_deleted (bool | Unset): Defines whether the Cosmos DB account is no longer present in Azure infrastructure.
        capacity_mode (CosmosDbCapacityMode | Unset):
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    azure_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    status: CosmosDbAccountStatus | Unset = UNSET
    account_type: CosmosDbAccountType | Unset = UNSET
    latest_restorable_timestamp: datetime.datetime | None | Unset = UNSET
    source_size_bytes: int | None | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    postgres_version: None | str | Unset = UNSET
    mongo_db_server_version: None | str | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    capacity_mode: CosmosDbCapacityMode | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        azure_id: None | str | Unset
        if isinstance(self.azure_id, Unset):
            azure_id = UNSET
        else:
            azure_id = self.azure_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        latest_restorable_timestamp: None | str | Unset
        if isinstance(self.latest_restorable_timestamp, Unset):
            latest_restorable_timestamp = UNSET
        elif isinstance(self.latest_restorable_timestamp, datetime.datetime):
            latest_restorable_timestamp = self.latest_restorable_timestamp.isoformat()
        else:
            latest_restorable_timestamp = self.latest_restorable_timestamp

        source_size_bytes: int | None | Unset
        if isinstance(self.source_size_bytes, Unset):
            source_size_bytes = UNSET
        else:
            source_size_bytes = self.source_size_bytes

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        postgres_version: None | str | Unset
        if isinstance(self.postgres_version, Unset):
            postgres_version = UNSET
        else:
            postgres_version = self.postgres_version

        mongo_db_server_version: None | str | Unset
        if isinstance(self.mongo_db_server_version, Unset):
            mongo_db_server_version = UNSET
        else:
            mongo_db_server_version = self.mongo_db_server_version

        is_deleted = self.is_deleted

        capacity_mode: str | Unset = UNSET
        if not isinstance(self.capacity_mode, Unset):
            capacity_mode = self.capacity_mode.value

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if azure_id is not UNSET:
            field_dict["azureId"] = azure_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if latest_restorable_timestamp is not UNSET:
            field_dict["latestRestorableTimestamp"] = latest_restorable_timestamp
        if source_size_bytes is not UNSET:
            field_dict["sourceSizeBytes"] = source_size_bytes
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if postgres_version is not UNSET:
            field_dict["postgresVersion"] = postgres_version
        if mongo_db_server_version is not UNSET:
            field_dict["mongoDbServerVersion"] = mongo_db_server_version
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if capacity_mode is not UNSET:
            field_dict["capacityMode"] = capacity_mode
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_azure_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_id = _parse_azure_id(d.pop("azureId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _status = d.pop("status", UNSET)
        status: CosmosDbAccountStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CosmosDbAccountStatus(_status)

        _account_type = d.pop("accountType", UNSET)
        account_type: CosmosDbAccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = CosmosDbAccountType(_account_type)

        def _parse_latest_restorable_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_restorable_timestamp_type_0 = isoparse(data)

                return latest_restorable_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_restorable_timestamp = _parse_latest_restorable_timestamp(d.pop("latestRestorableTimestamp", UNSET))

        def _parse_source_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_size_bytes = _parse_source_size_bytes(d.pop("sourceSizeBytes", UNSET))

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        def _parse_postgres_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postgres_version = _parse_postgres_version(d.pop("postgresVersion", UNSET))

        def _parse_mongo_db_server_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mongo_db_server_version = _parse_mongo_db_server_version(d.pop("mongoDbServerVersion", UNSET))

        is_deleted = d.pop("isDeleted", UNSET)

        _capacity_mode = d.pop("capacityMode", UNSET)
        capacity_mode: CosmosDbCapacityMode | Unset
        if isinstance(_capacity_mode, Unset):
            capacity_mode = UNSET
        else:
            capacity_mode = CosmosDbCapacityMode(_capacity_mode)

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        cosmos_db_account = cls(
            id=id,
            azure_id=azure_id,
            name=name,
            status=status,
            account_type=account_type,
            latest_restorable_timestamp=latest_restorable_timestamp,
            source_size_bytes=source_size_bytes,
            subscription_id=subscription_id,
            region_id=region_id,
            region_name=region_name,
            resource_group_name=resource_group_name,
            postgres_version=postgres_version,
            mongo_db_server_version=mongo_db_server_version,
            is_deleted=is_deleted,
            capacity_mode=capacity_mode,
            field_links=field_links,
        )

        return cosmos_db_account
