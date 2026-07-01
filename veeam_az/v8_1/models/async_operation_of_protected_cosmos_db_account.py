from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.async_operation_of_protected_cosmos_db_account_links import (
        AsyncOperationOfProtectedCosmosDbAccountLinks,
    )
    from ..models.problem_details import ProblemDetails
    from ..models.protected_cosmos_db_account import ProtectedCosmosDbAccount


T = TypeVar("T", bound="AsyncOperationOfProtectedCosmosDbAccount")


@_attrs_define
class AsyncOperationOfProtectedCosmosDbAccount:
    r"""Information on the session.

    Attributes:
        id (UUID): System ID assigned to the session in the Veeam Backup for Microsoft Azure REST API.
        start_time (datetime.datetime): Date and time when the session started.
        status (JobStatus): Specifies the status of the performed session.
        error (ProblemDetails | Unset): \[Applies only if the session completes with an error] Information on the error.
        field_links (AsyncOperationOfProtectedCosmosDbAccountLinks | Unset): URLs of operations where the properties
            obtained in the response can be used as an input.
        result (ProtectedCosmosDbAccount | Unset): Information on a Cosmos DB account protected by Veeam Backup for
            Microsoft Azure.
    """

    id: UUID
    start_time: datetime.datetime
    status: JobStatus
    error: ProblemDetails | Unset = UNSET
    field_links: AsyncOperationOfProtectedCosmosDbAccountLinks | Unset = UNSET
    result: ProtectedCosmosDbAccount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        start_time = self.start_time.isoformat()

        status = self.status.value

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "startTime": start_time,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.async_operation_of_protected_cosmos_db_account_links import (
            AsyncOperationOfProtectedCosmosDbAccountLinks,
        )
        from ..models.problem_details import ProblemDetails
        from ..models.protected_cosmos_db_account import ProtectedCosmosDbAccount

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        start_time = isoparse(d.pop("startTime"))

        status = JobStatus(d.pop("status"))

        _error = d.pop("error", UNSET)
        error: ProblemDetails | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ProblemDetails.from_dict(_error)

        _field_links = d.pop("_links", UNSET)
        field_links: AsyncOperationOfProtectedCosmosDbAccountLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = AsyncOperationOfProtectedCosmosDbAccountLinks.from_dict(_field_links)

        _result = d.pop("result", UNSET)
        result: ProtectedCosmosDbAccount | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ProtectedCosmosDbAccount.from_dict(_result)

        async_operation_of_protected_cosmos_db_account = cls(
            id=id,
            start_time=start_time,
            status=status,
            error=error,
            field_links=field_links,
            result=result,
        )

        async_operation_of_protected_cosmos_db_account.additional_properties = d
        return async_operation_of_protected_cosmos_db_account

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
