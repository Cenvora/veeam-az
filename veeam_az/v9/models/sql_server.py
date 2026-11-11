from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.sql_server_type import SqlServerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="SqlServer")


@_attrs_define
class SqlServer:
    """Information on an Azure SQL Server.

    Attributes:
        id (None | str | Unset): System ID assigned to the SQL Server in the Veeam Backup for Microsoft Azure REST API.
        name (None | str | Unset): Name of the SQL Server.
        resource_id (None | str | Unset): Resource ID of the SQL Server.
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to a subscription to which the SQL Server belongs.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the SQL Server resides.
        server_type (SqlServerType | Unset): Type of the SQL Server.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    region_id: None | str | Unset = UNSET
    server_type: SqlServerType | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

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

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        server_type: str | Unset = UNSET
        if not isinstance(self.server_type, Unset):
            server_type = self.server_type.value

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
        if name is not UNSET:
            field_dict["name"] = name
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

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

        _server_type = d.pop("serverType", UNSET)
        server_type: SqlServerType | Unset
        if isinstance(_server_type, Unset):
            server_type = UNSET
        else:
            server_type = SqlServerType(_server_type)

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

        sql_server = cls(
            id=id,
            name=name,
            resource_id=resource_id,
            subscription_id=subscription_id,
            region_id=region_id,
            server_type=server_type,
            field_links=field_links,
        )

        return sql_server
