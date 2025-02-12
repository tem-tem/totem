#!/usr/bin/env python3
import argparse
import re

def parse_time_input(time_str: str):
    """Parses time input with various separators and returns hours, minutes, and optionally seconds."""
    # Remove all non-numeric characters except spaces
    time_parts = re.split(r"[\s:.\-]+", time_str.strip())

    # Convert to integers
    time_parts = [int(part) for part in time_parts]

    # Ensure valid length (1-3 parts)
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

def main():
    parser = argparse.ArgumentParser(description="Totem - A multipurpose utility tool")
    subparsers = parser.add_subparsers(dest="command")

    # Time Conversion Command (t)
    time_parser = subparsers.add_parser("t", help="Convert time into decimal hours")
    time_parser.add_argument("time", type=str, help="Time in any format (HH:MM, HH-MM, HH.MM, HH MM SS)")

    args = parser.parse_args()

    if args.command == "t":
        try:
            hours, minutes, seconds = parse_time_input(args.time)
            print(time_to_decimal(hours, minutes, seconds))
        except ValueError as e:
            print(f"Error: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
