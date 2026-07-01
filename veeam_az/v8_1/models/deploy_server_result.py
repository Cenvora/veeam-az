from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeployServerResult")


@_attrs_define
class DeployServerResult:
    """
    Attributes:
        virtual_machine_name (str | Unset):
        virtual_machine_id (str | Unset):
        resource_group_name (None | str | Unset):
        resource_group_created (bool | Unset):
        virtual_network_id (None | str | Unset):
        virtual_network_created (bool | Unset):
        subnet_name (str | Unset):
        network_security_group_id (None | str | Unset):
        network_security_group_created (bool | Unset):
        public_ip_address (None | str | Unset):
        public_ip_address_id (None | str | Unset):
        public_ip_address_created (bool | Unset):
        azure_application_id (None | Unset | UUID):
        azure_application_created (bool | Unset):
        dns_name (str | Unset):
        network_interface_id (None | str | Unset):
        service_account_id (None | str | Unset):
    """

    virtual_machine_name: str | Unset = UNSET
    virtual_machine_id: str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    resource_group_created: bool | Unset = UNSET
    virtual_network_id: None | str | Unset = UNSET
    virtual_network_created: bool | Unset = UNSET
    subnet_name: str | Unset = UNSET
    network_security_group_id: None | str | Unset = UNSET
    network_security_group_created: bool | Unset = UNSET
    public_ip_address: None | str | Unset = UNSET
    public_ip_address_id: None | str | Unset = UNSET
    public_ip_address_created: bool | Unset = UNSET
    azure_application_id: None | Unset | UUID = UNSET
    azure_application_created: bool | Unset = UNSET
    dns_name: str | Unset = UNSET
    network_interface_id: None | str | Unset = UNSET
    service_account_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        virtual_machine_name = self.virtual_machine_name

        virtual_machine_id = self.virtual_machine_id

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        resource_group_created = self.resource_group_created

        virtual_network_id: None | str | Unset
        if isinstance(self.virtual_network_id, Unset):
            virtual_network_id = UNSET
        else:
            virtual_network_id = self.virtual_network_id

        virtual_network_created = self.virtual_network_created

        subnet_name = self.subnet_name

        network_security_group_id: None | str | Unset
        if isinstance(self.network_security_group_id, Unset):
            network_security_group_id = UNSET
        else:
            network_security_group_id = self.network_security_group_id

        network_security_group_created = self.network_security_group_created

        public_ip_address: None | str | Unset
        if isinstance(self.public_ip_address, Unset):
            public_ip_address = UNSET
        else:
            public_ip_address = self.public_ip_address

        public_ip_address_id: None | str | Unset
        if isinstance(self.public_ip_address_id, Unset):
            public_ip_address_id = UNSET
        else:
            public_ip_address_id = self.public_ip_address_id

        public_ip_address_created = self.public_ip_address_created

        azure_application_id: None | str | Unset
        if isinstance(self.azure_application_id, Unset):
            azure_application_id = UNSET
        elif isinstance(self.azure_application_id, UUID):
            azure_application_id = str(self.azure_application_id)
        else:
            azure_application_id = self.azure_application_id

        azure_application_created = self.azure_application_created

        dns_name = self.dns_name

        network_interface_id: None | str | Unset
        if isinstance(self.network_interface_id, Unset):
            network_interface_id = UNSET
        else:
            network_interface_id = self.network_interface_id

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if virtual_machine_name is not UNSET:
            field_dict["virtualMachineName"] = virtual_machine_name
        if virtual_machine_id is not UNSET:
            field_dict["virtualMachineId"] = virtual_machine_id
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if resource_group_created is not UNSET:
            field_dict["resourceGroupCreated"] = resource_group_created
        if virtual_network_id is not UNSET:
            field_dict["virtualNetworkId"] = virtual_network_id
        if virtual_network_created is not UNSET:
            field_dict["virtualNetworkCreated"] = virtual_network_created
        if subnet_name is not UNSET:
            field_dict["subnetName"] = subnet_name
        if network_security_group_id is not UNSET:
            field_dict["networkSecurityGroupId"] = network_security_group_id
        if network_security_group_created is not UNSET:
            field_dict["networkSecurityGroupCreated"] = network_security_group_created
        if public_ip_address is not UNSET:
            field_dict["publicIpAddress"] = public_ip_address
        if public_ip_address_id is not UNSET:
            field_dict["publicIpAddressId"] = public_ip_address_id
        if public_ip_address_created is not UNSET:
            field_dict["publicIpAddressCreated"] = public_ip_address_created
        if azure_application_id is not UNSET:
            field_dict["azureApplicationId"] = azure_application_id
        if azure_application_created is not UNSET:
            field_dict["azureApplicationCreated"] = azure_application_created
        if dns_name is not UNSET:
            field_dict["dnsName"] = dns_name
        if network_interface_id is not UNSET:
            field_dict["networkInterfaceId"] = network_interface_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        virtual_machine_name = d.pop("virtualMachineName", UNSET)

        virtual_machine_id = d.pop("virtualMachineId", UNSET)

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        resource_group_created = d.pop("resourceGroupCreated", UNSET)

        def _parse_virtual_network_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_network_id = _parse_virtual_network_id(d.pop("virtualNetworkId", UNSET))

        virtual_network_created = d.pop("virtualNetworkCreated", UNSET)

        subnet_name = d.pop("subnetName", UNSET)

        def _parse_network_security_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_security_group_id = _parse_network_security_group_id(d.pop("networkSecurityGroupId", UNSET))

        network_security_group_created = d.pop("networkSecurityGroupCreated", UNSET)

        def _parse_public_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_ip_address = _parse_public_ip_address(d.pop("publicIpAddress", UNSET))

        def _parse_public_ip_address_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_ip_address_id = _parse_public_ip_address_id(d.pop("publicIpAddressId", UNSET))

        public_ip_address_created = d.pop("publicIpAddressCreated", UNSET)

        def _parse_azure_application_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                azure_application_id_type_0 = UUID(data)

                return azure_application_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        azure_application_id = _parse_azure_application_id(d.pop("azureApplicationId", UNSET))

        azure_application_created = d.pop("azureApplicationCreated", UNSET)

        dns_name = d.pop("dnsName", UNSET)

        def _parse_network_interface_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_interface_id = _parse_network_interface_id(d.pop("networkInterfaceId", UNSET))

        def _parse_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        deploy_server_result = cls(
            virtual_machine_name=virtual_machine_name,
            virtual_machine_id=virtual_machine_id,
            resource_group_name=resource_group_name,
            resource_group_created=resource_group_created,
            virtual_network_id=virtual_network_id,
            virtual_network_created=virtual_network_created,
            subnet_name=subnet_name,
            network_security_group_id=network_security_group_id,
            network_security_group_created=network_security_group_created,
            public_ip_address=public_ip_address,
            public_ip_address_id=public_ip_address_id,
            public_ip_address_created=public_ip_address_created,
            azure_application_id=azure_application_id,
            azure_application_created=azure_application_created,
            dns_name=dns_name,
            network_interface_id=network_interface_id,
            service_account_id=service_account_id,
        )

        return deploy_server_result
