CONVERSIONS = {
    "length": {
        "m": 1,
        "km": 1_000,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1_609.344,
        "ft": 0.3048,
        "in": 0.0254,
    },
    "mass": {
        "kg": 1,
        "g": 0.001,
        "lb": 0.45359237,
        "oz": 0.028349523125,
    },
    "time": {
        "s": 1,
        "min": 60,
        "h": 3_600,
        "day": 86_400,
    },
}

def convert(value: float, category: str, from_unit: str, to_unit: str) -> float:
    """Convert between units in the same category."""
    units = CONVERSIONS[category.lower()]
    return value * units[from_unit.lower()] / units[to_unit.lower()]

try:
    value = float(input("Value: "))
    category = input("Category (length, mass, time): ").strip()
    from_unit = input("Convert from: ").strip()
    to_unit = input("Convert to: ").strip()

    result = convert(value, category, from_unit, to_unit)
    print(f"{value:g} {from_unit} = {result:g} {to_unit}")
except KeyError:
    print("Unknown category or unit.")
except ValueError:
    print("Please enter a valid number.")