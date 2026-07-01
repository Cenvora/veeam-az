from enum import Enum


class VnetResourceType(str, Enum):
    NETWORKINTERFACE = "NetworkInterface"
    NETWORKSECURITYGROUP = "NetworkSecurityGroup"
    PUBLICIPADDRESS = "PublicIpAddress"
    ROUTETABLE = "RouteTable"
    SUBNET = "Subnet"
    UNKNOWN = "Unknown"
    VIRTUALNETWORK = "VirtualNetwork"
    VIRTUALNETWORKPEERING = "VirtualNetworkPeering"

    def __str__(self) -> str:
        return str(self.value)
