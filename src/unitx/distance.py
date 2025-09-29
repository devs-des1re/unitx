"""Converts units of distances"""
from enum import Enum
from .exceptions import UnsupportedUnitError, InvalidUnitError, NonNumericError

class Distance(Enum):
    """Class for which contains Distance Enums.

    Args:
        Enum (float): The Distance Enum.
    """
    METERS = 1.0
    KILOMETERS = 1000.0
    CENTIMETERS = 0.01
    MILLIMETERS = 0.001
    FEET = 0.3048
    INCHES = 0.0254
    YARDS = 0.9144
    MILES = 1609.34

def convert_distance(value: float, from_unit: Distance, to_unit: Distance)  -> float:
    """Convert a distance value from a unit to another unit.

    Args:
        value (float): The numeric value to convert.
        from_unit (Distance): The unit you are converting from.
        to_unit (Distance): The unit you are converting to.

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

    # Check if from unit is from Distance Enum
    if not isinstance(from_unit, Distance):
        raise InvalidUnitError(f"From unit must be from the Distance enum, got {type(from_unit).__name__}")

    return value * from_unit.value / to_unit.value
