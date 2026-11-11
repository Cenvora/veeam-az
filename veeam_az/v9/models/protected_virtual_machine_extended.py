from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.os_type_nullable import OSTypeNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_vm_state import ProtectionVMState


T = TypeVar("T", bound="ProtectedVirtualMachineExtended")


@_attrs_define
class ProtectedVirtualMachineExtended:
    """
    Attributes:
        id (None | str | Unset):
        name (None | str | Unset):
        os_type (OSTypeNullable | Unset): Type of the operating system installed on the Azure VM.
        region_name (None | str | Unset):
        resource_group_name (None | str | Unset):
        vm_size (None | str | Unset):
        has_ephemeral_os_disk (bool | Unset):
        last_backup (datetime.datetime | Unset):
        subscription_id (UUID | Unset):
        tenant_id (None | str | Unset):
        policy_name (None | str | Unset):
        protection_state (ProtectionVMState | Unset):
        is_controller (bool | Unset):
        has_running_flr_session (bool | Unset):
        backup_size_bytes (int | None | Unset):
        archive_size_bytes (int | None | Unset):
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    os_type: OSTypeNullable | Unset = UNSET
    region_name: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    vm_size: None | str | Unset = UNSET
    has_ephemeral_os_disk: bool | Unset = UNSET
    last_backup: datetime.datetime | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    protection_state: ProtectionVMState | Unset = UNSET
    is_controller: bool | Unset = UNSET
    has_running_flr_session: bool | Unset = UNSET
    backup_size_bytes: int | None | Unset = UNSET
    archive_size_bytes: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        os_type: str | Unset = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        resource_group_name: None | str | Unset
        if isinstance(self.resource_group_name, Unset):
            resource_group_name = UNSET
        else:
            resource_group_name = self.resource_group_name

        vm_size: None | str | Unset
        if isinstance(self.vm_size, Unset):
            vm_size = UNSET
        else:
            vm_size = self.vm_size

        has_ephemeral_os_disk = self.has_ephemeral_os_disk

        last_backup: str | Unset = UNSET
        if not isinstance(self.last_backup, Unset):
            last_backup = self.last_backup.isoformat()

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        protection_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protection_state, Unset):
            protection_state = self.protection_state.to_dict()

        is_controller = self.is_controller

        has_running_flr_session = self.has_running_flr_session

        backup_size_bytes: int | None | Unset
        if isinstance(self.backup_size_bytes, Unset):
            backup_size_bytes = UNSET
        else:
            backup_size_bytes = self.backup_size_bytes

        archive_size_bytes: int | None | Unset
        if isinstance(self.archive_size_bytes, Unset):
            archive_size_bytes = UNSET
        else:
            archive_size_bytes = self.archive_size_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if vm_size is not UNSET:
            field_dict["vmSize"] = vm_size
        if has_ephemeral_os_disk is not UNSET:
            field_dict["hasEphemeralOsDisk"] = has_ephemeral_os_disk
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if protection_state is not UNSET:
            field_dict["protectionState"] = protection_state
        if is_controller is not UNSET:
            field_dict["isController"] = is_controller
        if has_running_flr_session is not UNSET:
            field_dict["hasRunningFlrSession"] = has_running_flr_session
        if backup_size_bytes is not UNSET:
            field_dict["backupSizeBytes"] = backup_size_bytes
        if archive_size_bytes is not UNSET:
            field_dict["archiveSizeBytes"] = archive_size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_vm_state import ProtectionVMState

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _os_type = d.pop("osType", UNSET)
        os_type: OSTypeNullable | Unset
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = OSTypeNullable(_os_type)

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_resource_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_group_name = _parse_resource_group_name(d.pop("resourceGroupName", UNSET))

        def _parse_vm_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_size = _parse_vm_size(d.pop("vmSize", UNSET))

        has_ephemeral_os_disk = d.pop("hasEphemeralOsDisk", UNSET)

        _last_backup = d.pop("lastBackup", UNSET)
        last_backup: datetime.datetime | Unset
        if isinstance(_last_backup, Unset):
            last_backup = UNSET
        else:
            last_backup = isoparse(_last_backup)

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

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        _protection_state = d.pop("protectionState", UNSET)
        protection_state: ProtectionVMState | Unset
        if isinstance(_protection_state, Unset):
            protection_state = UNSET
        else:
            protection_state = ProtectionVMState.from_dict(_protection_state)

        is_controller = d.pop("isController", UNSET)

        has_running_flr_session = d.pop("hasRunningFlrSession", UNSET)

        def _parse_backup_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_size_bytes = _parse_backup_size_bytes(d.pop("backupSizeBytes", UNSET))

        def _parse_archive_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archive_size_bytes = _parse_archive_size_bytes(d.pop("archiveSizeBytes", UNSET))

        protected_virtual_machine_extended = cls(
            id=id,
            name=name,
            os_type=os_type,
            region_name=region_name,
            resource_group_name=resource_group_name,
            vm_size=vm_size,
            has_ephemeral_os_disk=has_ephemeral_os_disk,
            last_backup=last_backup,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            policy_name=policy_name,
            protection_state=protection_state,
            is_controller=is_controller,
            has_running_flr_session=has_running_flr_session,
            backup_size_bytes=backup_size_bytes,
            archive_size_bytes=archive_size_bytes,
        )

        return protected_virtual_machine_extended
