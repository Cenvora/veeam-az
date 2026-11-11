from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryValidateDeleteOptions")


@_attrs_define
class RepositoryValidateDeleteOptions:
    """
    Attributes:
        repository_id (list[UUID] | None | Unset):
    """

    repository_id: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository_id: list[str] | None | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        elif isinstance(self.repository_id, list):
            repository_id = []
            for repository_id_type_0_item_data in self.repository_id:
                repository_id_type_0_item = str(repository_id_type_0_item_data)
                repository_id.append(repository_id_type_0_item)

        else:
            repository_id = self.repository_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_repository_id(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repository_id_type_0 = []
                _repository_id_type_0 = data
                for repository_id_type_0_item_data in _repository_id_type_0:
                    repository_id_type_0_item = UUID(repository_id_type_0_item_data)

                    repository_id_type_0.append(repository_id_type_0_item)

                return repository_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        repository_id = _parse_repository_id(d.pop("repositoryId", UNSET))

        repository_validate_delete_options = cls(
            repository_id=repository_id,
        )

        return repository_validate_delete_options
