from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemInfo")


@_attrs_define
class SystemInfo:
    """
    Attributes:
        server_version (None | str | Unset): Currently installed version of Veeam Backup for Microsoft Azure.
        worker_version (None | str | Unset): Version of worker instances launched by Veeam Backup for Microsoft Azure.
        flr_version (None | str | Unset): Version of the File-Level recovery service currently running on the backup
            appliance.
        database_id (UUID | Unset): System ID assigned in the Veeam Backup for Microsoft Azure REST API to the system
            database of the backup appliance.
        copyright_ (None | str | Unset): Text of the copyright notice.
        deployment_subscription_id (str | Unset): Azure Resource ID of subscription in which is the appliance deployed.
    """

    server_version: None | str | Unset = UNSET
    worker_version: None | str | Unset = UNSET
    flr_version: None | str | Unset = UNSET
    database_id: UUID | Unset = UNSET
    copyright_: None | str | Unset = UNSET
    deployment_subscription_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        server_version: None | str | Unset
        if isinstance(self.server_version, Unset):
            server_version = UNSET
        else:
            server_version = self.server_version

        worker_version: None | str | Unset
        if isinstance(self.worker_version, Unset):
            worker_version = UNSET
        else:
            worker_version = self.worker_version

        flr_version: None | str | Unset
        if isinstance(self.flr_version, Unset):
            flr_version = UNSET
        else:
            flr_version = self.flr_version

        database_id: str | Unset = UNSET
        if not isinstance(self.database_id, Unset):
            database_id = str(self.database_id)

        copyright_: None | str | Unset
        if isinstance(self.copyright_, Unset):
            copyright_ = UNSET
        else:
            copyright_ = self.copyright_

        deployment_subscription_id = self.deployment_subscription_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if server_version is not UNSET:
            field_dict["serverVersion"] = server_version
        if worker_version is not UNSET:
            field_dict["workerVersion"] = worker_version
        if flr_version is not UNSET:
            field_dict["flrVersion"] = flr_version
        if database_id is not UNSET:
            field_dict["databaseId"] = database_id
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if deployment_subscription_id is not UNSET:
            field_dict["deploymentSubscriptionId"] = deployment_subscription_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_server_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_version = _parse_server_version(d.pop("serverVersion", UNSET))

        def _parse_worker_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        worker_version = _parse_worker_version(d.pop("workerVersion", UNSET))

        def _parse_flr_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flr_version = _parse_flr_version(d.pop("flrVersion", UNSET))

        _database_id = d.pop("databaseId", UNSET)
        database_id: UUID | Unset
        if isinstance(_database_id, Unset):
            database_id = UNSET
        else:
            database_id = UUID(_database_id)

        def _parse_copyright_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        copyright_ = _parse_copyright_(d.pop("copyright", UNSET))

        deployment_subscription_id = d.pop("deploymentSubscriptionId", UNSET)

        system_info = cls(
            server_version=server_version,
            worker_version=worker_version,
            flr_version=flr_version,
            database_id=database_id,
            copyright_=copyright_,
            deployment_subscription_id=deployment_subscription_id,
        )

        return system_info
