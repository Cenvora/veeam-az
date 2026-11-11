from enum import Enum


class WorkerNetworkConfigurationSort(str, Enum):
    CONFIGURATIONTYPEASC = "ConfigurationTypeAsc"
    CONFIGURATIONTYPEDESC = "ConfigurationTypeDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"
    STATUSASC = "StatusAsc"
    STATUSDESC = "StatusDesc"
    SUBNETASC = "SubnetAsc"
    SUBNETDESC = "SubnetDesc"
    SUBSCRIPTIONASC = "SubscriptionAsc"
    SUBSCRIPTIONDESC = "SubscriptionDesc"
    VIRTUALNETWORKASC = "VirtualNetworkAsc"
    VIRTUALNETWORKDESC = "VirtualNetworkDesc"

    def __str__(self) -> str:
        return str(self.value)
