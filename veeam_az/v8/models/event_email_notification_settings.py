from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventEmailNotificationSettings")


@_attrs_define
class EventEmailNotificationSettings:
    """Defines whether email notifications will be sent depending on the backup policy completion result.

    Attributes:
        notify_on_success (bool | None | Unset): Defines whether an email notification will be sent when a backup policy
            completes successfully. The default value is *true*.
        notify_on_warning (bool | None | Unset): Defines whether an email notification will be sent when a backup policy
            completes with a warning. The default value is *true*.
        notify_on_failure (bool | None | Unset): Defines whether an email notification will be sent when a backup policy
            fails. The default value is *true*.
    """

    notify_on_success: bool | None | Unset = UNSET
    notify_on_warning: bool | None | Unset = UNSET
    notify_on_failure: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        notify_on_success: bool | None | Unset
        if isinstance(self.notify_on_success, Unset):
            notify_on_success = UNSET
        else:
            notify_on_success = self.notify_on_success

        notify_on_warning: bool | None | Unset
        if isinstance(self.notify_on_warning, Unset):
            notify_on_warning = UNSET
        else:
            notify_on_warning = self.notify_on_warning

        notify_on_failure: bool | None | Unset
        if isinstance(self.notify_on_failure, Unset):
            notify_on_failure = UNSET
        else:
            notify_on_failure = self.notify_on_failure

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if notify_on_success is not UNSET:
            field_dict["notifyOnSuccess"] = notify_on_success
        if notify_on_warning is not UNSET:
            field_dict["notifyOnWarning"] = notify_on_warning
        if notify_on_failure is not UNSET:
            field_dict["notifyOnFailure"] = notify_on_failure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_notify_on_success(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_on_success = _parse_notify_on_success(d.pop("notifyOnSuccess", UNSET))

        def _parse_notify_on_warning(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_on_warning = _parse_notify_on_warning(d.pop("notifyOnWarning", UNSET))

        def _parse_notify_on_failure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_on_failure = _parse_notify_on_failure(d.pop("notifyOnFailure", UNSET))

        event_email_notification_settings = cls(
            notify_on_success=notify_on_success,
            notify_on_warning=notify_on_warning,
            notify_on_failure=notify_on_failure,
        )

        return event_email_notification_settings
