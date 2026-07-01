from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.azure_account_cloud_state_nullable import AzureAccountCloudStateNullable
from ..models.azure_account_origin import AzureAccountOrigin
from ..models.azure_account_permissions_state import AzureAccountPermissionsState
from ..models.azure_account_purpose import AzureAccountPurpose
from ..models.azure_account_state import AzureAccountState
from ..models.azure_environment import AzureEnvironment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="AzureAccount")


@_attrs_define
class AzureAccount:
    """Information on a service account.

    Attributes:
        account_id (None | str | Unset): System ID assigned to the account in the Veeam Backup for Microsoft Azure REST
            API.
        application_id (UUID | Unset): Microsoft Azure ID assigned to the Entra ID application.
        application_certificate_name (None | str | Unset): Name of file name (or other possible name) uploaded as
            certificate for later reminder which certificate was uploaded.
        name (None | str | Unset): Name of the account in Veeam Backup for Microsoft Azure.
        description (None | str | Unset): Description of the account.
        region (AzureEnvironment | Unset): Specifies the type of the Microsoft Azure cloud environment.
        tenant_id (None | str | Unset): Microsoft Azure ID assigned to a tenant with which the service account is
            associated.
        tenant_name (None | str | Unset): Name of the tenant.
        account_origin (AzureAccountOrigin | Unset): Authentication type of the service account.
        expiration_date (datetime.datetime | None | Unset): Date of the account expiration.
        account_state (AzureAccountState | Unset): State of the service account creation.
        ad_group_id (None | Unset | UUID): Microsoft Azure ID assigned to a Microsoft Entra group to which the account
            belongs.
        cloud_state (AzureAccountCloudStateNullable | Unset): Status of the account in the Microsoft Azure environment.
        ad_group_name (None | str | Unset): Name of the Microsoft Entra group.
        purposes (list[AzureAccountPurpose] | None | Unset): List of operations that can be performed using the service
            account.
        management_group_id (None | str | Unset): Microsoft Azure ID assigned to a management group to which
            subscriptions protected using the service account belong.
        management_group_name (None | str | Unset): Name of the management group to which subscriptions protected using
            the service account belong.
        subscription_ids (list[str] | Unset): List of Azure subscriptions with which the service account is associated.
        selected_for_workermanagement (bool | Unset): Defines whether the account has the `Worker management` role
            selected.
        azure_permissions_state (list[AzureAccountPermissionsState] | None | Unset): Status of the service account
            permissions check. The `MissingSubscriptions` value indicates that the account has lost access to one or more
            subscriptions returned in the `subscriptionIds` property.
        azure_permissions_state_check_time_utc (datetime.datetime | None | Unset): Date and time of the last permission
            check performed for the service account.
        subscription_id_for_worker_deployment (None | Unset | UUID): Microsoft Azure ID assigned to the subscription in
            which the worker instances are deployed.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    account_id: None | str | Unset = UNSET
    application_id: UUID | Unset = UNSET
    application_certificate_name: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    region: AzureEnvironment | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    tenant_name: None | str | Unset = UNSET
    account_origin: AzureAccountOrigin | Unset = UNSET
    expiration_date: datetime.datetime | None | Unset = UNSET
    account_state: AzureAccountState | Unset = UNSET
    ad_group_id: None | Unset | UUID = UNSET
    cloud_state: AzureAccountCloudStateNullable | Unset = UNSET
    ad_group_name: None | str | Unset = UNSET
    purposes: list[AzureAccountPurpose] | None | Unset = UNSET
    management_group_id: None | str | Unset = UNSET
    management_group_name: None | str | Unset = UNSET
    subscription_ids: list[str] | Unset = UNSET
    selected_for_workermanagement: bool | Unset = UNSET
    azure_permissions_state: list[AzureAccountPermissionsState] | None | Unset = UNSET
    azure_permissions_state_check_time_utc: datetime.datetime | None | Unset = UNSET
    subscription_id_for_worker_deployment: None | Unset | UUID = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        application_id: str | Unset = UNSET
        if not isinstance(self.application_id, Unset):
            application_id = str(self.application_id)

        application_certificate_name: None | str | Unset
        if isinstance(self.application_certificate_name, Unset):
            application_certificate_name = UNSET
        else:
            application_certificate_name = self.application_certificate_name

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        tenant_name: None | str | Unset
        if isinstance(self.tenant_name, Unset):
            tenant_name = UNSET
        else:
            tenant_name = self.tenant_name

        account_origin: str | Unset = UNSET
        if not isinstance(self.account_origin, Unset):
            account_origin = self.account_origin.value

        expiration_date: None | str | Unset
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.datetime):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        account_state: str | Unset = UNSET
        if not isinstance(self.account_state, Unset):
            account_state = self.account_state.value

        ad_group_id: None | str | Unset
        if isinstance(self.ad_group_id, Unset):
            ad_group_id = UNSET
        elif isinstance(self.ad_group_id, UUID):
            ad_group_id = str(self.ad_group_id)
        else:
            ad_group_id = self.ad_group_id

        cloud_state: str | Unset = UNSET
        if not isinstance(self.cloud_state, Unset):
            cloud_state = self.cloud_state.value

        ad_group_name: None | str | Unset
        if isinstance(self.ad_group_name, Unset):
            ad_group_name = UNSET
        else:
            ad_group_name = self.ad_group_name

        purposes: list[str] | None | Unset
        if isinstance(self.purposes, Unset):
            purposes = UNSET
        elif isinstance(self.purposes, list):
            purposes = []
            for purposes_type_0_item_data in self.purposes:
                purposes_type_0_item = purposes_type_0_item_data.value
                purposes.append(purposes_type_0_item)

        else:
            purposes = self.purposes

        management_group_id: None | str | Unset
        if isinstance(self.management_group_id, Unset):
            management_group_id = UNSET
        else:
            management_group_id = self.management_group_id

        management_group_name: None | str | Unset
        if isinstance(self.management_group_name, Unset):
            management_group_name = UNSET
        else:
            management_group_name = self.management_group_name

        subscription_ids: list[str] | Unset = UNSET
        if not isinstance(self.subscription_ids, Unset):
            subscription_ids = self.subscription_ids

        selected_for_workermanagement = self.selected_for_workermanagement

        azure_permissions_state: list[str] | None | Unset
        if isinstance(self.azure_permissions_state, Unset):
            azure_permissions_state = UNSET
        elif isinstance(self.azure_permissions_state, list):
            azure_permissions_state = []
            for azure_permissions_state_type_0_item_data in self.azure_permissions_state:
                azure_permissions_state_type_0_item = azure_permissions_state_type_0_item_data.value
                azure_permissions_state.append(azure_permissions_state_type_0_item)

        else:
            azure_permissions_state = self.azure_permissions_state

        azure_permissions_state_check_time_utc: None | str | Unset
        if isinstance(self.azure_permissions_state_check_time_utc, Unset):
            azure_permissions_state_check_time_utc = UNSET
        elif isinstance(self.azure_permissions_state_check_time_utc, datetime.datetime):
            azure_permissions_state_check_time_utc = self.azure_permissions_state_check_time_utc.isoformat()
        else:
            azure_permissions_state_check_time_utc = self.azure_permissions_state_check_time_utc

        subscription_id_for_worker_deployment: None | str | Unset
        if isinstance(self.subscription_id_for_worker_deployment, Unset):
            subscription_id_for_worker_deployment = UNSET
        elif isinstance(self.subscription_id_for_worker_deployment, UUID):
            subscription_id_for_worker_deployment = str(self.subscription_id_for_worker_deployment)
        else:
            subscription_id_for_worker_deployment = self.subscription_id_for_worker_deployment

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate_name is not UNSET:
            field_dict["applicationCertificateName"] = application_certificate_name
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if region is not UNSET:
            field_dict["region"] = region
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if tenant_name is not UNSET:
            field_dict["tenantName"] = tenant_name
        if account_origin is not UNSET:
            field_dict["accountOrigin"] = account_origin
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if account_state is not UNSET:
            field_dict["accountState"] = account_state
        if ad_group_id is not UNSET:
            field_dict["adGroupId"] = ad_group_id
        if cloud_state is not UNSET:
            field_dict["cloudState"] = cloud_state
        if ad_group_name is not UNSET:
            field_dict["adGroupName"] = ad_group_name
        if purposes is not UNSET:
            field_dict["purposes"] = purposes
        if management_group_id is not UNSET:
            field_dict["managementGroupId"] = management_group_id
        if management_group_name is not UNSET:
            field_dict["managementGroupName"] = management_group_name
        if subscription_ids is not UNSET:
            field_dict["subscriptionIds"] = subscription_ids
        if selected_for_workermanagement is not UNSET:
            field_dict["selectedForWorkermanagement"] = selected_for_workermanagement
        if azure_permissions_state is not UNSET:
            field_dict["azurePermissionsState"] = azure_permissions_state
        if azure_permissions_state_check_time_utc is not UNSET:
            field_dict["azurePermissionsStateCheckTimeUtc"] = azure_permissions_state_check_time_utc
        if subscription_id_for_worker_deployment is not UNSET:
            field_dict["subscriptionIdForWorkerDeployment"] = subscription_id_for_worker_deployment
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))

        _application_id = d.pop("applicationId", UNSET)
        application_id: UUID | Unset
        if isinstance(_application_id, Unset):
            application_id = UNSET
        else:
            application_id = UUID(_application_id)

        def _parse_application_certificate_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_certificate_name = _parse_application_certificate_name(d.pop("applicationCertificateName", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _region = d.pop("region", UNSET)
        region: AzureEnvironment | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = AzureEnvironment(_region)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_tenant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_name = _parse_tenant_name(d.pop("tenantName", UNSET))

        _account_origin = d.pop("accountOrigin", UNSET)
        account_origin: AzureAccountOrigin | Unset
        if isinstance(_account_origin, Unset):
            account_origin = UNSET
        else:
            account_origin = AzureAccountOrigin(_account_origin)

        def _parse_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_type_0 = isoparse(data)

                return expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date = _parse_expiration_date(d.pop("expirationDate", UNSET))

        _account_state = d.pop("accountState", UNSET)
        account_state: AzureAccountState | Unset
        if isinstance(_account_state, Unset):
            account_state = UNSET
        else:
            account_state = AzureAccountState(_account_state)

        def _parse_ad_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ad_group_id_type_0 = UUID(data)

                return ad_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        ad_group_id = _parse_ad_group_id(d.pop("adGroupId", UNSET))

        _cloud_state = d.pop("cloudState", UNSET)
        cloud_state: AzureAccountCloudStateNullable | Unset
        if isinstance(_cloud_state, Unset):
            cloud_state = UNSET
        else:
            cloud_state = AzureAccountCloudStateNullable(_cloud_state)

        def _parse_ad_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ad_group_name = _parse_ad_group_name(d.pop("adGroupName", UNSET))

        def _parse_purposes(data: object) -> list[AzureAccountPurpose] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                purposes_type_0 = []
                _purposes_type_0 = data
                for purposes_type_0_item_data in _purposes_type_0:
                    purposes_type_0_item = AzureAccountPurpose(purposes_type_0_item_data)

                    purposes_type_0.append(purposes_type_0_item)

                return purposes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzureAccountPurpose] | None | Unset, data)

        purposes = _parse_purposes(d.pop("purposes", UNSET))

        def _parse_management_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        management_group_id = _parse_management_group_id(d.pop("managementGroupId", UNSET))

        def _parse_management_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        management_group_name = _parse_management_group_name(d.pop("managementGroupName", UNSET))

        subscription_ids = cast(list[str], d.pop("subscriptionIds", UNSET))

        selected_for_workermanagement = d.pop("selectedForWorkermanagement", UNSET)

        def _parse_azure_permissions_state(data: object) -> list[AzureAccountPermissionsState] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_permissions_state_type_0 = []
                _azure_permissions_state_type_0 = data
                for azure_permissions_state_type_0_item_data in _azure_permissions_state_type_0:
                    azure_permissions_state_type_0_item = AzureAccountPermissionsState(
                        azure_permissions_state_type_0_item_data
                    )

                    azure_permissions_state_type_0.append(azure_permissions_state_type_0_item)

                return azure_permissions_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzureAccountPermissionsState] | None | Unset, data)

        azure_permissions_state = _parse_azure_permissions_state(d.pop("azurePermissionsState", UNSET))

        def _parse_azure_permissions_state_check_time_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                azure_permissions_state_check_time_utc_type_0 = isoparse(data)

                return azure_permissions_state_check_time_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        azure_permissions_state_check_time_utc = _parse_azure_permissions_state_check_time_utc(
            d.pop("azurePermissionsStateCheckTimeUtc", UNSET)
        )

        def _parse_subscription_id_for_worker_deployment(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_for_worker_deployment_type_0 = UUID(data)

                return subscription_id_for_worker_deployment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id_for_worker_deployment = _parse_subscription_id_for_worker_deployment(
            d.pop("subscriptionIdForWorkerDeployment", UNSET)
        )

        def _parse_field_links(data: object) -> LinksDictionaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_links_dictionary_type_0 = LinksDictionaryType0.from_dict(data)

                return componentsschemas_links_dictionary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinksDictionaryType0 | None | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        azure_account = cls(
            account_id=account_id,
            application_id=application_id,
            application_certificate_name=application_certificate_name,
            name=name,
            description=description,
            region=region,
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            account_origin=account_origin,
            expiration_date=expiration_date,
            account_state=account_state,
            ad_group_id=ad_group_id,
            cloud_state=cloud_state,
            ad_group_name=ad_group_name,
            purposes=purposes,
            management_group_id=management_group_id,
            management_group_name=management_group_name,
            subscription_ids=subscription_ids,
            selected_for_workermanagement=selected_for_workermanagement,
            azure_permissions_state=azure_permissions_state,
            azure_permissions_state_check_time_utc=azure_permissions_state_check_time_utc,
            subscription_id_for_worker_deployment=subscription_id_for_worker_deployment,
            field_links=field_links,
        )

        return azure_account
