from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimezoneFromClient")


@_attrs_define
class TimezoneFromClient:
    """
    Attributes:
        timezone_id (str | Unset): Specifies the system ID assigned to the time zone in the Veeam Backup for Microsoft
            Azure REST API.
    """

    timezone_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        timezone_id = self.timezone_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if timezone_id is not UNSET:
            field_dict["timezoneId"] = timezone_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timezone_id = d.pop("timezoneId", UNSET)

        timezone_from_client = cls(
            timezone_id=timezone_id,
        )

        return timezone_from_client
