from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryJobInfo")


@_attrs_define
class RepositoryJobInfo:
    r"""\[Applies only if backup creation is enabled for the backup policy] Information on a backup repository added to the
    policy.

        Attributes:
            repository_id (None | str | Unset): System ID assigned to the repository in the Veeam Backup for Microsoft Azure
                REST API.
            repository_name (None | str | Unset): Name of the repository.
            repository_removed (bool | Unset): Defines whether the repository was removed.
    """

    repository_id: None | str | Unset = UNSET
    repository_name: None | str | Unset = UNSET
    repository_removed: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        else:
            repository_id = self.repository_id

        repository_name: None | str | Unset
        if isinstance(self.repository_name, Unset):
            repository_name = UNSET
        else:
            repository_name = self.repository_name

        repository_removed = self.repository_removed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if repository_removed is not UNSET:
            field_dict["repositoryRemoved"] = repository_removed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_repository_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_id = _parse_repository_id(d.pop("repositoryId", UNSET))

        def _parse_repository_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_name = _parse_repository_name(d.pop("repositoryName", UNSET))

        repository_removed = d.pop("repositoryRemoved", UNSET)

        repository_job_info = cls(
            repository_id=repository_id,
            repository_name=repository_name,
            repository_removed=repository_removed,
        )

        return repository_job_info
