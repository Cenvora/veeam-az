from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.worker_profile_type import WorkerProfileType
from ..models.worker_status import WorkerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Worker")


@_attrs_define
class Worker:
    r"""
    Attributes:
        resource_id (None | str | Unset): Resource ID of the worker instance.
        name (None | str | Unset): Name of the worker instance.
        host (None | str | Unset): DNS name or an IP address of the worker instance.
        network (None | str | Unset): Name of the network to which the worker instance is connected.
        subnet_name (None | str | Unset): Name of the subnet to which the worker instance is connected.
        instance_type (None | str | Unset): Type of the worker instance.
        availability_zone (None | str | Unset): \[Returned only if the availability zone is defined for the workers]
            Availability zone of an Azure region where the worker instance is launched.
        status (WorkerStatus | Unset): Status of the worker instance.
        region (None | str | Unset): Name of the Azure region where the worker instance is launched.
        region_id (None | str | Unset): Microsoft Azure ID assigned to a region where the worker instance is launched.
        profile (WorkerProfileType | Unset): Type of the worker instance profile.
    """

    resource_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    host: None | str | Unset = UNSET
    network: None | str | Unset = UNSET
    subnet_name: None | str | Unset = UNSET
    instance_type: None | str | Unset = UNSET
    availability_zone: None | str | Unset = UNSET
    status: WorkerStatus | Unset = UNSET
    region: None | str | Unset = UNSET
    region_id: None | str | Unset = UNSET
    profile: WorkerProfileType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        network: None | str | Unset
        if isinstance(self.network, Unset):
            network = UNSET
        else:
            network = self.network

        subnet_name: None | str | Unset
        if isinstance(self.subnet_name, Unset):
            subnet_name = UNSET
        else:
            subnet_name = self.subnet_name

        instance_type: None | str | Unset
        if isinstance(self.instance_type, Unset):
            instance_type = UNSET
        else:
            instance_type = self.instance_type

        availability_zone: None | str | Unset
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        profile: str | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if name is not UNSET:
            field_dict["name"] = name
        if host is not UNSET:
            field_dict["host"] = host
        if network is not UNSET:
            field_dict["network"] = network
        if subnet_name is not UNSET:
            field_dict["subnetName"] = subnet_name
        if instance_type is not UNSET:
            field_dict["instanceType"] = instance_type
        if availability_zone is not UNSET:
            field_dict["availabilityZone"] = availability_zone
        if status is not UNSET:
            field_dict["status"] = status
        if region is not UNSET:
            field_dict["region"] = region
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_network(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network = _parse_network(d.pop("network", UNSET))

        def _parse_subnet_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subnet_name = _parse_subnet_name(d.pop("subnetName", UNSET))

        def _parse_instance_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance_type = _parse_instance_type(d.pop("instanceType", UNSET))

        def _parse_availability_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        availability_zone = _parse_availability_zone(d.pop("availabilityZone", UNSET))

        _status = d.pop("status", UNSET)
        status: WorkerStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WorkerStatus(_status)

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_id = _parse_region_id(d.pop("regionId", UNSET))

        _profile = d.pop("profile", UNSET)
        profile: WorkerProfileType | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = WorkerProfileType(_profile)

        worker = cls(
            resource_id=resource_id,
            name=name,
            host=host,
            network=network,
            subnet_name=subnet_name,
            instance_type=instance_type,
            availability_zone=availability_zone,
            status=status,
            region=region,
            region_id=region_id,
            profile=profile,
        )

        return worker
