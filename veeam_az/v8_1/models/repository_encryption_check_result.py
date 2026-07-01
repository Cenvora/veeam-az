from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.check_result_severity import CheckResultSeverity
from ..models.repository_encryption_check_result_status import RepositoryEncryptionCheckResultStatus
from ..models.repository_encryption_method import RepositoryEncryptionMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository import Repository


T = TypeVar("T", bound="RepositoryEncryptionCheckResult")


@_attrs_define
class RepositoryEncryptionCheckResult:
    """Information on a repository.

    Attributes:
        repository (Repository | Unset): Information on a backup repository.
        status (RepositoryEncryptionCheckResultStatus | Unset): Status of the repository encryption settings.
        severity (CheckResultSeverity | Unset): Specifies the state of the configuration check operation.
        encryption_method (RepositoryEncryptionMethod | Unset): Method used for repository encryption.
        message (None | str | Unset): Message on the repository encryption settings check result.
    """

    repository: Repository | Unset = UNSET
    status: RepositoryEncryptionCheckResultStatus | Unset = UNSET
    severity: CheckResultSeverity | Unset = UNSET
    encryption_method: RepositoryEncryptionMethod | Unset = UNSET
    message: None | str | Unset = UNSET

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

        encryption_method: str | Unset = UNSET
        if not isinstance(self.encryption_method, Unset):
            encryption_method = self.encryption_method.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository is not UNSET:
            field_dict["repository"] = repository
        if status is not UNSET:
            field_dict["status"] = status
        if severity is not UNSET:
            field_dict["severity"] = severity
        if encryption_method is not UNSET:
            field_dict["encryptionMethod"] = encryption_method
        if message is not UNSET:
            field_dict["message"] = message

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
        status: RepositoryEncryptionCheckResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RepositoryEncryptionCheckResultStatus(_status)

        _severity = d.pop("severity", UNSET)
        severity: CheckResultSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = CheckResultSeverity(_severity)

        _encryption_method = d.pop("encryptionMethod", UNSET)
        encryption_method: RepositoryEncryptionMethod | Unset
        if isinstance(_encryption_method, Unset):
            encryption_method = UNSET
        else:
            encryption_method = RepositoryEncryptionMethod(_encryption_method)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        repository_encryption_check_result = cls(
            repository=repository,
            status=status,
            severity=severity,
            encryption_method=encryption_method,
            message=message,
        )

        return repository_encryption_check_result
