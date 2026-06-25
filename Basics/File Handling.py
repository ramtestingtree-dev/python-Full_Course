# Example: File Handling with Exception Handling

def read_file(filename):
    try:
        # Try opening the file
        with open(filename, "r") as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        print("File handling operation complete.")

# Test cases
read_file("example.txt")       # Normal case (if file exists)
read_file("missing.txt")       # FileNotFoundError
read_file("/root/secret.txt")  # PermissionError (on restricted files)
