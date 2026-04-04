# Print Formatting - All print() parameters and formatting options

# Basic print
print("Hello, World!")

# end parameter - change line ending
print("Hello", end=" ")
print("World")

# sep parameter - change separator between arguments
print("A", "B", "C", sep=", ")
print("2025", "01", "15", sep="-")

# Multiple arguments
print("Name:", "Python", "Version:", 3.12)

# f-string formatting
name = "Python"
version = 3.12
print(f"Language: {name}, Version: {version}")

# Number formatting
pi = 3.141592653589793
print(f"Pi (2 decimal): {pi:.2f}")
print(f"Pi (4 decimal): {pi:.4f}")

# Integer formatting
num = 1000000
print(f"Formatted number: {num:,}")

# Padding and alignment
text = "Hello"
print(f"|{text:<20}|")  # Left align
print(f"|{text:>20}|")  # Right align
print(f"|{text:^20}|")  # Center align
