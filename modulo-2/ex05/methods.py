import sys


def main() -> int:
    """receives str and displays if its highcase, numeric, ascii and alphanumeric"""
    s = sys.argv[1]
    if len(sys.argv) != 2:
        print("wrong number of args")
        return 1
    print(f"São maíusculas? {s.isupper()}")
    print(f"É númerico? {s.isnumeric()}")
    print(f"É ascii? {s.isascii()}")
    print(f"É alfanumérico? {s.isalnum()}")
    return 0


if __name__=="__main__":
    SystemExit(main())