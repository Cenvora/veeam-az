from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.azure_environment import AzureEnvironment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disabled_sections import DisabledSections


T = TypeVar("T", bound="ServerInfo")


@_attrs_define
class ServerInfo:
    """
    Attributes:
        subscription_id (UUID | Unset): Microsoft Azure ID assigned to the subscription to which the Azure VM belongs.
        server_name (None | str | Unset): Name of the server on which the backup appliance is run.
        azure_region (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the
            Azure region to which the Azure VM belongs.
        azure_region_name (None | str | Unset): Name of the Azure region to which the Azure VM belongs.
        azure_vm_id (None | str | Unset): Resource ID of the Azure VM.
        resource_group (None | str | Unset): Name of the resource group to which the Azure VM belongs.
        azure_environment (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        virtual_machine_unique_id (None | str | Unset): Azure VM Unique ID of the Azure VM running the backup appliance.
        disabled_sections (DisabledSections | Unset): Information that is not displayed in the Veeam Backup for
            Microsoft Azure UI.
    """

    subscription_id: UUID | Unset = UNSET
    server_name: None | str | Unset = UNSET
    azure_region: None | str | Unset = UNSET
    azure_region_name: None | str | Unset = UNSET
    azure_vm_id: None | str | Unset = UNSET
    resource_group: None | str | Unset = UNSET
    azure_environment: AzureEnvironment | Unset = UNSET
    virtual_machine_unique_id: None | str | Unset = UNSET
    disabled_sections: DisabledSections | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        azure_region: None | str | Unset
        if isinstance(self.azure_region, Unset):
            azure_region = UNSET
        else:
            azure_region = self.azure_region

        azure_region_name: None | str | Unset
        if isinstance(self.azure_region_name, Unset):
            azure_region_name = UNSET
        else:
            azure_region_name = self.azure_region_name

        azure_vm_id: None | str | Unset
        if isinstance(self.azure_vm_id, Unset):
            azure_vm_id = UNSET
        else:
            azure_vm_id = self.azure_vm_id

        resource_group: None | str | Unset
        if isinstance(self.resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = self.resource_group

        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        virtual_machine_unique_id: None | str | Unset
        if isinstance(self.virtual_machine_unique_id, Unset):
            virtual_machine_unique_id = UNSET
        else:
            virtual_machine_unique_id = self.virtual_machine_unique_id

        disabled_sections: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disabled_sections, Unset):
            disabled_sections = self.disabled_sections.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if azure_region is not UNSET:
            field_dict["azureRegion"] = azure_region
        if azure_region_name is not UNSET:
            field_dict["azureRegionName"] = azure_region_name
        if azure_vm_id is not UNSET:
            field_dict["azureVmId"] = azure_vm_id
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if virtual_machine_unique_id is not UNSET:
            field_dict["virtualMachineUniqueId"] = virtual_machine_unique_id
        if disabled_sections is not UNSET:
            field_dict["DisabledSections"] = disabled_sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disabled_sections import DisabledSections

        d = dict(src_dict)
        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("serverName", UNSET))

        def _parse_azure_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_region = _parse_azure_region(d.pop("azureRegion", UNSET))

        def _parse_azure_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_region_name = _parse_azure_region_name(d.pop("azureRegionName", UNSET))

        def _parse_azure_vm_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_vm_id = _parse_azure_vm_id(d.pop("azureVmId", UNSET))

        def _parse_resource_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group = _parse_resource_group(d.pop("resourceGroup", UNSET))

        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureEnvironment | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureEnvironment(_azure_environment)

        def _parse_virtual_machine_unique_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_machine_unique_id = _parse_virtual_machine_unique_id(d.pop("virtualMachineUniqueId", UNSET))

        _disabled_sections = d.pop("DisabledSections", UNSET)
        disabled_sections: DisabledSections | Unset
        if isinstance(_disabled_sections, Unset):
            disabled_sections = UNSET
        else:
            disabled_sections = DisabledSections.from_dict(_disabled_sections)

        server_info = cls(
            subscription_id=subscription_id,
            server_name=server_name,
            azure_region=azure_region,
            azure_region_name=azure_region_name,
            azure_vm_id=azure_vm_id,
            resource_group=resource_group,
            azure_environment=azure_environment,
            virtual_machine_unique_id=virtual_machine_unique_id,
            disabled_sections=disabled_sections,
        )

        return server_info
