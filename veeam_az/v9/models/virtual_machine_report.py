from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.os_type import OSType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_state import ProtectionState


T = TypeVar("T", bound="VirtualMachineReport")


@_attrs_define
class VirtualMachineReport:
    """
    Attributes:
        id (None | str | Unset):
        tenant_id (None | str | Unset):
        subscription_id (None | str | Unset):
        account_ids (list[str] | None | Unset):
        name (None | str | Unset):
        os_type (OSType | Unset): Type of the operating system installed on the Azure VM.
        region_name (None | str | Unset):
        resource_group_name (None | str | Unset):
        total_size_in_gb (int | Unset):
        vm_size (None | str | Unset):
        dns_name (None | str | Unset):
        virtual_network (None | str | Unset):
        subnet (None | str | Unset):
        public_ip (None | str | Unset):
        private_ip (None | str | Unset):
        protection_state (ProtectionState | Unset):
    """

    id: None | str | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    subscription_id: None | str | Unset = UNSET
    account_ids: list[str] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    os_type: OSType | Unset = UNSET
    region_name: None | str | Unset = UNSET
    resource_group_name: None | str | Unset = UNSET
    total_size_in_gb: int | Unset = UNSET
    vm_size: None | str | Unset = UNSET
    dns_name: None | str | Unset = UNSET
    virtual_network: None | str | Unset = UNSET
    subnet: None | str | Unset = UNSET
    public_ip: None | str | Unset = UNSET
    private_ip: None | str | Unset = UNSET
    protection_state: ProtectionState | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = self.subscription_id

        account_ids: list[str] | None | Unset
        if isinstance(self.account_ids, Unset):
            account_ids = UNSET
        elif isinstance(self.account_ids, list):
            account_ids = self.account_ids

        else:
            account_ids = self.account_ids

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

        total_size_in_gb = self.total_size_in_gb

        vm_size: None | str | Unset
        if isinstance(self.vm_size, Unset):
            vm_size = UNSET
        else:
            vm_size = self.vm_size

        dns_name: None | str | Unset
        if isinstance(self.dns_name, Unset):
            dns_name = UNSET
        else:
            dns_name = self.dns_name

        virtual_network: None | str | Unset
        if isinstance(self.virtual_network, Unset):
            virtual_network = UNSET
        else:
            virtual_network = self.virtual_network

        subnet: None | str | Unset
        if isinstance(self.subnet, Unset):
            subnet = UNSET
        else:
            subnet = self.subnet

        public_ip: None | str | Unset
        if isinstance(self.public_ip, Unset):
            public_ip = UNSET
        else:
            public_ip = self.public_ip

        private_ip: None | str | Unset
        if isinstance(self.private_ip, Unset):
            private_ip = UNSET
        else:
            private_ip = self.private_ip

        protection_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protection_state, Unset):
            protection_state = self.protection_state.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids
        if name is not UNSET:
            field_dict["name"] = name
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if total_size_in_gb is not UNSET:
            field_dict["totalSizeInGB"] = total_size_in_gb
        if vm_size is not UNSET:
            field_dict["vmSize"] = vm_size
        if dns_name is not UNSET:
            field_dict["dnsName"] = dns_name
        if virtual_network is not UNSET:
            field_dict["virtualNetwork"] = virtual_network
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if public_ip is not UNSET:
            field_dict["publicIP"] = public_ip
        if private_ip is not UNSET:
            field_dict["privateIP"] = private_ip
        if protection_state is not UNSET:
            field_dict["protectionState"] = protection_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_state import ProtectionState

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_subscription_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_account_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                account_ids_type_0 = cast(list[str], data)

                return account_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        account_ids = _parse_account_ids(d.pop("accountIds", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _os_type = d.pop("osType", UNSET)
        os_type: OSType | Unset
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = OSType(_os_type)

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

        total_size_in_gb = d.pop("totalSizeInGB", UNSET)

        def _parse_vm_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_size = _parse_vm_size(d.pop("vmSize", UNSET))

        def _parse_dns_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dns_name = _parse_dns_name(d.pop("dnsName", UNSET))

        def _parse_virtual_network(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_network = _parse_virtual_network(d.pop("virtualNetwork", UNSET))

        def _parse_subnet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subnet = _parse_subnet(d.pop("subnet", UNSET))

        def _parse_public_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_ip = _parse_public_ip(d.pop("publicIP", UNSET))

        def _parse_private_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        private_ip = _parse_private_ip(d.pop("privateIP", UNSET))

        _protection_state = d.pop("protectionState", UNSET)
        protection_state: ProtectionState | Unset
        if isinstance(_protection_state, Unset):
            protection_state = UNSET
        else:
            protection_state = ProtectionState.from_dict(_protection_state)

        virtual_machine_report = cls(
            id=id,
            tenant_id=tenant_id,
            subscription_id=subscription_id,
            account_ids=account_ids,
            name=name,
            os_type=os_type,
            region_name=region_name,
            resource_group_name=resource_group_name,
            total_size_in_gb=total_size_in_gb,
            vm_size=vm_size,
            dns_name=dns_name,
            virtual_network=virtual_network,
            subnet=subnet,
            public_ip=public_ip,
            private_ip=private_ip,
            protection_state=protection_state,
        )

        return virtual_machine_report
