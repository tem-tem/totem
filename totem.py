#!/usr/bin/env python3
import argparse
import sys
import re
import shlex  # Handles shell argument parsing correctly
from sympy import sympify, SympifyError

# Safe Calculator Function using sympy
def calculate(expression: str):
    """Evaluates a mathematical expression safely using sympy."""
    try:
        result = sympify(expression).evalf()  # Parse and evaluate expression
        return result
    except (SympifyError, ZeroDivisionError) as e:
        raise ValueError(f"Invalid expression: {e}")

# Time Conversion Functions
def parse_time_input(time_str: str):
    """Parses time input with various separators and returns hours, minutes, and optionally seconds."""
    time_parts = re.split(r"[\s:.\-]+", time_str.strip())
    time_parts = [int(part) for part in time_parts]

    if len(time_parts) == 1:
        return time_parts[0], 0, 0  # Only hours provided
    elif len(time_parts) == 2:
        return time_parts[0], time_parts[1], 0  # Hours, minutes
    elif len(time_parts) == 3:
        return time_parts[0], time_parts[1], time_parts[2]  # Hours, minutes, seconds
    else:
        raise ValueError("Invalid time format. Use HH:MM, HH-MM, HH MM SS, etc.")

def time_to_decimal(hours: int, minutes: int, seconds: int = 0):
    """Converts hours, minutes, and optionally seconds to decimal hours."""
    return round(hours + minutes / 60 + seconds / 3600, 4)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Totem - A multipurpose utility tool")
    subparsers = parser.add_subparsers(dest="command")

    # Time Conversion Command (t)
    time_parser = subparsers.add_parser("t", help="Convert time into decimal hours")
    time_parser.add_argument("time", type=str, help="Time in any format (HH:MM, HH-MM, HH.MM, HH MM SS)")

    # Calculator Command (c)
    calc_parser = subparsers.add_parser("c", help="Evaluate a mathematical expression")
    calc_parser.add_argument("expression", nargs="+", help="Mathematical expression (e.g., 2 + 3 * (2 + 22)/2)")

    args = parser.parse_args()

    if args.command == "t":
        try:
            hours, minutes, seconds = parse_time_input(args.time)
            print(time_to_decimal(hours, minutes, seconds))
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "c":
        try:
            # Fix: Properly join arguments while preserving operators and spaces
            expression = " ".join(args.expression)
            result = calculate(expression)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")

    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
