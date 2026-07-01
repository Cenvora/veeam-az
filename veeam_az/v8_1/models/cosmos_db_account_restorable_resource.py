from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cosmos_db_account_restorable_subresource import CosmosDbAccountRestorableSubresource


T = TypeVar("T", bound="CosmosDbAccountRestorableResource")


@_attrs_define
class CosmosDbAccountRestorableResource:
    """Specifies information on a Cosmos DB account item available for restore.

    Attributes:
        name (str | Unset): Specifies the name of the item.
        resource_type (None | str | Unset): Specifies the type of the item. The following types are available&#58;
            `Database` (applies to Cosmos DB accounts of the *NoSQL*, *MongoDB* and *Apache Gremlin* kinds), `Collection`
            (applies to Cosmos DB accounts of the *NoSQL* and *MongoDB* kinds), `Graph` (applies to Cosmos DB accounts of
            the *Apache Gremlin* kind) and `Table` (applies to Cosmos DB accounts of the *Table* kind).
        subresources (list[CosmosDbAccountRestorableSubresource] | None | Unset): Specifies a list of subresources
            contained in the item.
    """

    name: str | Unset = UNSET
    resource_type: None | str | Unset = UNSET
    subresources: list[CosmosDbAccountRestorableSubresource] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        resource_type: None | str | Unset
        if isinstance(self.resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = self.resource_type

        subresources: list[dict[str, Any]] | None | Unset
        if isinstance(self.subresources, Unset):
            subresources = UNSET
        elif isinstance(self.subresources, list):
            subresources = []
            for subresources_type_0_item_data in self.subresources:
                subresources_type_0_item = subresources_type_0_item_data.to_dict()
                subresources.append(subresources_type_0_item)

        else:
            subresources = self.subresources

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if subresources is not UNSET:
            field_dict["subresources"] = subresources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cosmos_db_account_restorable_subresource import CosmosDbAccountRestorableSubresource

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_resource_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_type = _parse_resource_type(d.pop("resourceType", UNSET))

        def _parse_subresources(data: object) -> list[CosmosDbAccountRestorableSubresource] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subresources_type_0 = []
                _subresources_type_0 = data
                for subresources_type_0_item_data in _subresources_type_0:
                    subresources_type_0_item = CosmosDbAccountRestorableSubresource.from_dict(
                        subresources_type_0_item_data
                    )

                    subresources_type_0.append(subresources_type_0_item)

                return subresources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CosmosDbAccountRestorableSubresource] | None | Unset, data)

        subresources = _parse_subresources(d.pop("subresources", UNSET))

        cosmos_db_account_restorable_resource = cls(
            name=name,
            resource_type=resource_type,
            subresources=subresources,
        )

        return cosmos_db_account_restorable_resource
