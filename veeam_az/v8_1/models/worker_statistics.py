from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkerStatistics")


@_attrs_define
class WorkerStatistics:
    """Statistics on worker instances.

    Attributes:
        count_of_workers (int | Unset): Total number of currently existing workers.
        running_workers (int | Unset): Total number of currently running workers.
        total_cycle_time (str | Unset): Total time of deployment or allocation and deletion or deallocation of all
            workers running during the past 24 hours.
        used_workers (int | Unset): Total number of workers that have been used during the past 24 hours.
        deployed_workers (int | Unset): Total number of workers deployed for all backup policies during the past 24
            hours.
    """

    count_of_workers: int | Unset = UNSET
    running_workers: int | Unset = UNSET
    total_cycle_time: str | Unset = UNSET
    used_workers: int | Unset = UNSET
    deployed_workers: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count_of_workers = self.count_of_workers

        running_workers = self.running_workers

        total_cycle_time = self.total_cycle_time

        used_workers = self.used_workers

        deployed_workers = self.deployed_workers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if count_of_workers is not UNSET:
            field_dict["countOfWorkers"] = count_of_workers
        if running_workers is not UNSET:
            field_dict["runningWorkers"] = running_workers
        if total_cycle_time is not UNSET:
            field_dict["totalCycleTime"] = total_cycle_time
        if used_workers is not UNSET:
            field_dict["usedWorkers"] = used_workers
        if deployed_workers is not UNSET:
            field_dict["deployedWorkers"] = deployed_workers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count_of_workers = d.pop("countOfWorkers", UNSET)

        running_workers = d.pop("runningWorkers", UNSET)

        total_cycle_time = d.pop("totalCycleTime", UNSET)

        used_workers = d.pop("usedWorkers", UNSET)

        deployed_workers = d.pop("deployedWorkers", UNSET)

        worker_statistics = cls(
            count_of_workers=count_of_workers,
            running_workers=running_workers,
            total_cycle_time=total_cycle_time,
            used_workers=used_workers,
            deployed_workers=deployed_workers,
        )

        return worker_statistics
