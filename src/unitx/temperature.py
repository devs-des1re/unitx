from enum import Enum
from .exceptions import UnsupportedUnitError, InvalidUnitError, NonNumericError

class Temperature(Enum):
    CELSIUS = "C"
    FAHRENHEIT = "F"
    KELVIN = "K"
    RANKINE = "R"

def convert_temperature(value: float, from_unit: Temperature, to_unit: Temperature) -> float:
    """Convert a temperature value from a unit to another unit.

    Args:
        value (float): The numeric value to convert.
        from_unit (Temperature): The unit you are converting from.
        to_unit (Temperature): The unit you are converting to.

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
    
    # Check if from unit is from Temperature Enum
    if not isinstance(from_unit, Temperature):
        raise InvalidUnitError(f"From unit must be from the Temperature enum, got {type(from_unit).__name__}")
    
    if from_unit == Temperature.CELSIUS:
        celsius = value
    elif from_unit == Temperature.FAHRENHEIT:
        celsius = (value - 32) * 5/9
    elif from_unit == Temperature.KELVIN:
        celsius = value - 273.15
    elif from_unit == Temperature.RANKINE:
        celsius = (value - 491.67) * 5/9

    # Convert from Celsius to target unit
    if to_unit == Temperature.CELSIUS:
        return celsius
    elif to_unit == Temperature.FAHRENHEIT:
        return celsius * 9/5 + 32
    elif to_unit == Temperature.KELVIN:
        return celsius + 273.15
    elif to_unit == Temperature.RANKINE:
        return (celsius + 273.15) * 9/5
