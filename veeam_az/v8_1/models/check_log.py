from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.configuration_check_status import ConfigurationCheckStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_response import CheckResponse
    from ..models.log_line_status import LogLineStatus


T = TypeVar("T", bound="CheckLog")


@_attrs_define
class CheckLog:
    """
    Attributes:
        log_line (list[LogLineStatus] | Unset): General information about the configuration check results.
        overall_status (ConfigurationCheckStatus | Unset): Status of the configuration check.
        check_response (CheckResponse | Unset): Detailed information on the configuration check.
    """

    log_line: list[LogLineStatus] | Unset = UNSET
    overall_status: ConfigurationCheckStatus | Unset = UNSET
    check_response: CheckResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        log_line: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.log_line, Unset):
            log_line = []
            for log_line_item_data in self.log_line:
                log_line_item = log_line_item_data.to_dict()
                log_line.append(log_line_item)

        overall_status: str | Unset = UNSET
        if not isinstance(self.overall_status, Unset):
            overall_status = self.overall_status.value

        check_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_response, Unset):
            check_response = self.check_response.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if log_line is not UNSET:
            field_dict["logLine"] = log_line
        if overall_status is not UNSET:
            field_dict["overallStatus"] = overall_status
        if check_response is not UNSET:
            field_dict["checkResponse"] = check_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_response import CheckResponse
        from ..models.log_line_status import LogLineStatus

        d = dict(src_dict)
        _log_line = d.pop("logLine", UNSET)
        log_line: list[LogLineStatus] | Unset = UNSET
        if _log_line is not UNSET:
            log_line = []
            for log_line_item_data in _log_line:
                log_line_item = LogLineStatus.from_dict(log_line_item_data)

                log_line.append(log_line_item)

        _overall_status = d.pop("overallStatus", UNSET)
        overall_status: ConfigurationCheckStatus | Unset
        if isinstance(_overall_status, Unset):
            overall_status = UNSET
        else:
            overall_status = ConfigurationCheckStatus(_overall_status)

        _check_response = d.pop("checkResponse", UNSET)
        check_response: CheckResponse | Unset
        if isinstance(_check_response, Unset):
            check_response = UNSET
        else:
            check_response = CheckResponse.from_dict(_check_response)

        check_log = cls(
            log_line=log_line,
            overall_status=overall_status,
            check_response=check_response,
        )

        return check_log
