#!/usr/bin/env python3
import argparse
import sys
from tools.time_converter import parse_time_input, time_to_decimal
from tools.calculator import calculate

def main():
    parser = argparse.ArgumentParser(description="Totem - A multipurpose utility tool")
    subparsers = parser.add_subparsers(dest="command")

    # Time Conversion Command (t)
    time_parser = subparsers.add_parser("t", help="Convert time into decimal hours")
    time_parser.add_argument("time", type=str, help="Time in any format (HH:MM, HH-MM, HH.MM, HH MM SS)")

    # Calculator Command (c)
    calc_parser = subparsers.add_parser("c", help="Perform basic arithmetic operations")
    calc_parser.add_argument("operator", type=str, choices=["+", "-", "*", "/", "^"], help="Arithmetic operator")
    calc_parser.add_argument("numbers", type=float, nargs="+", help="Numbers to perform operation on")

    args = parser.parse_args()

    if args.command == "t":
        try:
            hours, minutes, seconds = parse_time_input(args.time)
            print(time_to_decimal(hours, minutes, seconds))
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "c":
        try:
            result = calculate(args.operator, args.numbers)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")

    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()