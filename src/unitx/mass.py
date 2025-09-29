from enum import Enum
from .exceptions import UnsupportedUnitError, InvalidUnitError, NonNumericError

class Mass(Enum):
    KILOGRAM = 1.0
    GRAM = 0.001
    MILLIGRAM = 0.000001
    MICROGRAM = 1e-9
    TONNE = 1000.0
    POUND = 0.45359237
    OUNCE = 0.0283495231
    STONE = 6.35029318

def convert_mass(value: float, from_unit: Mass, to_unit: Mass)  -> float:
    """Convert a mass value from a unit to another unit.

    Args:
        value (float): The numeric value to convert.
        from_unit (Mass): The unit you are converting from.
        to_unit (Mass): The unit you are converting to.

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
    
    # Check if from unit is from Mass Enum
    if not isinstance(from_unit, Mass):
        raise InvalidUnitError(f"From unit must be from the Mass enum, got {type(from_unit).__name__}")
    
    return value * from_unit.value / to_unit.value
