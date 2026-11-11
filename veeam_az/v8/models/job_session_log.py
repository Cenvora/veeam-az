from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_item import LogItem


T = TypeVar("T", bound="JobSessionLog")


@_attrs_define
class JobSessionLog:
    """
    Attributes:
        job_session_id (None | str | Unset): System ID assigned to the session in the Veeam Backup for Microsoft Azure
            REST API.
        log (list[LogItem] | None | Unset): Session log.
    """

    job_session_id: None | str | Unset = UNSET
    log: list[LogItem] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        job_session_id: None | str | Unset
        if isinstance(self.job_session_id, Unset):
            job_session_id = UNSET
        else:
            job_session_id = self.job_session_id

        log: list[dict[str, Any]] | None | Unset
        if isinstance(self.log, Unset):
            log = UNSET
        elif isinstance(self.log, list):
            log = []
            for log_type_0_item_data in self.log:
                log_type_0_item = log_type_0_item_data.to_dict()
                log.append(log_type_0_item)

        else:
            log = self.log

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if job_session_id is not UNSET:
            field_dict["jobSessionId"] = job_session_id
        if log is not UNSET:
            field_dict["log"] = log

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_item import LogItem

        d = dict(src_dict)

        def _parse_job_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_session_id = _parse_job_session_id(d.pop("jobSessionId", UNSET))

        def _parse_log(data: object) -> list[LogItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                log_type_0 = []
                _log_type_0 = data
                for log_type_0_item_data in _log_type_0:
                    log_type_0_item = LogItem.from_dict(log_type_0_item_data)

                    log_type_0.append(log_type_0_item)

                return log_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LogItem] | None | Unset, data)

        log = _parse_log(d.pop("log", UNSET))

        job_session_log = cls(
            job_session_id=job_session_id,
            log=log,
        )

        return job_session_log
