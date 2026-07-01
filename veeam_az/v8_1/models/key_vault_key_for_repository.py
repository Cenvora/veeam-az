from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyVaultKeyForRepository")


@_attrs_define
class KeyVaultKeyForRepository:
    """
    Attributes:
        name (None | str | Unset):
        version (None | str | Unset):
        uri (None | str | Unset):
        key_vault_uri (None | str | Unset):
        error (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    uri: None | str | Unset = UNSET
    key_vault_uri: None | str | Unset = UNSET
    error: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        uri: None | str | Unset
        if isinstance(self.uri, Unset):
            uri = UNSET
        else:
            uri = self.uri

        key_vault_uri: None | str | Unset
        if isinstance(self.key_vault_uri, Unset):
            key_vault_uri = UNSET
        else:
            key_vault_uri = self.key_vault_uri

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if uri is not UNSET:
            field_dict["uri"] = uri
        if key_vault_uri is not UNSET:
            field_dict["keyVaultUri"] = key_vault_uri
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uri = _parse_uri(d.pop("uri", UNSET))

        def _parse_key_vault_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_vault_uri = _parse_key_vault_uri(d.pop("keyVaultUri", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        key_vault_key_for_repository = cls(
            name=name,
            version=version,
            uri=uri,
            key_vault_uri=key_vault_uri,
            error=error,
        )

        return key_vault_key_for_repository
