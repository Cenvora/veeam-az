from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_machine_to_alternative_restore_options import VirtualMachineToAlternativeRestoreOptions


T = TypeVar("T", bound="VirtualMachineRestoreOptions")


@_attrs_define
class VirtualMachineRestoreOptions:
    """Specifies Azure VM restore options.

    Attributes:
        reason (str): Specifies a reason for performing the restore operation.
        service_account_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft
            Azure REST API to a service account whose permissions will be used to perform the operation. </br> **Note**&#58;
            This parameter is required.
        source_service_account_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for
            Microsoft Azure REST API to a service account whose permissions were used to perform the backup operation.
        to_alternative (VirtualMachineToAlternativeRestoreOptions | Unset): /[Applies if restore is performed to a new
            location or with different settings/] Specifies Azure VM restore settings.
        start_vm_after_restore (bool | Unset): Defines whether to start the restored Azure VM after the restore
            operation completes.
    """

    reason: str
    service_account_id: None | str | Unset = UNSET
    source_service_account_id: None | str | Unset = UNSET
    to_alternative: VirtualMachineToAlternativeRestoreOptions | Unset = UNSET
    start_vm_after_restore: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id

        source_service_account_id: None | str | Unset
        if isinstance(self.source_service_account_id, Unset):
            source_service_account_id = UNSET
        else:
            source_service_account_id = self.source_service_account_id

        to_alternative: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_alternative, Unset):
            to_alternative = self.to_alternative.to_dict()

        start_vm_after_restore = self.start_vm_after_restore

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reason": reason,
            }
        )
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if source_service_account_id is not UNSET:
            field_dict["sourceServiceAccountId"] = source_service_account_id
        if to_alternative is not UNSET:
            field_dict["toAlternative"] = to_alternative
        if start_vm_after_restore is not UNSET:
            field_dict["startVmAfterRestore"] = start_vm_after_restore

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.virtual_machine_to_alternative_restore_options import VirtualMachineToAlternativeRestoreOptions

        d = dict(src_dict)
        reason = d.pop("reason")

        def _parse_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        def _parse_source_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_service_account_id = _parse_source_service_account_id(d.pop("sourceServiceAccountId", UNSET))

        _to_alternative = d.pop("toAlternative", UNSET)
        to_alternative: VirtualMachineToAlternativeRestoreOptions | Unset
        if isinstance(_to_alternative, Unset):
            to_alternative = UNSET
        else:
            to_alternative = VirtualMachineToAlternativeRestoreOptions.from_dict(_to_alternative)

        start_vm_after_restore = d.pop("startVmAfterRestore", UNSET)

        virtual_machine_restore_options = cls(
            reason=reason,
            service_account_id=service_account_id,
            source_service_account_id=source_service_account_id,
            to_alternative=to_alternative,
            start_vm_after_restore=start_vm_after_restore,
        )

        return virtual_machine_restore_options
