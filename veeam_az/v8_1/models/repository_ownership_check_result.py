from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.check_result_severity import CheckResultSeverity
from ..models.repository_ownership_check_result_status import RepositoryOwnershipCheckResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository import Repository


T = TypeVar("T", bound="RepositoryOwnershipCheckResult")


@_attrs_define
class RepositoryOwnershipCheckResult:
    """
    Attributes:
        repository (Repository | Unset): Information on a backup repository.
        status (RepositoryOwnershipCheckResultStatus | Unset):
        severity (CheckResultSeverity | Unset): Specifies the state of the configuration check operation.
        message (None | str | Unset):
        has_another_owner (bool | None | Unset):
        previous_owner (None | str | Unset):
    """

    repository: Repository | Unset = UNSET
    status: RepositoryOwnershipCheckResultStatus | Unset = UNSET
    severity: CheckResultSeverity | Unset = UNSET
    message: None | str | Unset = UNSET
    has_another_owner: bool | None | Unset = UNSET
    previous_owner: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        has_another_owner: bool | None | Unset
        if isinstance(self.has_another_owner, Unset):
            has_another_owner = UNSET
        else:
            has_another_owner = self.has_another_owner

        previous_owner: None | str | Unset
        if isinstance(self.previous_owner, Unset):
            previous_owner = UNSET
        else:
            previous_owner = self.previous_owner

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository is not UNSET:
            field_dict["repository"] = repository
        if status is not UNSET:
            field_dict["status"] = status
        if severity is not UNSET:
            field_dict["severity"] = severity
        if message is not UNSET:
            field_dict["message"] = message
        if has_another_owner is not UNSET:
            field_dict["hasAnotherOwner"] = has_another_owner
        if previous_owner is not UNSET:
            field_dict["previousOwner"] = previous_owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository import Repository

        d = dict(src_dict)
        _repository = d.pop("repository", UNSET)
        repository: Repository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        _status = d.pop("status", UNSET)
        status: RepositoryOwnershipCheckResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RepositoryOwnershipCheckResultStatus(_status)

        _severity = d.pop("severity", UNSET)
        severity: CheckResultSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = CheckResultSeverity(_severity)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_has_another_owner(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_another_owner = _parse_has_another_owner(d.pop("hasAnotherOwner", UNSET))

        def _parse_previous_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_owner = _parse_previous_owner(d.pop("previousOwner", UNSET))

        repository_ownership_check_result = cls(
            repository=repository,
            status=status,
            severity=severity,
            message=message,
            has_another_owner=has_another_owner,
            previous_owner=previous_owner,
        )

        return repository_ownership_check_result
