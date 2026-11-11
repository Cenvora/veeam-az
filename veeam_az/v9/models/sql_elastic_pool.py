from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="SqlElasticPool")


@_attrs_define
class SqlElasticPool:
    """Information on each Azure SQL elastic pool.

    Attributes:
        database_storage_capacity_mb (int | Unset): Maximum size of a database within the elastic pool.
        dtu (int | Unset): Maximum database transaction units (DTUs) for the elastic pool.
        edition (None | str | Unset): Pricing tier of the elastic pool.
        id (None | str | Unset): System ID assigned to the elastic pool in the Veeam Backup for Microsoft Azure REST
            API.
        name (None | str | Unset): Azure name of the elastic pool.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region of the elastic pool.
        resource_id (None | str | Unset): Resource ID of the SQL elastic pool.
        server_id (None | str | Unset): System ID assigned to the server ID of the elastic pool in the Veeam Backup for
            Microsoft Azure REST API.
        state (None | str | Unset): State of the elastic pool.
        pool_storage_capacity_mb (int | Unset): Maximum size of the elastic pool.
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to the elastic pool subscription.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    database_storage_capacity_mb: int | Unset = UNSET
    dtu: int | Unset = UNSET
    edition: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    server_id: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    pool_storage_capacity_mb: int | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        database_storage_capacity_mb = self.database_storage_capacity_mb

        dtu = self.dtu

        edition: None | str | Unset
        if isinstance(self.edition, Unset):
            edition = UNSET
        else:
            edition = self.edition

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        server_id: None | str | Unset
        if isinstance(self.server_id, Unset):
            server_id = UNSET
        else:
            server_id = self.server_id

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        pool_storage_capacity_mb = self.pool_storage_capacity_mb

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if database_storage_capacity_mb is not UNSET:
            field_dict["databaseStorageCapacityMb"] = database_storage_capacity_mb
        if dtu is not UNSET:
            field_dict["dtu"] = dtu
        if edition is not UNSET:
            field_dict["edition"] = edition
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if server_id is not UNSET:
            field_dict["serverId"] = server_id
        if state is not UNSET:
            field_dict["state"] = state
        if pool_storage_capacity_mb is not UNSET:
            field_dict["poolStorageCapacityMb"] = pool_storage_capacity_mb
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)
        database_storage_capacity_mb = d.pop("databaseStorageCapacityMb", UNSET)

        dtu = d.pop("dtu", UNSET)

        def _parse_edition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edition = _parse_edition(d.pop("edition", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        def _parse_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_id = _parse_server_id(d.pop("serverId", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        pool_storage_capacity_mb = d.pop("poolStorageCapacityMb", UNSET)

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

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

        sql_elastic_pool = cls(
            database_storage_capacity_mb=database_storage_capacity_mb,
            dtu=dtu,
            edition=edition,
            id=id,
            name=name,
            region_id=region_id,
            resource_id=resource_id,
            server_id=server_id,
            state=state,
            pool_storage_capacity_mb=pool_storage_capacity_mb,
            subscription_id=subscription_id,
            field_links=field_links,
        )

        return sql_elastic_pool
