def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling errors like division by zero and non-numeric inputs.
    """
    try:
        # Try to convert both inputs to numbers
        num = float(numerator)
        den = float(denominator)

        # Try to divide
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # This happens when denominator is 0
        return "Error: Cannot divide by zero."

    except ValueError:
        # This happens if someone types letters instead of numbers
        return "Error: Please enter numeric values only."
