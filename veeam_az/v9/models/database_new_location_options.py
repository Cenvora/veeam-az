from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseNewLocationOptions")


@_attrs_define
class DatabaseNewLocationOptions:
    """Specifies information on a new restore target location.

    Attributes:
        new_name (None | str | Unset): Specifies a name for the new target location.
        target_server_id (None | str | Unset): Specifies the system ID assigned to a target SQL Server in the Veeam
            Backup for Microsoft Azure REST API.
        elastic_pool_name (None | str | Unset): Specifies a name for the elastic pool.
    """

    new_name: None | str | Unset = UNSET
    target_server_id: None | str | Unset = UNSET
    elastic_pool_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_name: None | str | Unset
        if isinstance(self.new_name, Unset):
            new_name = UNSET
        else:
            new_name = self.new_name

        target_server_id: None | str | Unset
        if isinstance(self.target_server_id, Unset):
            target_server_id = UNSET
        else:
            target_server_id = self.target_server_id

        elastic_pool_name: None | str | Unset
        if isinstance(self.elastic_pool_name, Unset):
            elastic_pool_name = UNSET
        else:
            elastic_pool_name = self.elastic_pool_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if new_name is not UNSET:
            field_dict["newName"] = new_name
        if target_server_id is not UNSET:
            field_dict["targetServerId"] = target_server_id
        if elastic_pool_name is not UNSET:
            field_dict["elasticPoolName"] = elastic_pool_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_new_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_name = _parse_new_name(d.pop("newName", UNSET))

        def _parse_target_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_server_id = _parse_target_server_id(d.pop("targetServerId", UNSET))

        def _parse_elastic_pool_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        elastic_pool_name = _parse_elastic_pool_name(d.pop("elasticPoolName", UNSET))

        database_new_location_options = cls(
            new_name=new_name,
            target_server_id=target_server_id,
            elastic_pool_name=elastic_pool_name,
        )

        return database_new_location_options
