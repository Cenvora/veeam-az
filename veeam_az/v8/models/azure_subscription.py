from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.azure_environment import AzureEnvironment
from ..models.subscription_availability import SubscriptionAvailability
from ..models.subscription_status import SubscriptionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="AzureSubscription")


@_attrs_define
class AzureSubscription:
    """Specifies information on an Azure subscription.

    Attributes:
        id (UUID): Specifies the Microsoft Azure ID assigned to the subscription.
        environment (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        tenant_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a tenant with which the
            subscription is associated.
        tenant_name (None | str | Unset): Specifies the name of the tenant.
        name (None | str | Unset): Specifies the name of the subscription.
        status (SubscriptionStatus | Unset): Specifies the subscription status.
        availability (SubscriptionAvailability | Unset): Specifies the subscription availability.
        worker_resource_group_name (None | str | Unset): Specifies the name of the resource group used for worker
            deployment.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: UUID
    environment: AzureEnvironment | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    tenant_name: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    status: SubscriptionStatus | Unset = UNSET
    availability: SubscriptionAvailability | Unset = UNSET
    worker_resource_group_name: None | str | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id = str(self.id)

        environment: str | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        tenant_name: None | str | Unset
        if isinstance(self.tenant_name, Unset):
            tenant_name = UNSET
        else:
            tenant_name = self.tenant_name

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        availability: str | Unset = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value

        worker_resource_group_name: None | str | Unset
        if isinstance(self.worker_resource_group_name, Unset):
            worker_resource_group_name = UNSET
        else:
            worker_resource_group_name = self.worker_resource_group_name

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
                "id": id,
            }
        )
        if environment is not UNSET:
            field_dict["environment"] = environment
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if tenant_name is not UNSET:
            field_dict["tenantName"] = tenant_name
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if availability is not UNSET:
            field_dict["availability"] = availability
        if worker_resource_group_name is not UNSET:
            field_dict["workerResourceGroupName"] = worker_resource_group_name
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        _environment = d.pop("environment", UNSET)
        environment: AzureEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = AzureEnvironment(_environment)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_tenant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_name = _parse_tenant_name(d.pop("tenantName", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _status = d.pop("status", UNSET)
        status: SubscriptionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SubscriptionStatus(_status)

        _availability = d.pop("availability", UNSET)
        availability: SubscriptionAvailability | Unset
        if isinstance(_availability, Unset):
            availability = UNSET
        else:
            availability = SubscriptionAvailability(_availability)

        def _parse_worker_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        worker_resource_group_name = _parse_worker_resource_group_name(d.pop("workerResourceGroupName", UNSET))

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

        azure_subscription = cls(
            id=id,
            environment=environment,
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            name=name,
            status=status,
            availability=availability,
            worker_resource_group_name=worker_resource_group_name,
            field_links=field_links,
        )

        return azure_subscription
