from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="AzureStorageItemCreationConfig")


@_attrs_define
class AzureStorageItemCreationConfig:
    """
    Attributes:
        name (str): Specifies a name for the created item.
        account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST API to a
            service account whose permissions will be used to create the item.
    """

    name: str
    account_id: UUID

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        account_id = str(self.account_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "accountId": account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        account_id = UUID(d.pop("accountId"))

        azure_storage_item_creation_config = cls(
            name=name,
            account_id=account_id,
        )

        return azure_storage_item_creation_config
