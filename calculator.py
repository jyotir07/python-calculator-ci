
def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def power (a, b):
    return a ** b

if __name__ == "__main__":
    print("Sum:", add(2, 3))
    print("Difference:", subtract(5, 3))
    print("Product:", multiply(2, 3))
    print("Quotient:", divide(6, 3))
    print("Power:", power(2, 3))