from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.check_result_severity import CheckResultSeverity
from ..models.worker_configuration_check_result_status import WorkerConfigurationCheckResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.worker_network_configuration import WorkerNetworkConfiguration


T = TypeVar("T", bound="WorkerConfigurationCheckResult")


@_attrs_define
class WorkerConfigurationCheckResult:
    """
    Attributes:
        configurations (WorkerNetworkConfiguration | Unset): Information on a worker network configuration.
        status (WorkerConfigurationCheckResultStatus | Unset): Status of the worker configuration.
        severity (CheckResultSeverity | Unset): Specifies the state of the configuration check operation.
    """

    configurations: WorkerNetworkConfiguration | Unset = UNSET
    status: WorkerConfigurationCheckResultStatus | Unset = UNSET
    severity: CheckResultSeverity | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        configurations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = self.configurations.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if configurations is not UNSET:
            field_dict["configurations"] = configurations
        if status is not UNSET:
            field_dict["status"] = status
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worker_network_configuration import WorkerNetworkConfiguration

        d = dict(src_dict)
        _configurations = d.pop("configurations", UNSET)
        configurations: WorkerNetworkConfiguration | Unset
        if isinstance(_configurations, Unset):
            configurations = UNSET
        else:
            configurations = WorkerNetworkConfiguration.from_dict(_configurations)

        _status = d.pop("status", UNSET)
        status: WorkerConfigurationCheckResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WorkerConfigurationCheckResultStatus(_status)

        _severity = d.pop("severity", UNSET)
        severity: CheckResultSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = CheckResultSeverity(_severity)

        worker_configuration_check_result = cls(
            configurations=configurations,
            status=status,
            severity=severity,
        )

        return worker_configuration_check_result
