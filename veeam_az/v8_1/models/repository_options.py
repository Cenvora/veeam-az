from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.repository_status import RepositoryStatus
from ..models.storage_tier import StorageTier
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryOptions")


@_attrs_define
class RepositoryOptions:
    """
    Attributes:
        status (list[RepositoryStatus] | None | Unset): Returns only backup repositories with the specified status.
        tier (list[StorageTier] | None | Unset): Returns only backup repositories of the specified tier.
        search_pattern (None | str | Unset): Returns only those items of a resource collection whose names match the
            specified search pattern in the parameter value.
        is_encrypted (bool | None | Unset): Returns only backup repositories with enabled encryption.
        immutability_enabled (bool | None | Unset): Defines whether to return only repositories for which the
            immutability is enabled.
        repository_ids (list[UUID] | None | Unset):
    """

    status: list[RepositoryStatus] | None | Unset = UNSET
    tier: list[StorageTier] | None | Unset = UNSET
    search_pattern: None | str | Unset = UNSET
    is_encrypted: bool | None | Unset = UNSET
    immutability_enabled: bool | None | Unset = UNSET
    repository_ids: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: list[str] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, list):
            status = []
            for status_type_0_item_data in self.status:
                status_type_0_item = status_type_0_item_data.value
                status.append(status_type_0_item)

        else:
            status = self.status

        tier: list[str] | None | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        elif isinstance(self.tier, list):
            tier = []
            for tier_type_0_item_data in self.tier:
                tier_type_0_item = tier_type_0_item_data.value
                tier.append(tier_type_0_item)

        else:
            tier = self.tier

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        is_encrypted: bool | None | Unset
        if isinstance(self.is_encrypted, Unset):
            is_encrypted = UNSET
        else:
            is_encrypted = self.is_encrypted

        immutability_enabled: bool | None | Unset
        if isinstance(self.immutability_enabled, Unset):
            immutability_enabled = UNSET
        else:
            immutability_enabled = self.immutability_enabled

        repository_ids: list[str] | None | Unset
        if isinstance(self.repository_ids, Unset):
            repository_ids = UNSET
        elif isinstance(self.repository_ids, list):
            repository_ids = []
            for repository_ids_type_0_item_data in self.repository_ids:
                repository_ids_type_0_item = str(repository_ids_type_0_item_data)
                repository_ids.append(repository_ids_type_0_item)

        else:
            repository_ids = self.repository_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if tier is not UNSET:
            field_dict["tier"] = tier
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern
        if is_encrypted is not UNSET:
            field_dict["isEncrypted"] = is_encrypted
        if immutability_enabled is not UNSET:
            field_dict["immutabilityEnabled"] = immutability_enabled
        if repository_ids is not UNSET:
            field_dict["repositoryIds"] = repository_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> list[RepositoryStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                status_type_0 = []
                _status_type_0 = data
                for status_type_0_item_data in _status_type_0:
                    status_type_0_item = RepositoryStatus(status_type_0_item_data)

                    status_type_0.append(status_type_0_item)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RepositoryStatus] | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_tier(data: object) -> list[StorageTier] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tier_type_0 = []
                _tier_type_0 = data
                for tier_type_0_item_data in _tier_type_0:
                    tier_type_0_item = StorageTier(tier_type_0_item_data)

                    tier_type_0.append(tier_type_0_item)

                return tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StorageTier] | None | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        def _parse_is_encrypted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_encrypted = _parse_is_encrypted(d.pop("isEncrypted", UNSET))

        def _parse_immutability_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        immutability_enabled = _parse_immutability_enabled(d.pop("immutabilityEnabled", UNSET))

        def _parse_repository_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repository_ids_type_0 = []
                _repository_ids_type_0 = data
                for repository_ids_type_0_item_data in _repository_ids_type_0:
                    repository_ids_type_0_item = UUID(repository_ids_type_0_item_data)

                    repository_ids_type_0.append(repository_ids_type_0_item)

                return repository_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        repository_ids = _parse_repository_ids(d.pop("repositoryIds", UNSET))

        repository_options = cls(
            status=status,
            tier=tier,
            search_pattern=search_pattern,
            is_encrypted=is_encrypted,
            immutability_enabled=immutability_enabled,
            repository_ids=repository_ids,
        )

        return repository_options
