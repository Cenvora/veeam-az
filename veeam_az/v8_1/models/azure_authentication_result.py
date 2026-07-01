from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.azure_account_purpose import AzureAccountPurpose
from ..models.azure_environment import AzureEnvironment
from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="AzureAuthenticationResult")


@_attrs_define
class AzureAuthenticationResult:
    """Specifies information on authentication in Microsoft Azure environment.

    Attributes:
        access_token_cache (File): Specifies a string value representing authorization token to the Microsoft Azure
            Cross-platform Command Line Interface (Azure CLI).
        authenticated_by_certificate (bool | Unset): Defines whether the type of authentication is a certificate.
        azure_environment (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        azure_account_purposes (list[AzureAccountPurpose] | None | Unset): List of operations that can be performed
            using the service account.
        displayable_id (None | str | Unset): Specifies credentials of the Microsoft Azure account that will be used to
            log in to the Microsoft Azure Cross-platform Command Line Interface (Azure CLI).
        family_name (None | str | Unset): Last name of the user whose credentials are used to log in to the Microsoft
            Azure Cross-platform Command Line Interface (Azure CLI).
        given_name (None | str | Unset): First name of the user whose credentials are used to log in to the Microsoft
            Azure Cross-platform Command Line Interface (Azure CLI).
        identity_provider (None | str | Unset): Specifies the name of the identity provider used to manage identity
            information.
        tenant_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a tenant with which the service
            account is associated.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    access_token_cache: File
    authenticated_by_certificate: bool | Unset = UNSET
    azure_environment: AzureEnvironment | Unset = UNSET
    azure_account_purposes: list[AzureAccountPurpose] | None | Unset = UNSET
    displayable_id: None | str | Unset = UNSET
    family_name: None | str | Unset = UNSET
    given_name: None | str | Unset = UNSET
    identity_provider: None | str | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        access_token_cache = self.access_token_cache.to_tuple()

        authenticated_by_certificate = self.authenticated_by_certificate

        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        azure_account_purposes: list[str] | None | Unset
        if isinstance(self.azure_account_purposes, Unset):
            azure_account_purposes = UNSET
        elif isinstance(self.azure_account_purposes, list):
            azure_account_purposes = []
            for azure_account_purposes_type_0_item_data in self.azure_account_purposes:
                azure_account_purposes_type_0_item = azure_account_purposes_type_0_item_data.value
                azure_account_purposes.append(azure_account_purposes_type_0_item)

        else:
            azure_account_purposes = self.azure_account_purposes

        displayable_id: None | str | Unset
        if isinstance(self.displayable_id, Unset):
            displayable_id = UNSET
        else:
            displayable_id = self.displayable_id

        family_name: None | str | Unset
        if isinstance(self.family_name, Unset):
            family_name = UNSET
        else:
            family_name = self.family_name

        given_name: None | str | Unset
        if isinstance(self.given_name, Unset):
            given_name = UNSET
        else:
            given_name = self.given_name

        identity_provider: None | str | Unset
        if isinstance(self.identity_provider, Unset):
            identity_provider = UNSET
        else:
            identity_provider = self.identity_provider

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accessTokenCache": access_token_cache,
            }
        )
        if authenticated_by_certificate is not UNSET:
            field_dict["authenticatedByCertificate"] = authenticated_by_certificate
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if azure_account_purposes is not UNSET:
            field_dict["azureAccountPurposes"] = azure_account_purposes
        if displayable_id is not UNSET:
            field_dict["displayableId"] = displayable_id
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if identity_provider is not UNSET:
            field_dict["identityProvider"] = identity_provider
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)
        access_token_cache = File(payload=BytesIO(d.pop("accessTokenCache")))

        authenticated_by_certificate = d.pop("authenticatedByCertificate", UNSET)

        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureEnvironment | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureEnvironment(_azure_environment)

        def _parse_azure_account_purposes(data: object) -> list[AzureAccountPurpose] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_account_purposes_type_0 = []
                _azure_account_purposes_type_0 = data
                for azure_account_purposes_type_0_item_data in _azure_account_purposes_type_0:
                    azure_account_purposes_type_0_item = AzureAccountPurpose(azure_account_purposes_type_0_item_data)

                    azure_account_purposes_type_0.append(azure_account_purposes_type_0_item)

                return azure_account_purposes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzureAccountPurpose] | None | Unset, data)

        azure_account_purposes = _parse_azure_account_purposes(d.pop("azureAccountPurposes", UNSET))

        def _parse_displayable_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        displayable_id = _parse_displayable_id(d.pop("displayableId", UNSET))

        def _parse_family_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family_name = _parse_family_name(d.pop("familyName", UNSET))

        def _parse_given_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        given_name = _parse_given_name(d.pop("givenName", UNSET))

        def _parse_identity_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_provider = _parse_identity_provider(d.pop("identityProvider", UNSET))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

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

        azure_authentication_result = cls(
            access_token_cache=access_token_cache,
            authenticated_by_certificate=authenticated_by_certificate,
            azure_environment=azure_environment,
            azure_account_purposes=azure_account_purposes,
            displayable_id=displayable_id,
            family_name=family_name,
            given_name=given_name,
            identity_provider=identity_provider,
            tenant_id=tenant_id,
            field_links=field_links,
        )

        return azure_authentication_result
