from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.azure_environment import AzureEnvironment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="ResourceGroup")


@_attrs_define
class ResourceGroup:
    """Specifies information on a resource group.

    Attributes:
        id (None | str | Unset): Specifies a system ID assigned to a resource group in the Veeam Backup for Microsoft
            Azure REST API.
        resource_id (None | str | Unset): Specifies the resource ID assigned to the resource group.
        name (None | str | Unset): Specifies the name of the resource group.
        azure_environment (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        subscription_id (UUID | Unset): Subscription ID.
        tenant_id (None | str | Unset): Microsoft Azure ID assigned to a tenant to which the resource group belongs.
        region_id (None | str | Unset): Specifies a Microsoft Azure ID assigned to a region where the resource group is
            located.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    azure_environment: AzureEnvironment | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if name is not UNSET:
            field_dict["name"] = name
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureEnvironment | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureEnvironment(_azure_environment)

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

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

        resource_group = cls(
            id=id,
            resource_id=resource_id,
            name=name,
            azure_environment=azure_environment,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            region_id=region_id,
            field_links=field_links,
        )

        return resource_group
