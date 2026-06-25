# Example: Exception Handling in Python

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please provide numbers only.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        print("Execution of divide_numbers is complete.")

# Test cases
divide_numbers(10, 2)   # Normal case
divide_numbers(10, 0)   # ZeroDivisionError
divide_numbers(10, "a") # TypeError
