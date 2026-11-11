from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationBackupRequest")


@_attrs_define
class ConfigurationBackupRequest:
    """
    Attributes:
        repository_id (UUID | Unset): Specifies the system ID assigned in the Veeam backup for Microsoft Azure REST API
            to a backup repository where configuration backup files are stored.
        notification_email (None | str | Unset): Specifies an email where a notification on the configuration backup
            creation will be sent.
        should_send_completion_notification (bool | None | Unset): Defines whether a notification on the configuration
            backup creation will be sent.
    """

    repository_id: UUID | Unset = UNSET
    notification_email: None | str | Unset = UNSET
    should_send_completion_notification: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository_id: str | Unset = UNSET
        if not isinstance(self.repository_id, Unset):
            repository_id = str(self.repository_id)

        notification_email: None | str | Unset
        if isinstance(self.notification_email, Unset):
            notification_email = UNSET
        else:
            notification_email = self.notification_email

        should_send_completion_notification: bool | None | Unset
        if isinstance(self.should_send_completion_notification, Unset):
            should_send_completion_notification = UNSET
        else:
            should_send_completion_notification = self.should_send_completion_notification

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if notification_email is not UNSET:
            field_dict["notificationEmail"] = notification_email
        if should_send_completion_notification is not UNSET:
            field_dict["shouldSendCompletionNotification"] = should_send_completion_notification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _repository_id = d.pop("repositoryId", UNSET)
        repository_id: UUID | Unset
        if isinstance(_repository_id, Unset):
            repository_id = UNSET
        else:
            repository_id = UUID(_repository_id)

        def _parse_notification_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_email = _parse_notification_email(d.pop("notificationEmail", UNSET))

        def _parse_should_send_completion_notification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        should_send_completion_notification = _parse_should_send_completion_notification(
            d.pop("shouldSendCompletionNotification", UNSET)
        )

        configuration_backup_request = cls(
            repository_id=repository_id,
            notification_email=notification_email,
            should_send_completion_notification=should_send_completion_notification,
        )

        return configuration_backup_request
