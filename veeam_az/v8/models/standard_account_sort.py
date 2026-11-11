from enum import Enum


class StandardAccountSort(str, Enum):
    DESCRIPTIONASC = "DescriptionAsc"
    DESCRIPTIONDESC = "DescriptionDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"
    TYPEASC = "TypeAsc"
    TYPEDESC = "TypeDesc"
    USERNAMEASC = "UsernameAsc"
    USERNAMEDESC = "UsernameDesc"

    def __str__(self) -> str:
        return str(self.value)
