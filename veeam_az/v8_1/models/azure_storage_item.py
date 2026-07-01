from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.container_immutability_policy_state import ContainerImmutabilityPolicyState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="AzureStorageItem")


@_attrs_define
class AzureStorageItem:
    """Information on an Azure storage resource.

    Attributes:
        name (None | str | Unset): Name of an Azure storage resource.
        supports_versioning (bool | None | Unset): Defines whether the *Enable version-level immutability support*
            option is enabled for the blob container.
        immutability_policy_state (ContainerImmutabilityPolicyState | Unset): State of the immutability policy
            configured for the blob container.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    name: None | str | Unset = UNSET
    supports_versioning: bool | None | Unset = UNSET
    immutability_policy_state: ContainerImmutabilityPolicyState | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        supports_versioning: bool | None | Unset
        if isinstance(self.supports_versioning, Unset):
            supports_versioning = UNSET
        else:
            supports_versioning = self.supports_versioning

        immutability_policy_state: str | Unset = UNSET
        if not isinstance(self.immutability_policy_state, Unset):
            immutability_policy_state = self.immutability_policy_state.value

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if supports_versioning is not UNSET:
            field_dict["supportsVersioning"] = supports_versioning
        if immutability_policy_state is not UNSET:
            field_dict["ImmutabilityPolicyState"] = immutability_policy_state
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_supports_versioning(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_versioning = _parse_supports_versioning(d.pop("supportsVersioning", UNSET))

        _immutability_policy_state = d.pop("ImmutabilityPolicyState", UNSET)
        immutability_policy_state: ContainerImmutabilityPolicyState | Unset
        if isinstance(_immutability_policy_state, Unset):
            immutability_policy_state = UNSET
        else:
            immutability_policy_state = ContainerImmutabilityPolicyState(_immutability_policy_state)

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

        azure_storage_item = cls(
            name=name,
            supports_versioning=supports_versioning,
            immutability_policy_state=immutability_policy_state,
            field_links=field_links,
        )

        return azure_storage_item
