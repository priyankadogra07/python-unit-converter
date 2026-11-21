# Python Unit Converter

A simple command-line program that converts values between common length, mass, and time units. It uses only Python's built-in features and needs no extra packages.

## Features

- Converts between units within the same category.
- Supports length, mass, and time.
- Prompts for a value, category, starting unit, and target unit.
- Handles invalid numbers and unknown categories or units with a message.

## Supported units

| Category | Units |
| --- | --- |
| Length | `m`, `km`, `cm`, `mm`, `mi`, `ft`, `in` |
| Mass | `kg`, `g`, `lb`, `oz` |
| Time | `s`, `min`, `h`, `day` |

## Requirements

- Python 3
- No third-party libraries

## Run the program

1. Save the code in a file named `unit_converter.py`.
2. Open Command Prompt or PowerShell in the folder containing the file.
3. Run:

   ```bash
   python unit_converter.py
   ```

4. Follow the prompts. Use the category names and unit abbreviations listed above.

## Example

```text
Value: 5
Category (length, mass, time): length
Convert from: km
Convert to: m
5 km = 5000 m
```

## How conversion works

Each unit is represented by a factor relative to a base unit for its category: metres for length, kilograms for mass, and seconds for time. The program converts with this formula:

```text
converted value = input value * source unit factor / target unit factor
```

## Limitations

- Conversion is supported only between units in the same category.
- Temperature and other measurement categories are not included.
- Enter unit abbreviations as shown in the supported units table.
