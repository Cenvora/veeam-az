from enum import Enum


class CosmosDbAccountExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    POLICYNAME = "PolicyName"
    PROTECTIONSTATE = "ProtectionState"
    SUBSCRIPTIONNAME = "SubscriptionName"
    TENANT = "Tenant"

    def __str__(self) -> str:
        return str(self.value)
