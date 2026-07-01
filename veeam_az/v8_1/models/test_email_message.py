from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.smtp_settings_from_client import SmtpSettingsFromClient


T = TypeVar("T", bound="TestEmailMessage")


@_attrs_define
class TestEmailMessage:
    """
    Attributes:
        smtp_settings (SmtpSettingsFromClient): Specifies the settings of the SMTP server.
        from_ (str): Specifies the email address from which the test message will be sent.
        to (str): Specifies the email address of the test message recipient.
    """

    smtp_settings: SmtpSettingsFromClient
    from_: str
    to: str

    def to_dict(self) -> dict[str, Any]:
        smtp_settings = self.smtp_settings.to_dict()

        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "smtpSettings": smtp_settings,
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.smtp_settings_from_client import SmtpSettingsFromClient

        d = dict(src_dict)
        smtp_settings = SmtpSettingsFromClient.from_dict(d.pop("smtpSettings"))

        from_ = d.pop("from")

        to = d.pop("to")

        test_email_message = cls(
            smtp_settings=smtp_settings,
            from_=from_,
            to=to,
        )

        return test_email_message
