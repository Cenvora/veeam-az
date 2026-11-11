from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.azure_account_purpose import AzureAccountPurpose
from ..models.azure_environment_nullable import AzureEnvironmentNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceLoginParameters")


@_attrs_define
class DeviceLoginParameters:
    """
    Attributes:
        azure_environment (AzureEnvironmentNullable | Unset): Specifies the type of the Microsoft Azure cloud
            environment.
        user_code (None | str | Unset): Specifies a single-use verification code used to authenticate Veeam Backup for
            Microsoft Azure to the Azure CLI.
        device_code (None | str | Unset): Specifies a verification code used to start the authentication session between
            the client and the authorization server.
        verification_url (None | str | Unset): Specifies the redirect URI used to sign in with `userCode`.
        expires_on (datetime.datetime | Unset): Specifies the date and time when `deviceCode` and `userCode` will
            expire.
        interval (int | Unset): Specifies a time interval the user must wait between polling requests (in seconds).
        message (None | str | Unset): Specifies a message describing the steps of the user authentication process.
        client_id (None | str | Unset): Specifies the Application (client) ID.
        scopes (list[str] | None | Unset): Specifies the user permissions.
        azure_account_purposes (list[AzureAccountPurpose] | None | Unset):
    """

    azure_environment: AzureEnvironmentNullable | Unset = UNSET
    user_code: None | str | Unset = UNSET
    device_code: None | str | Unset = UNSET
    verification_url: None | str | Unset = UNSET
    expires_on: datetime.datetime | Unset = UNSET
    interval: int | Unset = UNSET
    message: None | str | Unset = UNSET
    client_id: None | str | Unset = UNSET
    scopes: list[str] | None | Unset = UNSET
    azure_account_purposes: list[AzureAccountPurpose] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        user_code: None | str | Unset
        if isinstance(self.user_code, Unset):
            user_code = UNSET
        else:
            user_code = self.user_code

        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        verification_url: None | str | Unset
        if isinstance(self.verification_url, Unset):
            verification_url = UNSET
        else:
            verification_url = self.verification_url

        expires_on: str | Unset = UNSET
        if not isinstance(self.expires_on, Unset):
            expires_on = self.expires_on.isoformat()

        interval = self.interval

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        client_id: None | str | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        scopes: list[str] | None | Unset
        if isinstance(self.scopes, Unset):
            scopes = UNSET
        elif isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        azure_account_purposes: list[str] | None | Unset
        if isinstance(self.azure_account_purposes, Unset):
            azure_account_purposes = UNSET
        elif isinstance(self.azure_account_purposes, list):
            azure_account_purposes = []
            for azure_account_purposes_type_0_item_data in self.azure_account_purposes:
                azure_account_purposes_type_0_item = azure_account_purposes_type_0_item_data.value
                azure_account_purposes.append(azure_account_purposes_type_0_item)

        else:
            azure_account_purposes = self.azure_account_purposes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if device_code is not UNSET:
            field_dict["deviceCode"] = device_code
        if verification_url is not UNSET:
            field_dict["verificationUrl"] = verification_url
        if expires_on is not UNSET:
            field_dict["expiresOn"] = expires_on
        if interval is not UNSET:
            field_dict["interval"] = interval
        if message is not UNSET:
            field_dict["message"] = message
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if azure_account_purposes is not UNSET:
            field_dict["azureAccountPurposes"] = azure_account_purposes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureEnvironmentNullable | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureEnvironmentNullable(_azure_environment)

        def _parse_user_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_code = _parse_user_code(d.pop("userCode", UNSET))

        def _parse_device_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_code = _parse_device_code(d.pop("deviceCode", UNSET))

        def _parse_verification_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verification_url = _parse_verification_url(d.pop("verificationUrl", UNSET))

        _expires_on = d.pop("expiresOn", UNSET)
        expires_on: datetime.datetime | Unset
        if isinstance(_expires_on, Unset):
            expires_on = UNSET
        else:
            expires_on = isoparse(_expires_on)

        interval = d.pop("interval", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_id = _parse_client_id(d.pop("clientId", UNSET))

        def _parse_scopes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scopes = _parse_scopes(d.pop("scopes", UNSET))

        def _parse_azure_account_purposes(data: object) -> list[AzureAccountPurpose] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_account_purposes_type_0 = []
                _azure_account_purposes_type_0 = data
                for azure_account_purposes_type_0_item_data in _azure_account_purposes_type_0:
                    azure_account_purposes_type_0_item = AzureAccountPurpose(azure_account_purposes_type_0_item_data)

                    azure_account_purposes_type_0.append(azure_account_purposes_type_0_item)

                return azure_account_purposes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzureAccountPurpose] | None | Unset, data)

        azure_account_purposes = _parse_azure_account_purposes(d.pop("azureAccountPurposes", UNSET))

        device_login_parameters = cls(
            azure_environment=azure_environment,
            user_code=user_code,
            device_code=device_code,
            verification_url=verification_url,
            expires_on=expires_on,
            interval=interval,
            message=message,
            client_id=client_id,
            scopes=scopes,
            azure_account_purposes=azure_account_purposes,
        )

        return device_login_parameters
