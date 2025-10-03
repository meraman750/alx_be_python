
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        try:
            ans = num / den
            return f"Result: f{ans}"
        except ZeroDivisionError:
            return "Error division by zero"
    except ValueError:
        return "Error invalid input"