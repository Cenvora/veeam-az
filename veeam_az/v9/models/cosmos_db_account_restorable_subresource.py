from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CosmosDbAccountRestorableSubresource")


@_attrs_define
class CosmosDbAccountRestorableSubresource:
    """Specifies information on a subresource.

    Attributes:
        name (str | Unset): Specifies the name of the subresource.
        resource_type (None | str | Unset): Specifies the type of the subresource. The following types are
            available&#58; `Database` (applies to Cosmos DB accounts of the *NoSQL*, *MongoDB* and *Apache Gremlin* kinds),
            `Collection` (applies to Cosmos DB accounts of the *NoSQL* and *MongoDB* kinds), `Graph` (applies to Cosmos DB
            accounts of the *Apache Gremlin* kind) and `Table` (applies to Cosmos DB accounts of the *Table* kind).
    """

    name: str | Unset = UNSET
    resource_type: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        resource_type: None | str | Unset
        if isinstance(self.resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = self.resource_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_resource_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_type = _parse_resource_type(d.pop("resourceType", UNSET))

        cosmos_db_account_restorable_subresource = cls(
            name=name,
            resource_type=resource_type,
        )

        return cosmos_db_account_restorable_subresource
