import sys

def convert_to_float() -> int:
    """convert to float"""
    try:
        if len(sys.argv) != 2:
            raise IndexError
        print(float(sys.argv[1]))
        return 0
    except ValueError:
        print("conversion impossible")
        return 1
    except IndexError:
        print("Input one and only one argument")
        return 1


if __name__=="__main__":
    sys.exit(convert_to_float())