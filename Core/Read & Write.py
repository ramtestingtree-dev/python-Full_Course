def file_operations():
    try:
        # Write
        with open("sample.txt", "w") as file:
            file.write("Hello Python\n")

        # Append
        with open("sample.txt", "a") as file:
            file.write("Welcome to File Handling\n")

        # Read
        with open("sample.txt", "r") as file:
            print(file.read())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Operation completed")

file_operations()