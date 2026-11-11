from enum import Enum


class AccountEditValidationIssueType(str, Enum):
    ACCOUNTDEPENDENTACCOUNT = "AccountDependentAccount"
    ACCOUNTDEPENDENTPOLICY = "AccountDependentPolicy"
    ACCOUNTDEPENDENTREPOSITORY = "AccountDependentRepository"
    PRIMARYSUBSCRIPTIONMISSING = "PrimarySubscriptionMissing"
    PURPOSECOSMOSPOLICYDEPENDENT = "PurposeCosmosPolicyDependent"
    PURPOSEFILEPOLICYDEPENDENT = "PurposeFilePolicyDependent"
    PURPOSEREPOSITORYDEPENDENT = "PurposeRepositoryDependent"
    PURPOSESQLPOLICYDEPENDENT = "PurposeSqlPolicyDependent"
    PURPOSEVMPOLICYDEPENDENT = "PurposeVmPolicyDependent"
    PURPOSEVNETPOLICYDEPENDENT = "PurposeVNetPolicyDependent"
    SELECTEDFORWORKERMANAGEMENT = "SelectedForWorkerManagement"
    SUBSCRIPTIONDEPENDENTONPOLICY = "SubscriptionDependentOnPolicy"
    SUBSCRIPTIONDEPENDENTONREPOSITORY = "SubscriptionDependentOnRepository"

    def __str__(self) -> str:
        return str(self.value)
