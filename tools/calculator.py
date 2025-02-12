def calculate(operator: str, numbers: list):
    """Performs a calculation on a list of numbers using the given operator."""
    if not numbers:
        raise ValueError("No numbers provided for calculation.")

    result = numbers[0]

    if operator == "+":
        result = sum(numbers)
    elif operator == "-":
        for num in numbers[1:]:
            result -= num
    elif operator == "*":
        for num in numbers[1:]:
            result *= num
    elif operator == "/":
        for num in numbers[1:]:
            if num == 0:
                raise ValueError("Division by zero is not allowed.")
            result /= num
    elif operator == "^":
        for num in numbers[1:]:
            result **= num
    else:
        raise ValueError("Invalid operator. Use +, -, *, /, or ^.")

    return result
