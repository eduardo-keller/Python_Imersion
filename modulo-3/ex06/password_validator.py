import sys

def is_valid_password(password: str) -> bool:
        if not min_8(password):
                return False
        if not max_16(password):
                return False
        if not upper(password):
                return False
        if not lower(password):
                return False
        if not has_digit(password):
                return False
        if not has_special(password):
                return False
        if not no_spaces(password):
                return False
        return True
        
def min_8(value: str) -> bool:
        """check min 8 chars"""
        if len(value) < 8:
                return False
        return True

def max_16(value: str) -> bool:
        """check max 16 chars"""
        if len(value) > 16:
                return False
        return True

def upper(v: str) -> bool:
        """check one upper"""
        if any(ch.isupper() for ch in v):
                return True
        else:
                return False

def lower(v: str) -> bool:
        """check one lower"""
        if any(ch.islower() for ch in v):
                return True
        else:
                return False 

def has_digit(v: str) -> bool:
        """check one digit"""
        if any(ch.isdigit() for ch in v):
                return True
        else:
                return False

def has_special(s: str) -> bool:
        """check one special"""
        return any(not ch.isalnum() for ch in s)

def no_spaces(s: str) -> bool:
        """check no blank"""
        return not any(ch.isspace() for ch in s)


if __name__ == "__main__":
        print (is_valid_password(sys.argv[1]))