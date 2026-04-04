import textwrap
from datetime import datetime


def fstring_tricks_demo():
    # 1. Embedding expressions:
    a, b = 5, 10
    print(f"Sum of {a} and {b} is {a + b}.")

    # 2. Self-documenting expressions (debugging):
    name = "Alice"
    value = 42
    print(f"{name=}, {value=}")

    # 3. Conversion flags:
    text = "Hello"
    print(f"Using str: {text!s}, using repr: {text!r}")

    # 4. Format specification (number formatting and alignment):
    number = 1234567.89123
    print(f"Formatted number with commas and 2 decimals: {number:,.2f}")
    print(f"{'Centered':_^20} | {'Left':=<20} | {'Right':#>20}".strip())

    # 5. Dynamic format specifiers:
    value = 3.14159
    width = 10
    precision = 3
    print(f"Dynamic formatting: {value:{width}.{precision}f}")

    # 6. Nested f-string for dynamic format:
    fmt = f".{precision}f"  # This builds the format string dynamically.
    print(f"Using nested format specifier: {value:{fmt}}")

    # 7. Calling functions and complex expressions:
    def greet(n):
        return n.upper()

    print(f"Greeting using a function: {greet(name)}")
    print(f"Squares of numbers 0-4: {[x**2 for x in range(5)]}")

    # 8. Multi-line f-string:
    info = f"""
    User Information:
      Name: {name}
      Age: {value}  # (using 'value' just as an example)
    """
    print(info)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.name}"
        elif format_spec == "detailed":
            return f"{self.name} is {self.age} years old."
        return str(self)


def additional_f_string_tricks():
    # 1. Automatic concatenation of adjacent f-strings.
    name = "Alice"
    greeting = f"Hello, {name}!"
    print(greeting)  # Output: Hello, Alice!

    # 2. Raw f-string usage (helpful for regex, paths, etc.).
    pattern = r"\d+"
    regex_info = rf"Regex pattern: {pattern}"
    print(regex_info)

    # 3. Inline conditional expressions.
    value = 42
    status = f"Value is {'positive' if value > 0 else 'non-positive'}."
    print(status)

    # 4. Dynamic format specifiers using nested f-strings.
    number = 3.14159265
    precision = 4
    formatted = f"Number: {number:{'.' + str(precision) + 'f'}}"
    print(formatted)

    # 5. Custom object formatting via __format__.
    person = Person("Bob", 25)
    print(f"Person (short): {person:short}")
    print(f"Person (detailed): {person:detailed}")

    # 6. Multi-line f-string with dedenting.
    multi_line = f"""
        This is a multi-line string.
        It preserves code indentation, but dedent will fix that.
        The current time is {datetime.now():%H:%M:%S}.
    """
    print(textwrap.dedent(multi_line))


if __name__ == "__main__":
    fstring_tricks_demo()
    additional_f_string_tricks()
