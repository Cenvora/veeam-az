from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageAccountCapabilities")


@_attrs_define
class StorageAccountCapabilities:
    """Result of the performed operation.

    Attributes:
        supports_archive (bool | Unset): Defines whether the storage account supports arcive tier.
        recommended_concurrency (int | Unset): Specifies the optimal number of concurrent connections from worker
            instances to the repository located in the storage account.
    """

    supports_archive: bool | Unset = UNSET
    recommended_concurrency: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        supports_archive = self.supports_archive

        recommended_concurrency = self.recommended_concurrency

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if supports_archive is not UNSET:
            field_dict["supportsArchive"] = supports_archive
        if recommended_concurrency is not UNSET:
            field_dict["recommendedConcurrency"] = recommended_concurrency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supports_archive = d.pop("supportsArchive", UNSET)

        recommended_concurrency = d.pop("recommendedConcurrency", UNSET)

        storage_account_capabilities = cls(
            supports_archive=supports_archive,
            recommended_concurrency=recommended_concurrency,
        )

        return storage_account_capabilities
