from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vnet_deletion_type import VnetDeletionType

T = TypeVar("T", bound="ProtectedVnetToDelete")


@_attrs_define
class ProtectedVnetToDelete:
    """
    Attributes:
        subscription_id (None | UUID): Specifies the Microsoft Azure ID assigned to a subscription whose virtual network
            configuration restore points will be removed from the Veeam Backup for Microsoft Azure configuration database.
        deletion_type (VnetDeletionType): Specifies the type of backups that will be removed.
    """

    subscription_id: None | UUID
    deletion_type: VnetDeletionType

    def to_dict(self) -> dict[str, Any]:
        subscription_id: None | str
        if isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        deletion_type = self.deletion_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "subscriptionId": subscription_id,
                "deletionType": deletion_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_subscription_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)

                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId"))

        deletion_type = VnetDeletionType(d.pop("deletionType"))

        protected_vnet_to_delete = cls(
            subscription_id=subscription_id,
            deletion_type=deletion_type,
        )

        return protected_vnet_to_delete
