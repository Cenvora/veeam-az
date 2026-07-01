from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseRestoreConfigParameters")


@_attrs_define
class DatabaseRestoreConfigParameters:
    """
    Attributes:
        source_database_name (None | str | Unset):
        database_name (None | str | Unset):
        source_server_name (None | str | Unset):
        server_name (None | str | Unset):
        elastic_pool_name (None | str | Unset):
    """

    source_database_name: None | str | Unset = UNSET
    database_name: None | str | Unset = UNSET
    source_server_name: None | str | Unset = UNSET
    server_name: None | str | Unset = UNSET
    elastic_pool_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_database_name: None | str | Unset
        if isinstance(self.source_database_name, Unset):
            source_database_name = UNSET
        else:
            source_database_name = self.source_database_name

        database_name: None | str | Unset
        if isinstance(self.database_name, Unset):
            database_name = UNSET
        else:
            database_name = self.database_name

        source_server_name: None | str | Unset
        if isinstance(self.source_server_name, Unset):
            source_server_name = UNSET
        else:
            source_server_name = self.source_server_name

        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        elastic_pool_name: None | str | Unset
        if isinstance(self.elastic_pool_name, Unset):
            elastic_pool_name = UNSET
        else:
            elastic_pool_name = self.elastic_pool_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if source_database_name is not UNSET:
            field_dict["sourceDatabaseName"] = source_database_name
        if database_name is not UNSET:
            field_dict["databaseName"] = database_name
        if source_server_name is not UNSET:
            field_dict["sourceServerName"] = source_server_name
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if elastic_pool_name is not UNSET:
            field_dict["elasticPoolName"] = elastic_pool_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_source_database_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_database_name = _parse_source_database_name(d.pop("sourceDatabaseName", UNSET))

        def _parse_database_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        database_name = _parse_database_name(d.pop("databaseName", UNSET))

        def _parse_source_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_server_name = _parse_source_server_name(d.pop("sourceServerName", UNSET))

        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("serverName", UNSET))

        def _parse_elastic_pool_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        elastic_pool_name = _parse_elastic_pool_name(d.pop("elasticPoolName", UNSET))

        database_restore_config_parameters = cls(
            source_database_name=source_database_name,
            database_name=database_name,
            source_server_name=source_server_name,
            server_name=server_name,
            elastic_pool_name=elastic_pool_name,
        )

        return database_restore_config_parameters
