from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaPolicyNotificationSettings")


@_attrs_define
class SlaPolicyNotificationSettings:
    """
    Attributes:
        enable_notifications (bool | Unset): Defines whether SLA notification is enabled.
        email (None | str | Unset): Email recipient of SLA report.
        include_only_missed_sla_and_removed_vms (bool | None | Unset): Defines whether to include into the report only
            removed VMs and VMs with missed SLA.
        send_on_specific_time (None | str | Unset): Specifies the time when the report will be sent after Veeam Backup
            for Microsoft Azure completes calculating the SLA compliance ratio for all regions protected by the policy. If
            not provided, email notifications will be sent immediately after Veeam Backup for Microsoft Azure completes
            calculating the SLA compliance ratio for all regions protected by the policy.
    """

    enable_notifications: bool | Unset = UNSET
    email: None | str | Unset = UNSET
    include_only_missed_sla_and_removed_vms: bool | None | Unset = UNSET
    send_on_specific_time: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_notifications = self.enable_notifications

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        include_only_missed_sla_and_removed_vms: bool | None | Unset
        if isinstance(self.include_only_missed_sla_and_removed_vms, Unset):
            include_only_missed_sla_and_removed_vms = UNSET
        else:
            include_only_missed_sla_and_removed_vms = self.include_only_missed_sla_and_removed_vms

        send_on_specific_time: None | str | Unset
        if isinstance(self.send_on_specific_time, Unset):
            send_on_specific_time = UNSET
        else:
            send_on_specific_time = self.send_on_specific_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_notifications is not UNSET:
            field_dict["enableNotifications"] = enable_notifications
        if email is not UNSET:
            field_dict["email"] = email
        if include_only_missed_sla_and_removed_vms is not UNSET:
            field_dict["includeOnlyMissedSlaAndRemovedVms"] = include_only_missed_sla_and_removed_vms
        if send_on_specific_time is not UNSET:
            field_dict["sendOnSpecificTime"] = send_on_specific_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_notifications = d.pop("enableNotifications", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_include_only_missed_sla_and_removed_vms(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_only_missed_sla_and_removed_vms = _parse_include_only_missed_sla_and_removed_vms(
            d.pop("includeOnlyMissedSlaAndRemovedVms", UNSET)
        )

        def _parse_send_on_specific_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        send_on_specific_time = _parse_send_on_specific_time(d.pop("sendOnSpecificTime", UNSET))

        sla_policy_notification_settings = cls(
            enable_notifications=enable_notifications,
            email=email,
            include_only_missed_sla_and_removed_vms=include_only_missed_sla_and_removed_vms,
            send_on_specific_time=send_on_specific_time,
        )

        sla_policy_notification_settings.additional_properties = d
        return sla_policy_notification_settings

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
