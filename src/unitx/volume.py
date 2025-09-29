from enum import Enum
from .exceptions import UnsupportedUnitError, InvalidUnitError, NonNumericError

class Volume(Enum):
    LITER = 1.0
    MILLILITER = 0.001
    CUBIC_METER = 1000.0
    CUBIC_CENTIMETER = 0.001
    GALLON_US = 3.78541
    QUART_US = 0.946353
    PINT_US = 0.473176
    CUP_US = 0.24
    FLUID_OUNCE_US = 0.0295735
    TABLESPOON_US = 0.0147868
    TEASPOON_US = 0.00492892

def convert_volume(value: float, from_unit: Volume, to_unit: Volume)  -> float:
    """Convert a volume value from a unit to another unit.

    Args:
        value (float): The numeric value to convert.
        from_unit (Volume): The unit you are converting from.
        to_unit (Volume): The unit you are converting to.

    Raises:
        NonNumericError: Raised when value is not int or float.
        UnsupportedUnitError: Raised when a unit is not recognized.
        InvalidUnitError: Raised when units are from a different category.

    Returns:
        float: The converted numeric value
    """

    # Check if value is numeric
    if not isinstance(value, (int, float)):
        raise NonNumericError(f"Value must be numeric, got {type(value).__name__}")
    
    # Check if units are valid Enum members
    if not isinstance(from_unit, Enum):
        raise UnsupportedUnitError(f"From unit must be enum, got {type(from_unit).__name__}")
    
    if not isinstance(to_unit, Enum):
        raise UnsupportedUnitError(f"From unit must be enum, got {type(to_unit).__name__}")
    
    # Check if category mismatch
    if from_unit.__class__ is not to_unit.__class__:
        raise InvalidUnitError(f"From unit and to unit must be from the category, got {type(from_unit).__name__}, {type(from_unit).__name__}")
    
    # Check if from unit is from Volume Enum
    if not isinstance(from_unit, Volume):
        raise InvalidUnitError(f"From unit must be from the Volume enum, got {type(from_unit).__name__}")
    
    return value * from_unit.value / to_unit.value
