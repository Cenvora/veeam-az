from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_report_settings import DailyReportSettings
    from ..models.event_email_notification_settings import EventEmailNotificationSettings
    from ..models.smtp_settings import SmtpSettings


T = TypeVar("T", bound="EmailNotificationSettingsObject")


@_attrs_define
class EmailNotificationSettingsObject:
    """
    Attributes:
        smtp_settings (SmtpSettings | Unset): Specifies the settings of the SMTP server.
        notifications_enabled (bool | None | Unset): Defines whether the email notifications are enabled. The default
            value is *false*.
        from_ (None | str | Unset): Email address from which the email notifications are sent.
        to (None | str | Unset): Email addresses of the notification recipients.
        subject (None | str | Unset): Subject of the notification message. The default value is *[%JobResult%] %JobName%
            (%ObjectCount% instances) %Issues%*.
        sla_report_subject (None | str | Unset): Subject of the SLA report message. The default value is *%JobName%
            (%ObjectCount% instances)&#58; [%SLAType% for the period %SLAPeriod% is %SLAStatus%]*.
        daily_report_settings (DailyReportSettings | Unset): Specifies the settings of daily reports.
        email_notification_settings (EventEmailNotificationSettings | Unset): Defines whether email notifications will
            be sent depending on the backup policy completion result.
    """

    smtp_settings: SmtpSettings | Unset = UNSET
    notifications_enabled: bool | None | Unset = UNSET
    from_: None | str | Unset = UNSET
    to: None | str | Unset = UNSET
    subject: None | str | Unset = UNSET
    sla_report_subject: None | str | Unset = UNSET
    daily_report_settings: DailyReportSettings | Unset = UNSET
    email_notification_settings: EventEmailNotificationSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        smtp_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smtp_settings, Unset):
            smtp_settings = self.smtp_settings.to_dict()

        notifications_enabled: bool | None | Unset
        if isinstance(self.notifications_enabled, Unset):
            notifications_enabled = UNSET
        else:
            notifications_enabled = self.notifications_enabled

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        sla_report_subject: None | str | Unset
        if isinstance(self.sla_report_subject, Unset):
            sla_report_subject = UNSET
        else:
            sla_report_subject = self.sla_report_subject

        daily_report_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_report_settings, Unset):
            daily_report_settings = self.daily_report_settings.to_dict()

        email_notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email_notification_settings, Unset):
            email_notification_settings = self.email_notification_settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if smtp_settings is not UNSET:
            field_dict["smtpSettings"] = smtp_settings
        if notifications_enabled is not UNSET:
            field_dict["notificationsEnabled"] = notifications_enabled
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if sla_report_subject is not UNSET:
            field_dict["slaReportSubject"] = sla_report_subject
        if daily_report_settings is not UNSET:
            field_dict["dailyReportSettings"] = daily_report_settings
        if email_notification_settings is not UNSET:
            field_dict["emailNotificationSettings"] = email_notification_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_report_settings import DailyReportSettings
        from ..models.event_email_notification_settings import EventEmailNotificationSettings
        from ..models.smtp_settings import SmtpSettings

        d = dict(src_dict)
        _smtp_settings = d.pop("smtpSettings", UNSET)
        smtp_settings: SmtpSettings | Unset
        if isinstance(_smtp_settings, Unset):
            smtp_settings = UNSET
        else:
            smtp_settings = SmtpSettings.from_dict(_smtp_settings)

        def _parse_notifications_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notifications_enabled = _parse_notifications_enabled(d.pop("notificationsEnabled", UNSET))

        def _parse_from_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_sla_report_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sla_report_subject = _parse_sla_report_subject(d.pop("slaReportSubject", UNSET))

        _daily_report_settings = d.pop("dailyReportSettings", UNSET)
        daily_report_settings: DailyReportSettings | Unset
        if isinstance(_daily_report_settings, Unset):
            daily_report_settings = UNSET
        else:
            daily_report_settings = DailyReportSettings.from_dict(_daily_report_settings)

        _email_notification_settings = d.pop("emailNotificationSettings", UNSET)
        email_notification_settings: EventEmailNotificationSettings | Unset
        if isinstance(_email_notification_settings, Unset):
            email_notification_settings = UNSET
        else:
            email_notification_settings = EventEmailNotificationSettings.from_dict(_email_notification_settings)

        email_notification_settings_object = cls(
            smtp_settings=smtp_settings,
            notifications_enabled=notifications_enabled,
            from_=from_,
            to=to,
            subject=subject,
            sla_report_subject=sla_report_subject,
            daily_report_settings=daily_report_settings,
            email_notification_settings=email_notification_settings,
        )

        return email_notification_settings_object
