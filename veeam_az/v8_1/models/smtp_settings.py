from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_account import OAuth2Account
    from ..models.smtp_server_state_model import SmtpServerStateModel
    from ..models.standard_account import StandardAccount


T = TypeVar("T", bound="SmtpSettings")


@_attrs_define
class SmtpSettings:
    """Specifies the settings of the SMTP server.

    Attributes:
        oauth_2_account (OAuth2Account | Unset):
        basic_account (StandardAccount | Unset):
        host (None | str | Unset): DNS name or an IP address of the SMTP server.
        port (int | None | Unset): Port used by the SMTP server.
        use_secure_connection (bool | None | Unset): Defines whether the secure connection is used for email operations.
        time_out_mili_seconds (int | None | Unset): Connection timeout for the SMTP server (in milliseconds).
        server_state (SmtpServerStateModel | Unset):
    """

    oauth_2_account: OAuth2Account | Unset = UNSET
    basic_account: StandardAccount | Unset = UNSET
    host: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    use_secure_connection: bool | None | Unset = UNSET
    time_out_mili_seconds: int | None | Unset = UNSET
    server_state: SmtpServerStateModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        oauth_2_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oauth_2_account, Unset):
            oauth_2_account = self.oauth_2_account.to_dict()

        basic_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_account, Unset):
            basic_account = self.basic_account.to_dict()

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

        server_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server_state, Unset):
            server_state = self.server_state.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if oauth_2_account is not UNSET:
            field_dict["oauth2Account"] = oauth_2_account
        if basic_account is not UNSET:
            field_dict["basicAccount"] = basic_account
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if use_secure_connection is not UNSET:
            field_dict["useSecureConnection"] = use_secure_connection
        if time_out_mili_seconds is not UNSET:
            field_dict["timeOutMiliSeconds"] = time_out_mili_seconds
        if server_state is not UNSET:
            field_dict["serverState"] = server_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_account import OAuth2Account
        from ..models.smtp_server_state_model import SmtpServerStateModel
        from ..models.standard_account import StandardAccount

        d = dict(src_dict)
        _oauth_2_account = d.pop("oauth2Account", UNSET)
        oauth_2_account: OAuth2Account | Unset
        if isinstance(_oauth_2_account, Unset):
            oauth_2_account = UNSET
        else:
            oauth_2_account = OAuth2Account.from_dict(_oauth_2_account)

        _basic_account = d.pop("basicAccount", UNSET)
        basic_account: StandardAccount | Unset
        if isinstance(_basic_account, Unset):
            basic_account = UNSET
        else:
            basic_account = StandardAccount.from_dict(_basic_account)

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

        _server_state = d.pop("serverState", UNSET)
        server_state: SmtpServerStateModel | Unset
        if isinstance(_server_state, Unset):
            server_state = UNSET
        else:
            server_state = SmtpServerStateModel.from_dict(_server_state)

        smtp_settings = cls(
            oauth_2_account=oauth_2_account,
            basic_account=basic_account,
            host=host,
            port=port,
            use_secure_connection=use_secure_connection,
            time_out_mili_seconds=time_out_mili_seconds,
            server_state=server_state,
        )

        return smtp_settings
