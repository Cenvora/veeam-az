from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.protection_policy_sla_report import ProtectionPolicySlaReport


T = TypeVar("T", bound="VmProtectionPolicyWithSla")


@_attrs_define
class VmProtectionPolicyWithSla:
    """
    Attributes:
        id (UUID): System ID assigned to an SLA-based backup policy in the Veeam Backup for Microsoft Azure REST API.
        priority (int | Unset): Priority ordinal number of the SLA-based backup policy.
        excluded_items_count (int | Unset): Number of items excluded from the policy.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
        name (None | str | Unset): Name of the policy.
        description (None | str | Unset): Description of the policy.
        is_enabled (bool | None | Unset): Defines whether the policy is enabled.
        snapshot_sla_report (ProtectionPolicySlaReport | Unset): SLA compliance report for each schedule type.
        backup_sla_report (ProtectionPolicySlaReport | Unset): SLA compliance report for each schedule type.
        archive_sla_report (ProtectionPolicySlaReport | Unset): SLA compliance report for each schedule type.
    """

    id: UUID
    priority: int | Unset = UNSET
    excluded_items_count: int | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    snapshot_sla_report: ProtectionPolicySlaReport | Unset = UNSET
    backup_sla_report: ProtectionPolicySlaReport | Unset = UNSET
    archive_sla_report: ProtectionPolicySlaReport | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id = str(self.id)

        priority = self.priority

        excluded_items_count = self.excluded_items_count

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

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

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        snapshot_sla_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_sla_report, Unset):
            snapshot_sla_report = self.snapshot_sla_report.to_dict()

        backup_sla_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_sla_report, Unset):
            backup_sla_report = self.backup_sla_report.to_dict()

        archive_sla_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.archive_sla_report, Unset):
            archive_sla_report = self.archive_sla_report.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if excluded_items_count is not UNSET:
            field_dict["excludedItemsCount"] = excluded_items_count
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if snapshot_sla_report is not UNSET:
            field_dict["snapshotSlaReport"] = snapshot_sla_report
        if backup_sla_report is not UNSET:
            field_dict["backupSlaReport"] = backup_sla_report
        if archive_sla_report is not UNSET:
            field_dict["archiveSlaReport"] = archive_sla_report

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.protection_policy_sla_report import ProtectionPolicySlaReport

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        priority = d.pop("priority", UNSET)

        excluded_items_count = d.pop("excludedItemsCount", UNSET)

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

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        _snapshot_sla_report = d.pop("snapshotSlaReport", UNSET)
        snapshot_sla_report: ProtectionPolicySlaReport | Unset
        if isinstance(_snapshot_sla_report, Unset):
            snapshot_sla_report = UNSET
        else:
            snapshot_sla_report = ProtectionPolicySlaReport.from_dict(_snapshot_sla_report)

        _backup_sla_report = d.pop("backupSlaReport", UNSET)
        backup_sla_report: ProtectionPolicySlaReport | Unset
        if isinstance(_backup_sla_report, Unset):
            backup_sla_report = UNSET
        else:
            backup_sla_report = ProtectionPolicySlaReport.from_dict(_backup_sla_report)

        _archive_sla_report = d.pop("archiveSlaReport", UNSET)
        archive_sla_report: ProtectionPolicySlaReport | Unset
        if isinstance(_archive_sla_report, Unset):
            archive_sla_report = UNSET
        else:
            archive_sla_report = ProtectionPolicySlaReport.from_dict(_archive_sla_report)

        vm_protection_policy_with_sla = cls(
            id=id,
            priority=priority,
            excluded_items_count=excluded_items_count,
            field_links=field_links,
            name=name,
            description=description,
            is_enabled=is_enabled,
            snapshot_sla_report=snapshot_sla_report,
            backup_sla_report=backup_sla_report,
            archive_sla_report=archive_sla_report,
        )

        return vm_protection_policy_with_sla
