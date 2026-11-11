from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrySettings")


@_attrs_define
class RetrySettings:
    """Specifies the retry settings for the backup policy.

    Attributes:
        retry_count (int | None | Unset): Specifies the maximum number of retry attempts for the backup policy.
    """

    retry_count: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        retry_count: int | None | Unset
        if isinstance(self.retry_count, Unset):
            retry_count = UNSET
        else:
            retry_count = self.retry_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if retry_count is not UNSET:
            field_dict["retryCount"] = retry_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_retry_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_count = _parse_retry_count(d.pop("retryCount", UNSET))

        retry_settings = cls(
            retry_count=retry_count,
        )

        return retry_settings
