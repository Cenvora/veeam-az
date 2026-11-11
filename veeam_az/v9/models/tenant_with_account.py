from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_account import AzureAccount
    from ..models.links_dictionary_type_0 import LinksDictionaryType0


T = TypeVar("T", bound="TenantWithAccount")


@_attrs_define
class TenantWithAccount:
    """Information on each account linked to the returned tenant.

    Attributes:
        id (None | str | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the unique
            combination of a tenant and a service account in Veeam Backup for Microsoft Azure.
        account (AzureAccount | Unset): Information on a service account.
        tenant_id (None | str | Unset): Specifies the Microsoft Azure ID assigned to a tenant with which the service
            account is associated.
        name (None | str | Unset): Name of the tenant.
        field_links (LinksDictionaryType0 | None | Unset): URLs of operations where the properties obtained in the
            response can be used as an input.
    """

    id: None | str | Unset = UNSET
    account: AzureAccount | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    field_links: LinksDictionaryType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, LinksDictionaryType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account is not UNSET:
            field_dict["account"] = account
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if name is not UNSET:
            field_dict["name"] = name
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_account import AzureAccount
        from ..models.links_dictionary_type_0 import LinksDictionaryType0

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _account = d.pop("account", UNSET)
        account: AzureAccount | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = AzureAccount.from_dict(_account)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        tenant_with_account = cls(
            id=id,
            account=account,
            tenant_id=tenant_id,
            name=name,
            field_links=field_links,
        )

        return tenant_with_account
