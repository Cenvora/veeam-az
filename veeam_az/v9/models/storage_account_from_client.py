from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageAccountFromClient")


@_attrs_define
class StorageAccountFromClient:
    """
    Attributes:
        resource_id (str | Unset):
        service_account_id (str | Unset):
    """

    resource_id: str | Unset = UNSET
    service_account_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        service_account_id = self.service_account_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = d.pop("resourceId", UNSET)

        service_account_id = d.pop("serviceAccountId", UNSET)

        storage_account_from_client = cls(
            resource_id=resource_id,
            service_account_id=service_account_id,
        )

        return storage_account_from_client
