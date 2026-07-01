from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.verification_needed_result import VerificationNeededResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_response_azure_accounts import CheckResponseAzureAccounts
    from ..models.check_response_portal_users import CheckResponsePortalUsers
    from ..models.check_response_repositories import CheckResponseRepositories
    from ..models.check_response_repository_encryption import CheckResponseRepositoryEncryption
    from ..models.check_response_repository_ownership import CheckResponseRepositoryOwnership
    from ..models.check_response_worker_configurations import CheckResponseWorkerConfigurations


T = TypeVar("T", bound="CheckResponse")


@_attrs_define
class CheckResponse:
    """Detailed information on the configuration check.

    Attributes:
        missing_roles (CheckResponseAzureAccounts | Unset): Information on the missing Azure roles required to work with
            the service account.
        worker_configuration (CheckResponseWorkerConfigurations | Unset): Results of the worker configurations check.
        repositories (CheckResponseRepositories | Unset): Results of the configuration check of repositories.
        repository_ownership (CheckResponseRepositoryOwnership | Unset):
        repository_encryption (CheckResponseRepositoryEncryption | Unset): Results of the configuration check of
            repositories encryption.
        mfa_users (CheckResponsePortalUsers | Unset): List of MFA users that might be affected after configuration
            restore.
        sso_configuration (VerificationNeededResult | Unset): Result of the configuration check.
    """

    missing_roles: CheckResponseAzureAccounts | Unset = UNSET
    worker_configuration: CheckResponseWorkerConfigurations | Unset = UNSET
    repositories: CheckResponseRepositories | Unset = UNSET
    repository_ownership: CheckResponseRepositoryOwnership | Unset = UNSET
    repository_encryption: CheckResponseRepositoryEncryption | Unset = UNSET
    mfa_users: CheckResponsePortalUsers | Unset = UNSET
    sso_configuration: VerificationNeededResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        missing_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.missing_roles, Unset):
            missing_roles = self.missing_roles.to_dict()

        worker_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.worker_configuration, Unset):
            worker_configuration = self.worker_configuration.to_dict()

        repositories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = self.repositories.to_dict()

        repository_ownership: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_ownership, Unset):
            repository_ownership = self.repository_ownership.to_dict()

        repository_encryption: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_encryption, Unset):
            repository_encryption = self.repository_encryption.to_dict()

        mfa_users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mfa_users, Unset):
            mfa_users = self.mfa_users.to_dict()

        sso_configuration: str | Unset = UNSET
        if not isinstance(self.sso_configuration, Unset):
            sso_configuration = self.sso_configuration.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if missing_roles is not UNSET:
            field_dict["missingRoles"] = missing_roles
        if worker_configuration is not UNSET:
            field_dict["workerConfiguration"] = worker_configuration
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if repository_ownership is not UNSET:
            field_dict["repositoryOwnership"] = repository_ownership
        if repository_encryption is not UNSET:
            field_dict["repositoryEncryption"] = repository_encryption
        if mfa_users is not UNSET:
            field_dict["mfaUsers"] = mfa_users
        if sso_configuration is not UNSET:
            field_dict["ssoConfiguration"] = sso_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_response_azure_accounts import CheckResponseAzureAccounts
        from ..models.check_response_portal_users import CheckResponsePortalUsers
        from ..models.check_response_repositories import CheckResponseRepositories
        from ..models.check_response_repository_encryption import CheckResponseRepositoryEncryption
        from ..models.check_response_repository_ownership import CheckResponseRepositoryOwnership
        from ..models.check_response_worker_configurations import CheckResponseWorkerConfigurations

        d = dict(src_dict)
        _missing_roles = d.pop("missingRoles", UNSET)
        missing_roles: CheckResponseAzureAccounts | Unset
        if isinstance(_missing_roles, Unset):
            missing_roles = UNSET
        else:
            missing_roles = CheckResponseAzureAccounts.from_dict(_missing_roles)

        _worker_configuration = d.pop("workerConfiguration", UNSET)
        worker_configuration: CheckResponseWorkerConfigurations | Unset
        if isinstance(_worker_configuration, Unset):
            worker_configuration = UNSET
        else:
            worker_configuration = CheckResponseWorkerConfigurations.from_dict(_worker_configuration)

        _repositories = d.pop("repositories", UNSET)
        repositories: CheckResponseRepositories | Unset
        if isinstance(_repositories, Unset):
            repositories = UNSET
        else:
            repositories = CheckResponseRepositories.from_dict(_repositories)

        _repository_ownership = d.pop("repositoryOwnership", UNSET)
        repository_ownership: CheckResponseRepositoryOwnership | Unset
        if isinstance(_repository_ownership, Unset):
            repository_ownership = UNSET
        else:
            repository_ownership = CheckResponseRepositoryOwnership.from_dict(_repository_ownership)

        _repository_encryption = d.pop("repositoryEncryption", UNSET)
        repository_encryption: CheckResponseRepositoryEncryption | Unset
        if isinstance(_repository_encryption, Unset):
            repository_encryption = UNSET
        else:
            repository_encryption = CheckResponseRepositoryEncryption.from_dict(_repository_encryption)

        _mfa_users = d.pop("mfaUsers", UNSET)
        mfa_users: CheckResponsePortalUsers | Unset
        if isinstance(_mfa_users, Unset):
            mfa_users = UNSET
        else:
            mfa_users = CheckResponsePortalUsers.from_dict(_mfa_users)

        _sso_configuration = d.pop("ssoConfiguration", UNSET)
        sso_configuration: VerificationNeededResult | Unset
        if isinstance(_sso_configuration, Unset):
            sso_configuration = UNSET
        else:
            sso_configuration = VerificationNeededResult(_sso_configuration)

        check_response = cls(
            missing_roles=missing_roles,
            worker_configuration=worker_configuration,
            repositories=repositories,
            repository_ownership=repository_ownership,
            repository_encryption=repository_encryption,
            mfa_users=mfa_users,
            sso_configuration=sso_configuration,
        )

        check_response.additional_properties = d
        return check_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
