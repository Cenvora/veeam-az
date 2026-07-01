from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.policy_id_name_type import PolicyIdNameType
    from ..models.repository import Repository
    from ..models.repository_validate_delete_error import RepositoryValidateDeleteError
    from ..models.uuid_name_pair import UuidNamePair


T = TypeVar("T", bound="RepositoryValidateDelete")


@_attrs_define
class RepositoryValidateDelete:
    """Information on each repository.

    Attributes:
        repository (Repository | Unset): Information on a backup repository.
        used_in_policies (list[PolicyIdNameType] | Unset): List of policies that are using the repository.
        used_in_storage_templates (list[UuidNamePair] | Unset): List of storage templates that are using the repository.
        additional_usages_and_errors (list[RepositoryValidateDeleteError] | None | Unset): List of errors occurred
            during the validation.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    repository: Repository | Unset = UNSET
    used_in_policies: list[PolicyIdNameType] | Unset = UNSET
    used_in_storage_templates: list[UuidNamePair] | Unset = UNSET
    additional_usages_and_errors: list[RepositoryValidateDeleteError] | None | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        used_in_policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.used_in_policies, Unset):
            used_in_policies = []
            for used_in_policies_item_data in self.used_in_policies:
                used_in_policies_item = used_in_policies_item_data.to_dict()
                used_in_policies.append(used_in_policies_item)

        used_in_storage_templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.used_in_storage_templates, Unset):
            used_in_storage_templates = []
            for used_in_storage_templates_item_data in self.used_in_storage_templates:
                used_in_storage_templates_item = used_in_storage_templates_item_data.to_dict()
                used_in_storage_templates.append(used_in_storage_templates_item)

        additional_usages_and_errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.additional_usages_and_errors, Unset):
            additional_usages_and_errors = UNSET
        elif isinstance(self.additional_usages_and_errors, list):
            additional_usages_and_errors = []
            for additional_usages_and_errors_type_0_item_data in self.additional_usages_and_errors:
                additional_usages_and_errors_type_0_item = additional_usages_and_errors_type_0_item_data.to_dict()
                additional_usages_and_errors.append(additional_usages_and_errors_type_0_item)

        else:
            additional_usages_and_errors = self.additional_usages_and_errors

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository is not UNSET:
            field_dict["repository"] = repository
        if used_in_policies is not UNSET:
            field_dict["usedInPolicies"] = used_in_policies
        if used_in_storage_templates is not UNSET:
            field_dict["usedInStorageTemplates"] = used_in_storage_templates
        if additional_usages_and_errors is not UNSET:
            field_dict["additionalUsagesAndErrors"] = additional_usages_and_errors
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.policy_id_name_type import PolicyIdNameType
        from ..models.repository import Repository
        from ..models.repository_validate_delete_error import RepositoryValidateDeleteError
        from ..models.uuid_name_pair import UuidNamePair

        d = dict(src_dict)
        _repository = d.pop("repository", UNSET)
        repository: Repository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        _used_in_policies = d.pop("usedInPolicies", UNSET)
        used_in_policies: list[PolicyIdNameType] | Unset = UNSET
        if _used_in_policies is not UNSET:
            used_in_policies = []
            for used_in_policies_item_data in _used_in_policies:
                used_in_policies_item = PolicyIdNameType.from_dict(used_in_policies_item_data)

                used_in_policies.append(used_in_policies_item)

        _used_in_storage_templates = d.pop("usedInStorageTemplates", UNSET)
        used_in_storage_templates: list[UuidNamePair] | Unset = UNSET
        if _used_in_storage_templates is not UNSET:
            used_in_storage_templates = []
            for used_in_storage_templates_item_data in _used_in_storage_templates:
                used_in_storage_templates_item = UuidNamePair.from_dict(used_in_storage_templates_item_data)

                used_in_storage_templates.append(used_in_storage_templates_item)

        def _parse_additional_usages_and_errors(data: object) -> list[RepositoryValidateDeleteError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_usages_and_errors_type_0 = []
                _additional_usages_and_errors_type_0 = data
                for additional_usages_and_errors_type_0_item_data in _additional_usages_and_errors_type_0:
                    additional_usages_and_errors_type_0_item = RepositoryValidateDeleteError.from_dict(
                        additional_usages_and_errors_type_0_item_data
                    )

                    additional_usages_and_errors_type_0.append(additional_usages_and_errors_type_0_item)

                return additional_usages_and_errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RepositoryValidateDeleteError] | None | Unset, data)

        additional_usages_and_errors = _parse_additional_usages_and_errors(d.pop("additionalUsagesAndErrors", UNSET))

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        repository_validate_delete = cls(
            repository=repository,
            used_in_policies=used_in_policies,
            used_in_storage_templates=used_in_storage_templates,
            additional_usages_and_errors=additional_usages_and_errors,
            field_links=field_links,
        )

        return repository_validate_delete
