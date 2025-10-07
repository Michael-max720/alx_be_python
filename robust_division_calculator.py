def safe_divide(numerator,denominator):
    try:
        num=float(numerator)
        den=float(denominator)
    except ValueError:
        return "Error: Both values must be numeric."
    try:
        result= num/den
        return result
    except ZeroDivisionError:
        return "Error: You can not divide a number by zero."
    
    
