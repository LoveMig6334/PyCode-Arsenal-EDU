"""
Python Memory Identity and Equality Demonstration
================================================
This script demonstrates the difference between:
- Identity comparison (is) - checks if two variables reference the same object in memory
- Equality comparison (==) - checks if two variables have the same value
"""

# Part 1: Creating two lists with the same values but different identities
# --------------------------------------------------------------------- #
x: list = [
    1,
    2,
    3,
    4,
]  # First list with values 1-4
y: list = [
    1,
    2,
    3,
    4,
]  # Second list with identical values but different memory location

# Compare identity and display memory addresses
print("\n--- Initial Comparison ---")
print(f"Identity comparison (x is y): {x is y}")
print(f"Memory address of x: {hex(id(x))}")
print(f"Memory address of y: {hex(id(y))}")
print(f"Equality comparison (x == y): {x == y}")
print("Explanation: The lists contain the same values so they're equal (==),")
print(
    "but they are different objects in memory so their identity (is) comparison is False."
)

# Part 2: Making y reference the same object as x
# --------------------------------------------------------------------- #
print("\n--- After Assignment y = x ---")
y = x  # Now y references the exact same list object as x

# Compare identity and display memory addresses again
print(f"Identity comparison (x is y): {x is y}")
print(f"Memory address of x: {hex(id(x))}")
print(f"Memory address of y: {hex(id(y))}")
print(f"Equality comparison (x == y): {x == y}")
print("Explanation: Now both variables point to the exact same object in memory,")
print("so both identity (is) and equality (==) comparisons return True.")

# Part 3: Demonstrating how changes affect both variables when they share identity
# --------------------------------------------------------------------- #
print("\n--- Demonstrating Shared References ---")
print(f"Original x: {x}")
print(f"Original y: {y}")

x.append(5)  # Modify x by adding a new element
print("\nAfter x.append(5):")
print(f"Modified x: {x}")
print(f"y is also modified: {y}")
print("This happens because x and y reference the same object in memory.")

# Part 4: Immutable vs Mutable types example
# --------------------------------------------------------------------- #
print("\n--- Immutable vs Mutable Types ---")
a = "hello"
b = "hello"
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # Often True for strings due to string interning
print(f"a == b: {a == b}")
print("For immutable types like strings, Python may optimize by reusing objects.")

c = 42
d = 42
print(f"\nc = {d}, d = {d}")
print(f"c is d: {c is d}")  # Often True for small integers due to integer caching
print(f"c == d: {c == d}")
print("Python caches small integers (-5 to 256) for efficiency.")
