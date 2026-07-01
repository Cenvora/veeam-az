from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.worker_configuration_check_result import WorkerConfigurationCheckResult


T = TypeVar("T", bound="CheckResponseWorkerConfigurations")


@_attrs_define
class CheckResponseWorkerConfigurations:
    """Results of the worker configurations check.

    Attributes:
        worker_configurations (list[WorkerConfigurationCheckResult] | Unset): Information on each worker configuration.
    """

    worker_configurations: list[WorkerConfigurationCheckResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        worker_configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.worker_configurations, Unset):
            worker_configurations = []
            for worker_configurations_item_data in self.worker_configurations:
                worker_configurations_item = worker_configurations_item_data.to_dict()
                worker_configurations.append(worker_configurations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if worker_configurations is not UNSET:
            field_dict["workerConfigurations"] = worker_configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worker_configuration_check_result import WorkerConfigurationCheckResult

        d = dict(src_dict)
        _worker_configurations = d.pop("workerConfigurations", UNSET)
        worker_configurations: list[WorkerConfigurationCheckResult] | Unset = UNSET
        if _worker_configurations is not UNSET:
            worker_configurations = []
            for worker_configurations_item_data in _worker_configurations:
                worker_configurations_item = WorkerConfigurationCheckResult.from_dict(worker_configurations_item_data)

                worker_configurations.append(worker_configurations_item)

        check_response_worker_configurations = cls(
            worker_configurations=worker_configurations,
        )

        check_response_worker_configurations.additional_properties = d
        return check_response_worker_configurations

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
