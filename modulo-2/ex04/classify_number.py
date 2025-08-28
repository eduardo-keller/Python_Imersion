import sys

def is_positive(num : int) -> bool:
    """checks if a number is positive"""
    return (num > 0)

if __name__=="__main__":
    print(is_positive(int(sys.argv[1])))
