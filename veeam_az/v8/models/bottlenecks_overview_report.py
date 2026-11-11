from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cpu_quota_state import CpuQuotaState
from ..models.storage_account_bottleneck_state import StorageAccountBottleneckState
from ..models.worker_wait_time_state import WorkerWaitTimeState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BottlenecksOverviewReport")


@_attrs_define
class BottlenecksOverviewReport:
    """
    Attributes:
        worker_wait_time_state (WorkerWaitTimeState | Unset): State of the total workers waiting time.
        average_workers_wait_time_min (str | Unset): Average waiting time of the workers (in minutes).
        maximum_workers_wait_time_min (str | Unset): Maximum workers waiting time (in minutes).
        worker_bottleneck_region (str | Unset): Name of an Azure region in which the maximum workers waiting time is
            reached.
        cpu_quota_state (CpuQuotaState | Unset): State of the vCPU quota.
        cpu_quota_bottleneck_region (str | Unset): Name of an Azure region in which vCPU quota is reached.
        storage_account_bottleneck_state (StorageAccountBottleneckState | Unset): State of the storage account.
        storage_account_bottleneck_region (str | Unset): Name of an Azure region in which the storage account is
            throttled.
        storage_account_bottleneck_name (str | Unset): Name of the throttled storage account.
        storage_account_bottleneck_resource_id (str | Unset): Resource ID of the throttled storage account.
    """

    worker_wait_time_state: WorkerWaitTimeState | Unset = UNSET
    average_workers_wait_time_min: str | Unset = UNSET
    maximum_workers_wait_time_min: str | Unset = UNSET
    worker_bottleneck_region: str | Unset = UNSET
    cpu_quota_state: CpuQuotaState | Unset = UNSET
    cpu_quota_bottleneck_region: str | Unset = UNSET
    storage_account_bottleneck_state: StorageAccountBottleneckState | Unset = UNSET
    storage_account_bottleneck_region: str | Unset = UNSET
    storage_account_bottleneck_name: str | Unset = UNSET
    storage_account_bottleneck_resource_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        worker_wait_time_state: str | Unset = UNSET
        if not isinstance(self.worker_wait_time_state, Unset):
            worker_wait_time_state = self.worker_wait_time_state.value

        average_workers_wait_time_min = self.average_workers_wait_time_min

        maximum_workers_wait_time_min = self.maximum_workers_wait_time_min

        worker_bottleneck_region = self.worker_bottleneck_region

        cpu_quota_state: str | Unset = UNSET
        if not isinstance(self.cpu_quota_state, Unset):
            cpu_quota_state = self.cpu_quota_state.value

        cpu_quota_bottleneck_region = self.cpu_quota_bottleneck_region

        storage_account_bottleneck_state: str | Unset = UNSET
        if not isinstance(self.storage_account_bottleneck_state, Unset):
            storage_account_bottleneck_state = self.storage_account_bottleneck_state.value

        storage_account_bottleneck_region = self.storage_account_bottleneck_region

        storage_account_bottleneck_name = self.storage_account_bottleneck_name

        storage_account_bottleneck_resource_id = self.storage_account_bottleneck_resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if worker_wait_time_state is not UNSET:
            field_dict["workerWaitTimeState"] = worker_wait_time_state
        if average_workers_wait_time_min is not UNSET:
            field_dict["averageWorkersWaitTimeMin"] = average_workers_wait_time_min
        if maximum_workers_wait_time_min is not UNSET:
            field_dict["maximumWorkersWaitTimeMin"] = maximum_workers_wait_time_min
        if worker_bottleneck_region is not UNSET:
            field_dict["workerBottleneckRegion"] = worker_bottleneck_region
        if cpu_quota_state is not UNSET:
            field_dict["cpuQuotaState"] = cpu_quota_state
        if cpu_quota_bottleneck_region is not UNSET:
            field_dict["cpuQuotaBottleneckRegion"] = cpu_quota_bottleneck_region
        if storage_account_bottleneck_state is not UNSET:
            field_dict["storageAccountBottleneckState"] = storage_account_bottleneck_state
        if storage_account_bottleneck_region is not UNSET:
            field_dict["storageAccountBottleneckRegion"] = storage_account_bottleneck_region
        if storage_account_bottleneck_name is not UNSET:
            field_dict["storageAccountBottleneckName"] = storage_account_bottleneck_name
        if storage_account_bottleneck_resource_id is not UNSET:
            field_dict["storageAccountBottleneckResourceId"] = storage_account_bottleneck_resource_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _worker_wait_time_state = d.pop("workerWaitTimeState", UNSET)
        worker_wait_time_state: WorkerWaitTimeState | Unset
        if isinstance(_worker_wait_time_state, Unset):
            worker_wait_time_state = UNSET
        else:
            worker_wait_time_state = WorkerWaitTimeState(_worker_wait_time_state)

        average_workers_wait_time_min = d.pop("averageWorkersWaitTimeMin", UNSET)

        maximum_workers_wait_time_min = d.pop("maximumWorkersWaitTimeMin", UNSET)

        worker_bottleneck_region = d.pop("workerBottleneckRegion", UNSET)

        _cpu_quota_state = d.pop("cpuQuotaState", UNSET)
        cpu_quota_state: CpuQuotaState | Unset
        if isinstance(_cpu_quota_state, Unset):
            cpu_quota_state = UNSET
        else:
            cpu_quota_state = CpuQuotaState(_cpu_quota_state)

        cpu_quota_bottleneck_region = d.pop("cpuQuotaBottleneckRegion", UNSET)

        _storage_account_bottleneck_state = d.pop("storageAccountBottleneckState", UNSET)
        storage_account_bottleneck_state: StorageAccountBottleneckState | Unset
        if isinstance(_storage_account_bottleneck_state, Unset):
            storage_account_bottleneck_state = UNSET
        else:
            storage_account_bottleneck_state = StorageAccountBottleneckState(_storage_account_bottleneck_state)

        storage_account_bottleneck_region = d.pop("storageAccountBottleneckRegion", UNSET)

        storage_account_bottleneck_name = d.pop("storageAccountBottleneckName", UNSET)

        storage_account_bottleneck_resource_id = d.pop("storageAccountBottleneckResourceId", UNSET)

        bottlenecks_overview_report = cls(
            worker_wait_time_state=worker_wait_time_state,
            average_workers_wait_time_min=average_workers_wait_time_min,
            maximum_workers_wait_time_min=maximum_workers_wait_time_min,
            worker_bottleneck_region=worker_bottleneck_region,
            cpu_quota_state=cpu_quota_state,
            cpu_quota_bottleneck_region=cpu_quota_bottleneck_region,
            storage_account_bottleneck_state=storage_account_bottleneck_state,
            storage_account_bottleneck_region=storage_account_bottleneck_region,
            storage_account_bottleneck_name=storage_account_bottleneck_name,
            storage_account_bottleneck_resource_id=storage_account_bottleneck_resource_id,
        )

        bottlenecks_overview_report.additional_properties = d
        return bottlenecks_overview_report

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
