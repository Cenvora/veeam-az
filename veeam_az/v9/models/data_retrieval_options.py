from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.data_retrieval_priority import DataRetrievalPriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataRetrievalOptions")


@_attrs_define
class DataRetrievalOptions:
    """
    Attributes:
        data_retrieval_priority (DataRetrievalPriority): Specifies the priority type for the data retrieval operation.
        days_to_keep (int | Unset): Specifies the number of days for which the retrieved data will be kept.
        notify_before_expiration_hours (int | None | Unset): Specifies the time when a notification will be sent (in
            hours remaining until the expiration).
        notify_after_complete (bool | None | Unset): Defines whether a notification must be sent after the operation is
            complete.
    """

    data_retrieval_priority: DataRetrievalPriority
    days_to_keep: int | Unset = UNSET
    notify_before_expiration_hours: int | None | Unset = UNSET
    notify_after_complete: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data_retrieval_priority = self.data_retrieval_priority.value

        days_to_keep = self.days_to_keep

        notify_before_expiration_hours: int | None | Unset
        if isinstance(self.notify_before_expiration_hours, Unset):
            notify_before_expiration_hours = UNSET
        else:
            notify_before_expiration_hours = self.notify_before_expiration_hours

        notify_after_complete: bool | None | Unset
        if isinstance(self.notify_after_complete, Unset):
            notify_after_complete = UNSET
        else:
            notify_after_complete = self.notify_after_complete

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dataRetrievalPriority": data_retrieval_priority,
            }
        )
        if days_to_keep is not UNSET:
            field_dict["daysToKeep"] = days_to_keep
        if notify_before_expiration_hours is not UNSET:
            field_dict["notifyBeforeExpirationHours"] = notify_before_expiration_hours
        if notify_after_complete is not UNSET:
            field_dict["notifyAfterComplete"] = notify_after_complete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_retrieval_priority = DataRetrievalPriority(d.pop("dataRetrievalPriority"))

        days_to_keep = d.pop("daysToKeep", UNSET)

        def _parse_notify_before_expiration_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        notify_before_expiration_hours = _parse_notify_before_expiration_hours(
            d.pop("notifyBeforeExpirationHours", UNSET)
        )

        def _parse_notify_after_complete(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_after_complete = _parse_notify_after_complete(d.pop("notifyAfterComplete", UNSET))

        data_retrieval_options = cls(
            data_retrieval_priority=data_retrieval_priority,
            days_to_keep=days_to_keep,
            notify_before_expiration_hours=notify_before_expiration_hours,
            notify_after_complete=notify_after_complete,
        )

        return data_retrieval_options
