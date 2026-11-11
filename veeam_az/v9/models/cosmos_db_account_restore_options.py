from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cosmos_db_account_restorable_resource import CosmosDbAccountRestorableResource


T = TypeVar("T", bound="CosmosDbAccountRestoreOptions")


@_attrs_define
class CosmosDbAccountRestoreOptions:
    r"""Specifies information for the Cosmos DB account point-in-time restore.

    Attributes:
        service_account_id (UUID): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure to a service
            account that will be used for the restore operation.
        target_region_id (str): Specifies a Microsoft Azure ID assigned to a region to which the data will be restored.
        target_resource_group_id (str): Specifies the system ID assigned in the Veeam Backup for Microsoft Azure to a
            resource group to which the data will be restored.
        point_in_time (datetime.datetime): Specifies the date and time to which the data will be restored. Consider that
            the specified value must be within the available point-in-time restore period. To obtain this period for the
            Cosmos DB account, see [Get Cosmos DB Account Point-in-time Restore
            Period](#tag/System/operation/AzureCosmosDbAccounts_GetAvailableRestoreTimeRange).
        target_name (str): Specifies a name for the target Cosmos DB account that will be created by the restore
            process.
        reason (None | str | Unset): Specifies a reason for the restore operation.
        selected_items (list[CosmosDbAccountRestorableResource] | None | Unset): \[Applies to Cosmos DB accounts of the
            following kinds only&#58; NoSQL, MongoDB, Apache Gremlin and Table] Specifies items that will be restored.
    """

    service_account_id: UUID
    target_region_id: str
    target_resource_group_id: str
    point_in_time: datetime.datetime
    target_name: str
    reason: None | str | Unset = UNSET
    selected_items: list[CosmosDbAccountRestorableResource] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_account_id = str(self.service_account_id)

        target_region_id = self.target_region_id

        target_resource_group_id = self.target_resource_group_id

        point_in_time = self.point_in_time.isoformat()

        target_name = self.target_name

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        selected_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.selected_items, Unset):
            selected_items = UNSET
        elif isinstance(self.selected_items, list):
            selected_items = []
            for selected_items_type_0_item_data in self.selected_items:
                selected_items_type_0_item = selected_items_type_0_item_data.to_dict()
                selected_items.append(selected_items_type_0_item)

        else:
            selected_items = self.selected_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ServiceAccountId": service_account_id,
                "TargetRegionId": target_region_id,
                "TargetResourceGroupId": target_resource_group_id,
                "PointInTime": point_in_time,
                "TargetName": target_name,
            }
        )
        if reason is not UNSET:
            field_dict["Reason"] = reason
        if selected_items is not UNSET:
            field_dict["SelectedItems"] = selected_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cosmos_db_account_restorable_resource import CosmosDbAccountRestorableResource

        d = dict(src_dict)
        service_account_id = UUID(d.pop("ServiceAccountId"))

        target_region_id = d.pop("TargetRegionId")

        target_resource_group_id = d.pop("TargetResourceGroupId")

        point_in_time = isoparse(d.pop("PointInTime"))

        target_name = d.pop("TargetName")

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("Reason", UNSET))

        def _parse_selected_items(data: object) -> list[CosmosDbAccountRestorableResource] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_items_type_0 = []
                _selected_items_type_0 = data
                for selected_items_type_0_item_data in _selected_items_type_0:
                    selected_items_type_0_item = CosmosDbAccountRestorableResource.from_dict(
                        selected_items_type_0_item_data
                    )

                    selected_items_type_0.append(selected_items_type_0_item)

                return selected_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CosmosDbAccountRestorableResource] | None | Unset, data)

        selected_items = _parse_selected_items(d.pop("SelectedItems", UNSET))

        cosmos_db_account_restore_options = cls(
            service_account_id=service_account_id,
            target_region_id=target_region_id,
            target_resource_group_id=target_resource_group_id,
            point_in_time=point_in_time,
            target_name=target_name,
            reason=reason,
            selected_items=selected_items,
        )

        cosmos_db_account_restore_options.additional_properties = d
        return cosmos_db_account_restore_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
