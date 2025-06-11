def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denomnator = float(denominator)
        result = numerator/denominator
    except ValueError:
        return f"Error: Please enter numeric values only"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero"
    else:
        return f"The result of the division is {result}"
