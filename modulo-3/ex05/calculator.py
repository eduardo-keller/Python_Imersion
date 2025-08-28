from typing import Any

def add(num1: int, num2: int) -> int:
    """add"""
    return (num1 + num2)

def subtract(num1: int, num2: int) -> int:
    """subtract"""
    return (num1 - num2)

def multiply(num1: int, num2: int) -> int:
    """multiply"""
    return (num1 * num2)

def divide(num1: int, num2: int) -> float:
    """divide"""
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return(num1 / num2)

def power(base: int, exponent: int) -> Any:
    """power"""
    return(base**exponent)
    


