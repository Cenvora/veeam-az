from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.protection_status import ProtectionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileShareExportOptions")


@_attrs_define
class FileShareExportOptions:
    """
    Attributes:
        file_share_ids (list[str] | None | Unset): Specifies the system IDs assigned in the Veeam Backup for Microsoft
            Azure REST API to the Azure file shares whose data will be exported.
        region_ids (list[str] | None | Unset): Returns only file shares that reside in Azure regions with the specified
            IDs.
        search_pattern (None | str | Unset): Returns only those items of a resource collection whose names match the
            specified search pattern in the parameter value.
        subscription_id (None | Unset | UUID): Returns only file shares available in a subscription with the specified
            ID.
        tenant_id (None | Unset | UUID): Returns only file shares available for a tenant with the specified ID.
        service_account_id (None | str | Unset): Returns only file shares to which a service account ith the specified
            ID has access.
        file_share_from_protected_regions (bool | Unset): Defines whether Veeam Backup for Microsoft Azure must return
            only file shares that reside in regions protected by backup policies.
        protection_status (list[ProtectionStatus] | None | Unset): Returns only file shares with the specified
            protection status.
    """

    file_share_ids: list[str] | None | Unset = UNSET
    region_ids: list[str] | None | Unset = UNSET
    search_pattern: None | str | Unset = UNSET
    subscription_id: None | Unset | UUID = UNSET
    tenant_id: None | Unset | UUID = UNSET
    service_account_id: None | str | Unset = UNSET
    file_share_from_protected_regions: bool | Unset = UNSET
    protection_status: list[ProtectionStatus] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_share_ids: list[str] | None | Unset
        if isinstance(self.file_share_ids, Unset):
            file_share_ids = UNSET
        elif isinstance(self.file_share_ids, list):
            file_share_ids = self.file_share_ids

        else:
            file_share_ids = self.file_share_ids

        region_ids: list[str] | None | Unset
        if isinstance(self.region_ids, Unset):
            region_ids = UNSET
        elif isinstance(self.region_ids, list):
            region_ids = self.region_ids

        else:
            region_ids = self.region_ids

        search_pattern: None | str | Unset
        if isinstance(self.search_pattern, Unset):
            search_pattern = UNSET
        else:
            search_pattern = self.search_pattern

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        elif isinstance(self.tenant_id, UUID):
            tenant_id = str(self.tenant_id)
        else:
            tenant_id = self.tenant_id

        service_account_id: None | str | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id

        file_share_from_protected_regions = self.file_share_from_protected_regions

        protection_status: list[str] | None | Unset
        if isinstance(self.protection_status, Unset):
            protection_status = UNSET
        elif isinstance(self.protection_status, list):
            protection_status = []
            for protection_status_type_0_item_data in self.protection_status:
                protection_status_type_0_item = protection_status_type_0_item_data.value
                protection_status.append(protection_status_type_0_item)

        else:
            protection_status = self.protection_status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_share_ids is not UNSET:
            field_dict["fileShareIds"] = file_share_ids
        if region_ids is not UNSET:
            field_dict["regionIds"] = region_ids
        if search_pattern is not UNSET:
            field_dict["searchPattern"] = search_pattern
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if service_account_id is not UNSET:
            field_dict["serviceAccountId"] = service_account_id
        if file_share_from_protected_regions is not UNSET:
            field_dict["fileShareFromProtectedRegions"] = file_share_from_protected_regions
        if protection_status is not UNSET:
            field_dict["protectionStatus"] = protection_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_file_share_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_share_ids_type_0 = cast(list[str], data)

                return file_share_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        file_share_ids = _parse_file_share_ids(d.pop("fileShareIds", UNSET))

        def _parse_region_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                region_ids_type_0 = cast(list[str], data)

                return region_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        region_ids = _parse_region_ids(d.pop("regionIds", UNSET))

        def _parse_search_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_pattern = _parse_search_pattern(d.pop("searchPattern", UNSET))

        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_tenant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_id_type_0 = UUID(data)

                return tenant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_service_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("serviceAccountId", UNSET))

        file_share_from_protected_regions = d.pop("fileShareFromProtectedRegions", UNSET)

        def _parse_protection_status(data: object) -> list[ProtectionStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protection_status_type_0 = []
                _protection_status_type_0 = data
                for protection_status_type_0_item_data in _protection_status_type_0:
                    protection_status_type_0_item = ProtectionStatus(protection_status_type_0_item_data)

                    protection_status_type_0.append(protection_status_type_0_item)

                return protection_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProtectionStatus] | None | Unset, data)

        protection_status = _parse_protection_status(d.pop("protectionStatus", UNSET))

        file_share_export_options = cls(
            file_share_ids=file_share_ids,
            region_ids=region_ids,
            search_pattern=search_pattern,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            service_account_id=service_account_id,
            file_share_from_protected_regions=file_share_from_protected_regions,
            protection_status=protection_status,
        )

        return file_share_export_options
