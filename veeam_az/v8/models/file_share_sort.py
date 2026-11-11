from enum import Enum


class FileShareSort(str, Enum):
    ACCESSTIERASC = "AccessTierAsc"
    ACCESSTIERDESC = "AccessTierDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    REGIONASC = "RegionAsc"
    REGIONDESC = "RegionDesc"

    def __str__(self) -> str:
        return str(self.value)
