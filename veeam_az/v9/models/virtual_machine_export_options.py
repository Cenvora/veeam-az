from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_destination_filter_options import BackupDestinationFilterOptions
from ..models.protection_status import ProtectionStatus
from ..models.virtual_machine_exists_state import VirtualMachineExistsState
from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualMachineExportOptions")


@_attrs_define
class VirtualMachineExportOptions:
    """
    Attributes:
        virtual_machine_ids (list[str] | None | Unset): Specifies the system IDs assigned in the Veeam Backup for
            Microsoft Azure REST API to the Azure VMs whose data will be exported.
        subscription_id (None | Unset | UUID):
        resource_group_id (None | str | Unset):
        tenant_id (None | str | Unset):
        service_account_id (None | str | Unset):
        region_ids (list[str] | None | Unset):
        search_pattern (None | str | Unset):
        protection_status (list[ProtectionStatus] | None | Unset):
        backup_destination (list[BackupDestinationFilterOptions] | None | Unset):
        exists_state (VirtualMachineExistsState | Unset):
        vm_from_protected_regions (bool | None | Unset):
    """

    virtual_machine_ids: list[str] | None | Unset = UNSET
    subscription_id: None | Unset | UUID = UNSET
    resource_group_id: None | str | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    service_account_id: None | str | Unset = UNSET
    region_ids: list[str] | None | Unset = UNSET
    search_pattern: None | str | Unset = UNSET
    protection_status: list[ProtectionStatus] | None | Unset = UNSET
    backup_destination: list[BackupDestinationFilterOptions] | None | Unset = UNSET
    exists_state: VirtualMachineExistsState | Unset = UNSET
    vm_from_protected_regions: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        virtual_machine_ids: list[str] | None | Unset
        if isinstance(self.virtual_machine_ids, Unset):
            virtual_machine_ids = UNSET
        elif isinstance(self.virtual_machine_ids, list):
            virtual_machine_ids = self.virtual_machine_ids

        else:
            virtual_machine_ids = self.virtual_machine_ids

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        resource_group_id: None | str | Unset
        if isinstance(self.resource_group_id, Unset):
            resource_group_id = UNSET
        else:
            resource_group_id = self.resource_group_id

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id

        region_ids: list[str] | None | Unset
        if isinstance(self.region_ids, Unset):
            region_ids = UNSET
        elif isinstance(self.region_ids, list):
            region_ids = self.region_ids

        else:
            region_ids = self.region_ids

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        protection_status: list[str] | None | Unset
        if isinstance(self.protection_status, Unset):
            protection_status = UNSET
        elif isinstance(self.protection_status, list):
            protection_status = []
            for protection_status_type_0_item_data in self.protection_status:
                protection_status_type_0_item = protection_status_type_0_item_data.value
                protection_status.append(protection_status_type_0_item)

        else:
            protection_status = self.protection_status

        backup_destination: list[str] | None | Unset
        if isinstance(self.backup_destination, Unset):
            backup_destination = UNSET
        elif isinstance(self.backup_destination, list):
            backup_destination = []
            for backup_destination_type_0_item_data in self.backup_destination:
                backup_destination_type_0_item = backup_destination_type_0_item_data.value
                backup_destination.append(backup_destination_type_0_item)

        else:
            backup_destination = self.backup_destination

        exists_state: str | Unset = UNSET
        if not isinstance(self.exists_state, Unset):
            exists_state = self.exists_state.value

        vm_from_protected_regions: bool | None | Unset
        if isinstance(self.vm_from_protected_regions, Unset):
            vm_from_protected_regions = UNSET
        else:
            vm_from_protected_regions = self.vm_from_protected_regions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if virtual_machine_ids is not UNSET:
            field_dict["virtualMachineIds"] = virtual_machine_ids
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if resource_group_id is not UNSET:
            field_dict["resourceGroupId"] = resource_group_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if region_ids is not UNSET:
            field_dict["regionIds"] = region_ids
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern
        if protection_status is not UNSET:
            field_dict["protectionStatus"] = protection_status
        if backup_destination is not UNSET:
            field_dict["backupDestination"] = backup_destination
        if exists_state is not UNSET:
            field_dict["existsState"] = exists_state
        if vm_from_protected_regions is not UNSET:
            field_dict["vmFromProtectedRegions"] = vm_from_protected_regions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_virtual_machine_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                virtual_machine_ids_type_0 = cast(list[str], data)

                return virtual_machine_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        virtual_machine_ids = _parse_virtual_machine_ids(d.pop("virtualMachineIds", UNSET))

        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_resource_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_id = _parse_resource_group_id(d.pop("resourceGroupId", UNSET))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        def _parse_region_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                region_ids_type_0 = cast(list[str], data)

                return region_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        region_ids = _parse_region_ids(d.pop("regionIds", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        def _parse_protection_status(data: object) -> list[ProtectionStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protection_status_type_0 = []
                _protection_status_type_0 = data
                for protection_status_type_0_item_data in _protection_status_type_0:
                    protection_status_type_0_item = ProtectionStatus(protection_status_type_0_item_data)

                    protection_status_type_0.append(protection_status_type_0_item)

                return protection_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProtectionStatus] | None | Unset, data)

        protection_status = _parse_protection_status(d.pop("protectionStatus", UNSET))

        def _parse_backup_destination(data: object) -> list[BackupDestinationFilterOptions] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backup_destination_type_0 = []
                _backup_destination_type_0 = data
                for backup_destination_type_0_item_data in _backup_destination_type_0:
                    backup_destination_type_0_item = BackupDestinationFilterOptions(backup_destination_type_0_item_data)

                    backup_destination_type_0.append(backup_destination_type_0_item)

                return backup_destination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BackupDestinationFilterOptions] | None | Unset, data)

        backup_destination = _parse_backup_destination(d.pop("backupDestination", UNSET))

        _exists_state = d.pop("existsState", UNSET)
        exists_state: VirtualMachineExistsState | Unset
        if isinstance(_exists_state, Unset):
            exists_state = UNSET
        else:
            exists_state = VirtualMachineExistsState(_exists_state)

        def _parse_vm_from_protected_regions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        vm_from_protected_regions = _parse_vm_from_protected_regions(d.pop("vmFromProtectedRegions", UNSET))

        virtual_machine_export_options = cls(
            virtual_machine_ids=virtual_machine_ids,
            subscription_id=subscription_id,
            resource_group_id=resource_group_id,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            region_ids=region_ids,
            search_pattern=search_pattern,
            protection_status=protection_status,
            backup_destination=backup_destination,
            exists_state=exists_state,
            vm_from_protected_regions=vm_from_protected_regions,
        )

        return virtual_machine_export_options
