from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.policy_type import PolicyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VbrBackup")


@_attrs_define
class VbrBackup:
    """
    Attributes:
        id (UUID | Unset):
        last_policy_id (None | Unset | UUID):
        last_policy_display_name (None | str | Unset):
        repository_id (None | str | Unset):
        last_policy_type (PolicyType | Unset): Workload type protected by a backup policy.
    """

    id: UUID | Unset = UNSET
    last_policy_id: None | Unset | UUID = UNSET
    last_policy_display_name: None | str | Unset = UNSET
    repository_id: None | str | Unset = UNSET
    last_policy_type: PolicyType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        last_policy_id: None | str | Unset
        if isinstance(self.last_policy_id, Unset):
            last_policy_id = UNSET
        elif isinstance(self.last_policy_id, UUID):
            last_policy_id = str(self.last_policy_id)
        else:
            last_policy_id = self.last_policy_id

        last_policy_display_name: None | str | Unset
        if isinstance(self.last_policy_display_name, Unset):
            last_policy_display_name = UNSET
        else:
            last_policy_display_name = self.last_policy_display_name

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        else:
            repository_id = self.repository_id

        last_policy_type: str | Unset = UNSET
        if not isinstance(self.last_policy_type, Unset):
            last_policy_type = self.last_policy_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if last_policy_id is not UNSET:
            field_dict["lastPolicyId"] = last_policy_id
        if last_policy_display_name is not UNSET:
            field_dict["lastPolicyDisplayName"] = last_policy_display_name
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if last_policy_type is not UNSET:
            field_dict["lastPolicyType"] = last_policy_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_last_policy_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_policy_id_type_0 = UUID(data)

                return last_policy_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        last_policy_id = _parse_last_policy_id(d.pop("lastPolicyId", UNSET))

        def _parse_last_policy_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_policy_display_name = _parse_last_policy_display_name(d.pop("lastPolicyDisplayName", UNSET))

        def _parse_repository_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_id = _parse_repository_id(d.pop("repositoryId", UNSET))

        _last_policy_type = d.pop("lastPolicyType", UNSET)
        last_policy_type: PolicyType | Unset
        if isinstance(_last_policy_type, Unset):
            last_policy_type = UNSET
        else:
            last_policy_type = PolicyType(_last_policy_type)

        vbr_backup = cls(
            id=id,
            last_policy_id=last_policy_id,
            last_policy_display_name=last_policy_display_name,
            repository_id=repository_id,
            last_policy_type=last_policy_type,
        )

        return vbr_backup
