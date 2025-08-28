import sys


def read_file(filename: str) -> int:
    """reads and prints the content of a file in the terminal"""
    try:
        with open(filename, "r") as file:
            print(file.read())
            return 0
    except PermissionError:
        print("Error: permission error")
        return 1
    except FileNotFoundError:
        print("Error: file not found")
        return 1
    except IsADirectoryError:
        print("Error: is a directory")
        return 1
    except UnicodeDecodeError:
        print("Error: unicode decode error")
        return 1
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python3 read_file.py <file>")
    else:
        sys.exit(read_file(sys.argv[1]))
