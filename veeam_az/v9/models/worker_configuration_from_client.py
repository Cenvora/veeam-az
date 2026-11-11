from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerConfigurationFromClient")


@_attrs_define
class WorkerConfigurationFromClient:
    """
    Attributes:
        subnet (str):
        virtual_network_resource_id (str):
        region_id (str):
        virtual_machine_type (str):
        min_instances (int | Unset):
        max_instances (int | Unset):
        network_security_group_id (None | str | Unset):
        forbid_public_ip (bool | None | Unset):
    """

    subnet: str
    virtual_network_resource_id: str
    region_id: str
    virtual_machine_type: str
    min_instances: int | Unset = UNSET
    max_instances: int | Unset = UNSET
    network_security_group_id: None | str | Unset = UNSET
    forbid_public_ip: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subnet = self.subnet

        virtual_network_resource_id = self.virtual_network_resource_id

        region_id = self.region_id

        virtual_machine_type = self.virtual_machine_type

        min_instances = self.min_instances

        max_instances = self.max_instances

        network_security_group_id: None | str | Unset
        if isinstance(self.network_security_group_id, Unset):
            network_security_group_id = UNSET
        else:
            network_security_group_id = self.network_security_group_id

        forbid_public_ip: bool | None | Unset
        if isinstance(self.forbid_public_ip, Unset):
            forbid_public_ip = UNSET
        else:
            forbid_public_ip = self.forbid_public_ip

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "subnet": subnet,
                "virtualNetworkResourceId": virtual_network_resource_id,
                "regionId": region_id,
                "virtualMachineType": virtual_machine_type,
            }
        )
        if min_instances is not UNSET:
            field_dict["minInstances"] = min_instances
        if max_instances is not UNSET:
            field_dict["maxInstances"] = max_instances
        if network_security_group_id is not UNSET:
            field_dict["networkSecurityGroupId"] = network_security_group_id
        if forbid_public_ip is not UNSET:
            field_dict["forbidPublicIp"] = forbid_public_ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subnet = d.pop("subnet")

        virtual_network_resource_id = d.pop("virtualNetworkResourceId")

        region_id = d.pop("regionId")

        virtual_machine_type = d.pop("virtualMachineType")

        min_instances = d.pop("minInstances", UNSET)

        max_instances = d.pop("maxInstances", UNSET)

        def _parse_network_security_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_security_group_id = _parse_network_security_group_id(d.pop("networkSecurityGroupId", UNSET))

        def _parse_forbid_public_ip(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        forbid_public_ip = _parse_forbid_public_ip(d.pop("forbidPublicIp", UNSET))

        worker_configuration_from_client = cls(
            subnet=subnet,
            virtual_network_resource_id=virtual_network_resource_id,
            region_id=region_id,
            virtual_machine_type=virtual_machine_type,
            min_instances=min_instances,
            max_instances=max_instances,
            network_security_group_id=network_security_group_id,
            forbid_public_ip=forbid_public_ip,
        )

        return worker_configuration_from_client
