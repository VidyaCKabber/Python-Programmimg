def check_even_odd(num):
    return "Even" if str(num)[-1] in '02468' else "Odd"

# Example usage:
print(check_even_odd(12))  # Even
print(check_even_odd(7))   # Odd
