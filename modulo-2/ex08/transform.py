import sys

def square_even_numbers(lst : list[int]) -> list[int]:
    """takes a list of ints and returns a list of the even numbers raised to the power of two"""
    sqr_even : list[int] = [num**2 for num in lst if num % 2 == 0]
    return (sqr_even)

if __name__ == "__main__":
    numbers : list[int] =  list(map(int, sys.argv[1].split()))
    print(f"Squared evens: {square_even_numbers(numbers)}")
    