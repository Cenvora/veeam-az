from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.database_status import DatabaseStatus
from ..models.database_type import DatabaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="Database")


@_attrs_define
class Database:
    """Information on an Azure SQL database.

    Attributes:
        id (None | str | Unset): System ID assigned to the Azure SQL database in the Veeam Backup for Microsoft Azure
            REST API.
        resource_id (None | str | Unset): Resource ID of the Azure SQL database.
        name (None | str | Unset): Name of the Azure SQL database.
        server_name (None | str | Unset): Name of an Azure SQL Server hosting the database.
        server_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the SQL
            Server hosting the database.
        resource_group_name (None | str | Unset): Information on a resource group to which the database belongs.
        size_in_mb (int | Unset): Size of the database (in Mb).
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to a subscription to which the database belongs.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the database resides.
        region_name (None | str | Unset): Name of the Azure region where the database resides.
        has_elastic_pool (bool | None | Unset): Defines whether the database belongs to an elastic pool.
        status (DatabaseStatus | Unset): Status of the database.
        database_type (DatabaseType | Unset): Type of the database.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    server_name: None | str | Unset = UNSET
    server_id: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    size_in_mb: int | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    region_id: None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    has_elastic_pool: bool | None | Unset = UNSET
    status: DatabaseStatus | Unset = UNSET
    database_type: DatabaseType | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        server_id: None | str | Unset
        if isinstance(self.server_id, Unset):
            server_id = UNSET
        else:
            server_id = self.server_id

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        size_in_mb = self.size_in_mb

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

        has_elastic_pool: bool | None | Unset
        if isinstance(self.has_elastic_pool, Unset):
            has_elastic_pool = UNSET
        else:
            has_elastic_pool = self.has_elastic_pool

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        database_type: str | Unset = UNSET
        if not isinstance(self.database_type, Unset):
            database_type = self.database_type.value

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
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if name is not UNSET:
            field_dict["name"] = name
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if server_id is not UNSET:
            field_dict["serverId"] = server_id
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if size_in_mb is not UNSET:
            field_dict["sizeInMb"] = size_in_mb
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if has_elastic_pool is not UNSET:
            field_dict["hasElasticPool"] = has_elastic_pool
        if status is not UNSET:
            field_dict["status"] = status
        if database_type is not UNSET:
            field_dict["databaseType"] = database_type
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

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("serverName", UNSET))

        def _parse_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_id = _parse_server_id(d.pop("serverId", UNSET))

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        size_in_mb = d.pop("sizeInMb", UNSET)

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

        def _parse_has_elastic_pool(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_elastic_pool = _parse_has_elastic_pool(d.pop("hasElasticPool", UNSET))

        _status = d.pop("status", UNSET)
        status: DatabaseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DatabaseStatus(_status)

        _database_type = d.pop("databaseType", UNSET)
        database_type: DatabaseType | Unset
        if isinstance(_database_type, Unset):
            database_type = UNSET
        else:
            database_type = DatabaseType(_database_type)

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

        database = cls(
            id=id,
            resource_id=resource_id,
            name=name,
            server_name=server_name,
            server_id=server_id,
            resource_group_name=resource_group_name,
            size_in_mb=size_in_mb,
            subscription_id=subscription_id,
            region_id=region_id,
            region_name=region_name,
            has_elastic_pool=has_elastic_pool,
            status=status,
            database_type=database_type,
            field_links=field_links,
        )

        return database
