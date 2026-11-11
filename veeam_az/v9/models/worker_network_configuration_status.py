from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.worker_configuration_status_result import WorkerConfigurationStatusResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerNetworkConfigurationStatus")


@_attrs_define
class WorkerNetworkConfigurationStatus:
    """
    Attributes:
        has_service_endpoint_microsoft_storage (bool | None | Unset):
        virtual_network_found (bool | Unset):
        virtual_network_region_match (bool | None | Unset):
        network_security_group_found (bool | None | Unset):
        network_security_group_region_match (bool | None | Unset):
        network_security_group_deleted (bool | None | Unset):
        virtual_network_subnet_match (bool | None | Unset):
        subscription_match (bool | None | Unset):
        summary (WorkerConfigurationStatusResult | Unset):
    """

    has_service_endpoint_microsoft_storage: bool | None | Unset = UNSET
    virtual_network_found: bool | Unset = UNSET
    virtual_network_region_match: bool | None | Unset = UNSET
    network_security_group_found: bool | None | Unset = UNSET
    network_security_group_region_match: bool | None | Unset = UNSET
    network_security_group_deleted: bool | None | Unset = UNSET
    virtual_network_subnet_match: bool | None | Unset = UNSET
    subscription_match: bool | None | Unset = UNSET
    summary: WorkerConfigurationStatusResult | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        has_service_endpoint_microsoft_storage: bool | None | Unset
        if isinstance(self.has_service_endpoint_microsoft_storage, Unset):
            has_service_endpoint_microsoft_storage = UNSET
        else:
            has_service_endpoint_microsoft_storage = self.has_service_endpoint_microsoft_storage

        virtual_network_found = self.virtual_network_found

        virtual_network_region_match: bool | None | Unset
        if isinstance(self.virtual_network_region_match, Unset):
            virtual_network_region_match = UNSET
        else:
            virtual_network_region_match = self.virtual_network_region_match

        network_security_group_found: bool | None | Unset
        if isinstance(self.network_security_group_found, Unset):
            network_security_group_found = UNSET
        else:
            network_security_group_found = self.network_security_group_found

        network_security_group_region_match: bool | None | Unset
        if isinstance(self.network_security_group_region_match, Unset):
            network_security_group_region_match = UNSET
        else:
            network_security_group_region_match = self.network_security_group_region_match

        network_security_group_deleted: bool | None | Unset
        if isinstance(self.network_security_group_deleted, Unset):
            network_security_group_deleted = UNSET
        else:
            network_security_group_deleted = self.network_security_group_deleted

        virtual_network_subnet_match: bool | None | Unset
        if isinstance(self.virtual_network_subnet_match, Unset):
            virtual_network_subnet_match = UNSET
        else:
            virtual_network_subnet_match = self.virtual_network_subnet_match

        subscription_match: bool | None | Unset
        if isinstance(self.subscription_match, Unset):
            subscription_match = UNSET
        else:
            subscription_match = self.subscription_match

        summary: str | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if has_service_endpoint_microsoft_storage is not UNSET:
            field_dict["hasServiceEndpointMicrosoftStorage"] = has_service_endpoint_microsoft_storage
        if virtual_network_found is not UNSET:
            field_dict["virtualNetworkFound"] = virtual_network_found
        if virtual_network_region_match is not UNSET:
            field_dict["virtualNetworkRegionMatch"] = virtual_network_region_match
        if network_security_group_found is not UNSET:
            field_dict["networkSecurityGroupFound"] = network_security_group_found
        if network_security_group_region_match is not UNSET:
            field_dict["networkSecurityGroupRegionMatch"] = network_security_group_region_match
        if network_security_group_deleted is not UNSET:
            field_dict["networkSecurityGroupDeleted"] = network_security_group_deleted
        if virtual_network_subnet_match is not UNSET:
            field_dict["virtualNetworkSubnetMatch"] = virtual_network_subnet_match
        if subscription_match is not UNSET:
            field_dict["subscriptionMatch"] = subscription_match
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_has_service_endpoint_microsoft_storage(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_service_endpoint_microsoft_storage = _parse_has_service_endpoint_microsoft_storage(
            d.pop("hasServiceEndpointMicrosoftStorage", UNSET)
        )

        virtual_network_found = d.pop("virtualNetworkFound", UNSET)

        def _parse_virtual_network_region_match(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        virtual_network_region_match = _parse_virtual_network_region_match(d.pop("virtualNetworkRegionMatch", UNSET))

        def _parse_network_security_group_found(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        network_security_group_found = _parse_network_security_group_found(d.pop("networkSecurityGroupFound", UNSET))

        def _parse_network_security_group_region_match(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        network_security_group_region_match = _parse_network_security_group_region_match(
            d.pop("networkSecurityGroupRegionMatch", UNSET)
        )

        def _parse_network_security_group_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        network_security_group_deleted = _parse_network_security_group_deleted(
            d.pop("networkSecurityGroupDeleted", UNSET)
        )

        def _parse_virtual_network_subnet_match(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        virtual_network_subnet_match = _parse_virtual_network_subnet_match(d.pop("virtualNetworkSubnetMatch", UNSET))

        def _parse_subscription_match(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        subscription_match = _parse_subscription_match(d.pop("subscriptionMatch", UNSET))

        _summary = d.pop("summary", UNSET)
        summary: WorkerConfigurationStatusResult | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = WorkerConfigurationStatusResult(_summary)

        worker_network_configuration_status = cls(
            has_service_endpoint_microsoft_storage=has_service_endpoint_microsoft_storage,
            virtual_network_found=virtual_network_found,
            virtual_network_region_match=virtual_network_region_match,
            network_security_group_found=network_security_group_found,
            network_security_group_region_match=network_security_group_region_match,
            network_security_group_deleted=network_security_group_deleted,
            virtual_network_subnet_match=virtual_network_subnet_match,
            subscription_match=subscription_match,
            summary=summary,
        )

        return worker_network_configuration_status
