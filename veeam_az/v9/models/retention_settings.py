from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links_dictionary_type_0 import LinksDictionaryType0
    from ..models.retention_setting import RetentionSetting


T = TypeVar("T", bound="RetentionSettings")


@_attrs_define
class RetentionSettings:
    """
    Attributes:
        sessions_settings (RetentionSetting): Global retention settings for keeping session records (for
            `sessionsSettings`, the minimum possible value is 1 day) or snapshots of unprotected Azure VMs (for
            `obsoleteSnapshotsSettings`, the minimum possible value is 15 days).
        obsolete_snapshots_settings (RetentionSetting): Global retention settings for keeping session records (for
            `sessionsSettings`, the minimum possible value is 1 day) or snapshots of unprotected Azure VMs (for
            `obsoleteSnapshotsSettings`, the minimum possible value is 15 days).
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    sessions_settings: RetentionSetting
    obsolete_snapshots_settings: RetentionSetting
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        sessions_settings = self.sessions_settings.to_dict()

        obsolete_snapshots_settings = self.obsolete_snapshots_settings.to_dict()

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sessionsSettings": sessions_settings,
                "obsoleteSnapshotsSettings": obsolete_snapshots_settings,
            }
        )
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0
        from ..models.retention_setting import RetentionSetting

        d = dict(src_dict)
        sessions_settings = RetentionSetting.from_dict(d.pop("sessionsSettings"))

        obsolete_snapshots_settings = RetentionSetting.from_dict(d.pop("obsoleteSnapshotsSettings"))

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

        retention_settings = cls(
            sessions_settings=sessions_settings,
            obsolete_snapshots_settings=obsolete_snapshots_settings,
            field_links=field_links,
        )

        return retention_settings
