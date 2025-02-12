import re

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
