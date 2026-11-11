from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_from_client import TagFromClient
    from ..models.user_scripts import UserScripts


T = TypeVar("T", bound="SnapshotSettings")


@_attrs_define
class SnapshotSettings:
    """Specifies cloud-native snapshot settings for the backup policy.

    Attributes:
        additional_tags (list[TagFromClient] | None | Unset): Specifies tags to be assigned to the snapshots.
        copy_original_tags (bool | Unset): Defines whether to assign to the snapshots tags of virtual disks attached to
            processed Azure VMs.
        application_aware_snapshot (bool | Unset): Defines whether to enable application-aware processing for Windows-
            based Azure VMs running VSS-aware applications.
        user_scripts (UserScripts | Unset): Specifies script settings to be applied before and after the snapshot
            creating operation.
    """

    additional_tags: list[TagFromClient] | None | Unset = UNSET
    copy_original_tags: bool | Unset = UNSET
    application_aware_snapshot: bool | Unset = UNSET
    user_scripts: UserScripts | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        additional_tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.additional_tags, Unset):
            additional_tags = UNSET
        elif isinstance(self.additional_tags, list):
            additional_tags = []
            for additional_tags_type_0_item_data in self.additional_tags:
                additional_tags_type_0_item = additional_tags_type_0_item_data.to_dict()
                additional_tags.append(additional_tags_type_0_item)

        else:
            additional_tags = self.additional_tags

        copy_original_tags = self.copy_original_tags

        application_aware_snapshot = self.application_aware_snapshot

        user_scripts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_scripts, Unset):
            user_scripts = self.user_scripts.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if additional_tags is not UNSET:
            field_dict["additionalTags"] = additional_tags
        if copy_original_tags is not UNSET:
            field_dict["copyOriginalTags"] = copy_original_tags
        if application_aware_snapshot is not UNSET:
            field_dict["applicationAwareSnapshot"] = application_aware_snapshot
        if user_scripts is not UNSET:
            field_dict["userScripts"] = user_scripts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag_from_client import TagFromClient
        from ..models.user_scripts import UserScripts

        d = dict(src_dict)

        def _parse_additional_tags(data: object) -> list[TagFromClient] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_tags_type_0 = []
                _additional_tags_type_0 = data
                for additional_tags_type_0_item_data in _additional_tags_type_0:
                    additional_tags_type_0_item = TagFromClient.from_dict(additional_tags_type_0_item_data)

                    additional_tags_type_0.append(additional_tags_type_0_item)

                return additional_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TagFromClient] | None | Unset, data)

        additional_tags = _parse_additional_tags(d.pop("additionalTags", UNSET))

        copy_original_tags = d.pop("copyOriginalTags", UNSET)

        application_aware_snapshot = d.pop("applicationAwareSnapshot", UNSET)

        _user_scripts = d.pop("userScripts", UNSET)
        user_scripts: UserScripts | Unset
        if isinstance(_user_scripts, Unset):
            user_scripts = UNSET
        else:
            user_scripts = UserScripts.from_dict(_user_scripts)

        snapshot_settings = cls(
            additional_tags=additional_tags,
            copy_original_tags=copy_original_tags,
            application_aware_snapshot=application_aware_snapshot,
            user_scripts=user_scripts,
        )

        return snapshot_settings
