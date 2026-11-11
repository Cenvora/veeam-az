from enum import Enum


class SqlServerExpansion(str, Enum):
    ALL = "All"
    ELASTICPOOLS = "ElasticPools"
    NONE = "None"
    REGION = "Region"
    RESOURCEGROUP = "ResourceGroup"
    SUBSCRIPTION = "Subscription"
    TENANT = "Tenant"

    def __str__(self) -> str:
        return str(self.value)
