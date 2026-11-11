from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.smtp_account_type import SmtpAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SmtpSettingsFromClient")


@_attrs_define
class SmtpSettingsFromClient:
    """Specifies the settings of the SMTP server.

    Attributes:
        account_id (None | str | Unset): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure REST
            API to the account used to send email notifications.
        account_type (SmtpAccountType | Unset): Defines whether you want to employ basic (SMTP) or modern (OAuth 2.0)
            authentication for your mail server. </br> **Note**&#58; To be able to use OAuth 2.0 to access Google Cloud or
            Microsoft Azure APIs, you must first create a new client application in the Google Cloud Console or Microsoft
            Azure portal.
        host (None | str | Unset): Specifies the DNS name or an IP address of the SMTP server.
        port (int | None | Unset): Specifies the port used by the SMTP server. The default value is *25*.
        use_secure_connection (bool | None | Unset): Defines whether to use the secure connection for email operations.
            The default value is *false*.
        time_out_mili_seconds (int | None | Unset): Specifies the connection timeout for the SMTP server (in
            milliseconds). The default value is *100000*.
    """

    account_id: None | str | Unset = UNSET
    account_type: SmtpAccountType | Unset = UNSET
    host: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    use_secure_connection: bool | None | Unset = UNSET
    time_out_mili_seconds: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        use_secure_connection: bool | None | Unset
        if isinstance(self.use_secure_connection, Unset):
            use_secure_connection = UNSET
        else:
            use_secure_connection = self.use_secure_connection

        time_out_mili_seconds: int | None | Unset
        if isinstance(self.time_out_mili_seconds, Unset):
            time_out_mili_seconds = UNSET
        else:
            time_out_mili_seconds = self.time_out_mili_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if use_secure_connection is not UNSET:
            field_dict["useSecureConnection"] = use_secure_connection
        if time_out_mili_seconds is not UNSET:
            field_dict["timeOutMiliSeconds"] = time_out_mili_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))

        _account_type = d.pop("accountType", UNSET)
        account_type: SmtpAccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = SmtpAccountType(_account_type)

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_use_secure_connection(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_secure_connection = _parse_use_secure_connection(d.pop("useSecureConnection", UNSET))

        def _parse_time_out_mili_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_out_mili_seconds = _parse_time_out_mili_seconds(d.pop("timeOutMiliSeconds", UNSET))

        smtp_settings_from_client = cls(
            account_id=account_id,
            account_type=account_type,
            host=host,
            port=port,
            use_secure_connection=use_secure_connection,
            time_out_mili_seconds=time_out_mili_seconds,
        )

        return smtp_settings_from_client
