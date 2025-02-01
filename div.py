class PeriodicNumber:
    def __init__(self, sign, integer, non_repeating=None, repeating=None):
        self.sign = sign
        self.integer = integer
        self.non_repeating = non_repeating
        self.repeating = repeating

    def __str__(self):
        string = f"{self.sign}{self.integer}"
        if self.non_repeating:
            string += f".{self.non_repeating}"
        if self.repeating:
            string += f"({self.repeating})"
        return string


# Division with Period
def divide_with_period(a, b):
    c = []
    seen_remainders = {}

    # Handle division by zero
    if b == 0:
        raise ValueError("Division by zero")

    # Determine the sign of the result
    sign = "-" if (a * b) < 0 else ""
    a, b = abs(a), abs(b)

    # Get integer part and initial remainder
    integer = a // b
    r = (a % b) * 10

    # Handle exact division case
    if r == 0:
        return PeriodicNumber(sign, integer)

    # Calculate decimal expansion
    while r != 0:
        if r in seen_remainders:
            repeat_start = seen_remainders[r]
            non_repeating = "".join(map(str, c[:repeat_start]))
            repeating = "".join(map(str, c[repeat_start:]))
            return PeriodicNumber(sign, integer, non_repeating, repeating)

        seen_remainders[r] = len(c)
        digit = r // b
        c.append(digit)
        r = (r % b) * 10
    else:
        # If no repetition found
        non_repeating = "".join(map(str, c))
        return PeriodicNumber(sign, integer, non_repeating)


if __name__ == "__main__":
    while True:
        try:
            print(
                "Enter two integers a and b to divide a by b (or type 'exit' to quit):"
            )
            user_input = input().strip()
            if user_input.lower() in ("exit", "quit", "q", "bye"):
                break
            a, b = map(int, user_input.split())
            print(divide_with_period(a, b))
        except ValueError:
            print("Invalid input. Please enter two integers.")
