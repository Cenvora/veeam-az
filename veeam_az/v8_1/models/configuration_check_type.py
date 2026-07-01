from enum import Enum


class ConfigurationCheckType(str, Enum):
    ALLPRIVATEDEPLOYMENT = "AllPrivateDeployment"
    AZUREACCOUNTS = "AzureAccounts"
    PORTALUSERS = "PortalUsers"
    REPOSITORIES = "Repositories"
    REPOSITORIESENCRYPTION = "RepositoriesEncryption"
    REPOSITORIESOWNERSHIP = "RepositoriesOwnership"
    SSOUSERS = "SsoUsers"
    UNKNOWN = "Unknown"
    WORKERCONFIGURATION = "WorkerConfiguration"

    def __str__(self) -> str:
        return str(self.value)
