from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.azure_account_purpose import AzureAccountPurpose
from ..models.azure_environment_nullable import AzureEnvironmentNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientLoginParameters")


@_attrs_define
class ClientLoginParameters:
    """Specifies the login data of the Entra ID application.

    Attributes:
        azure_environment (AzureEnvironmentNullable): Specifies the type of the Microsoft Azure cloud environment.
        application_id (UUID): Specifies the Microsoft Azure ID assigned to the Entra ID application.
        tenant_id (UUID): Specifies the Microsoft Azure ID assigned to a tenant in which the Entra ID application has
            been registered.
        client_secret (None | str | Unset): /[Required to authenticate using client secret] Specifies the client secret
            generated on the Azure portal.
        application_certificate (None | str | Unset): /[Required to authenticate using certificate] Specifies the
            certificate generated for the Entra ID application.
        application_certificate_name (None | str | Unset): /[Required to authenticate using certificate] Specifies the
            certificate file name or other way of naming certificate. Later on it will be used during account edit as
            reminder for certificate being used.
        certificate_password (None | str | Unset): Specifies the password used to encrypt the certificate on the
            certificate creation.
        azure_account_purposes (list[AzureAccountPurpose] | None | Unset): Specifies operations that can be performed
            using the service account.
        subscriptions (list[UUID] | None | Unset): Specifies Azure subscriptions with which the service account is
            associated.
    """

    azure_environment: AzureEnvironmentNullable
    application_id: UUID
    tenant_id: UUID
    client_secret: None | str | Unset = UNSET
    application_certificate: None | str | Unset = UNSET
    application_certificate_name: None | str | Unset = UNSET
    certificate_password: None | str | Unset = UNSET
    azure_account_purposes: list[AzureAccountPurpose] | None | Unset = UNSET
    subscriptions: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        azure_environment = self.azure_environment.value

        application_id = str(self.application_id)

        tenant_id = str(self.tenant_id)

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        application_certificate: None | str | Unset
        if isinstance(self.application_certificate, Unset):
            application_certificate = UNSET
        else:
            application_certificate = self.application_certificate

        application_certificate_name: None | str | Unset
        if isinstance(self.application_certificate_name, Unset):
            application_certificate_name = UNSET
        else:
            application_certificate_name = self.application_certificate_name

        certificate_password: None | str | Unset
        if isinstance(self.certificate_password, Unset):
            certificate_password = UNSET
        else:
            certificate_password = self.certificate_password

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

        subscriptions: list[str] | None | Unset
        if isinstance(self.subscriptions, Unset):
            subscriptions = UNSET
        elif isinstance(self.subscriptions, list):
            subscriptions = []
            for subscriptions_type_0_item_data in self.subscriptions:
                subscriptions_type_0_item = str(subscriptions_type_0_item_data)
                subscriptions.append(subscriptions_type_0_item)

        else:
            subscriptions = self.subscriptions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "azureEnvironment": azure_environment,
                "applicationId": application_id,
                "tenantId": tenant_id,
            }
        )
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if application_certificate_name is not UNSET:
            field_dict["applicationCertificateName"] = application_certificate_name
        if certificate_password is not UNSET:
            field_dict["certificatePassword"] = certificate_password
        if azure_account_purposes is not UNSET:
            field_dict["azureAccountPurposes"] = azure_account_purposes
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        azure_environment = AzureEnvironmentNullable(d.pop("azureEnvironment"))

        application_id = UUID(d.pop("applicationId"))

        tenant_id = UUID(d.pop("tenantId"))

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("clientSecret", UNSET))

        def _parse_application_certificate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_certificate = _parse_application_certificate(d.pop("applicationCertificate", UNSET))

        def _parse_application_certificate_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_certificate_name = _parse_application_certificate_name(d.pop("applicationCertificateName", UNSET))

        def _parse_certificate_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certificate_password = _parse_certificate_password(d.pop("certificatePassword", UNSET))

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

        def _parse_subscriptions(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subscriptions_type_0 = []
                _subscriptions_type_0 = data
                for subscriptions_type_0_item_data in _subscriptions_type_0:
                    subscriptions_type_0_item = UUID(subscriptions_type_0_item_data)

                    subscriptions_type_0.append(subscriptions_type_0_item)

                return subscriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        subscriptions = _parse_subscriptions(d.pop("subscriptions", UNSET))

        client_login_parameters = cls(
            azure_environment=azure_environment,
            application_id=application_id,
            tenant_id=tenant_id,
            client_secret=client_secret,
            application_certificate=application_certificate,
            application_certificate_name=application_certificate_name,
            certificate_password=certificate_password,
            azure_account_purposes=azure_account_purposes,
            subscriptions=subscriptions,
        )

        return client_login_parameters
