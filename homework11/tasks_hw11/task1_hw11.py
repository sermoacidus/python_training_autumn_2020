"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
assert ColorsEnum.RED == "RED"
"""


class SimplifiedEnum(type):
    def __new__(cls, name, bases, dct):
        attributes_to_add = {}
        for key, value in dct.items():
            if key.endswith("__keys"):
                for item in value:
                    attributes_to_add[item.__str__()] = item
        new_attributes = {**dct, **attributes_to_add}
        cls_instance = super().__new__(cls, name, bases, new_attributes)
        return cls_instance


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
