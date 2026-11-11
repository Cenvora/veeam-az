from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.license_type import LicenseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.licensing_server_info import LicensingServerInfo


T = TypeVar("T", bound="LicenseInfo")


@_attrs_define
class LicenseInfo:
    r"""
    Attributes:
        license_type (LicenseType | Unset): Type of the license.
        is_free_edition (bool | Unset): Defines whether the license edition is free.
        total_instances_uses (float | Unset): Total number of instances consuming license units.
        vms_instances_uses (float | Unset): Number of Azure VM instances consuming license units.
        sql_instances_uses (float | Unset): Number of SQL instances consuming license units.
        file_share_instances_uses (float | Unset): Number of file share instances consuming license units.
        cosmos_db_instances_uses (float | Unset): Number of Cosmos DB instances consuming license units.
        instances (int | Unset): Total number of license units.
        company (None | str | Unset): Company of the license owner.
        email (None | str | Unset): Email address of the license owner.
        license_expires (datetime.datetime | None | Unset): Date and time of license expiration.
        license_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure to the Veeam
            license.
        support_id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure to the Veeam support
            contract.
        grace_period_days (int | Unset): The number of days provided to install a new license file.
        veeam_online_store_url (None | str | Unset): Link to the Veeam subscription product.
        licensing_server (LicensingServerInfo | Unset): \[Applies if the backup appliance is managed by a Veeam Backup &
            Replication server] Information on the Veeam Backup & Replication server managing the backup appliance.
    """

    license_type: LicenseType | Unset = UNSET
    is_free_edition: bool | Unset = UNSET
    total_instances_uses: float | Unset = UNSET
    vms_instances_uses: float | Unset = UNSET
    sql_instances_uses: float | Unset = UNSET
    file_share_instances_uses: float | Unset = UNSET
    cosmos_db_instances_uses: float | Unset = UNSET
    instances: int | Unset = UNSET
    company: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    license_expires: datetime.datetime | None | Unset = UNSET
    license_id: None | str | Unset = UNSET
    support_id: None | str | Unset = UNSET
    grace_period_days: int | Unset = UNSET
    veeam_online_store_url: None | str | Unset = UNSET
    licensing_server: LicensingServerInfo | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        license_type: str | Unset = UNSET
        if not isinstance(self.license_type, Unset):
            license_type = self.license_type.value

        is_free_edition = self.is_free_edition

        total_instances_uses = self.total_instances_uses

        vms_instances_uses = self.vms_instances_uses

        sql_instances_uses = self.sql_instances_uses

        file_share_instances_uses = self.file_share_instances_uses

        cosmos_db_instances_uses = self.cosmos_db_instances_uses

        instances = self.instances

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        license_expires: None | str | Unset
        if isinstance(self.license_expires, Unset):
            license_expires = UNSET
        elif isinstance(self.license_expires, datetime.datetime):
            license_expires = self.license_expires.isoformat()
        else:
            license_expires = self.license_expires

        license_id: None | str | Unset
        if isinstance(self.license_id, Unset):
            license_id = UNSET
        else:
            license_id = self.license_id

        support_id: None | str | Unset
        if isinstance(self.support_id, Unset):
            support_id = UNSET
        else:
            support_id = self.support_id

        grace_period_days = self.grace_period_days

        veeam_online_store_url: None | str | Unset
        if isinstance(self.veeam_online_store_url, Unset):
            veeam_online_store_url = UNSET
        else:
            veeam_online_store_url = self.veeam_online_store_url

        licensing_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.licensing_server, Unset):
            licensing_server = self.licensing_server.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type
        if is_free_edition is not UNSET:
            field_dict["isFreeEdition"] = is_free_edition
        if total_instances_uses is not UNSET:
            field_dict["totalInstancesUses"] = total_instances_uses
        if vms_instances_uses is not UNSET:
            field_dict["vmsInstancesUses"] = vms_instances_uses
        if sql_instances_uses is not UNSET:
            field_dict["sqlInstancesUses"] = sql_instances_uses
        if file_share_instances_uses is not UNSET:
            field_dict["fileShareInstancesUses"] = file_share_instances_uses
        if cosmos_db_instances_uses is not UNSET:
            field_dict["cosmosDbInstancesUses"] = cosmos_db_instances_uses
        if instances is not UNSET:
            field_dict["instances"] = instances
        if company is not UNSET:
            field_dict["company"] = company
        if email is not UNSET:
            field_dict["email"] = email
        if license_expires is not UNSET:
            field_dict["licenseExpires"] = license_expires
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if support_id is not UNSET:
            field_dict["supportId"] = support_id
        if grace_period_days is not UNSET:
            field_dict["gracePeriodDays"] = grace_period_days
        if veeam_online_store_url is not UNSET:
            field_dict["veeamOnlineStoreUrl"] = veeam_online_store_url
        if licensing_server is not UNSET:
            field_dict["licensingServer"] = licensing_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.licensing_server_info import LicensingServerInfo

        d = dict(src_dict)
        _license_type = d.pop("licenseType", UNSET)
        license_type: LicenseType | Unset
        if isinstance(_license_type, Unset):
            license_type = UNSET
        else:
            license_type = LicenseType(_license_type)

        is_free_edition = d.pop("isFreeEdition", UNSET)

        total_instances_uses = d.pop("totalInstancesUses", UNSET)

        vms_instances_uses = d.pop("vmsInstancesUses", UNSET)

        sql_instances_uses = d.pop("sqlInstancesUses", UNSET)

        file_share_instances_uses = d.pop("fileShareInstancesUses", UNSET)

        cosmos_db_instances_uses = d.pop("cosmosDbInstancesUses", UNSET)

        instances = d.pop("instances", UNSET)

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_license_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                license_expires_type_0 = isoparse(data)

                return license_expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        license_expires = _parse_license_expires(d.pop("licenseExpires", UNSET))

        def _parse_license_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_id = _parse_license_id(d.pop("licenseId", UNSET))

        def _parse_support_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_id = _parse_support_id(d.pop("supportId", UNSET))

        grace_period_days = d.pop("gracePeriodDays", UNSET)

        def _parse_veeam_online_store_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        veeam_online_store_url = _parse_veeam_online_store_url(d.pop("veeamOnlineStoreUrl", UNSET))

        _licensing_server = d.pop("licensingServer", UNSET)
        licensing_server: LicensingServerInfo | Unset
        if isinstance(_licensing_server, Unset):
            licensing_server = UNSET
        else:
            licensing_server = LicensingServerInfo.from_dict(_licensing_server)

        license_info = cls(
            license_type=license_type,
            is_free_edition=is_free_edition,
            total_instances_uses=total_instances_uses,
            vms_instances_uses=vms_instances_uses,
            sql_instances_uses=sql_instances_uses,
            file_share_instances_uses=file_share_instances_uses,
            cosmos_db_instances_uses=cosmos_db_instances_uses,
            instances=instances,
            company=company,
            email=email,
            license_expires=license_expires,
            license_id=license_id,
            support_id=support_id,
            grace_period_days=grace_period_days,
            veeam_online_store_url=veeam_online_store_url,
            licensing_server=licensing_server,
        )

        return license_info
