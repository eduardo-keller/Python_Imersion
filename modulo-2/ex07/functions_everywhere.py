import sys

def shrink(s : str) -> str:
    """shrink str to 8 characters"""
    return(s[:8])


def enlarge(s : str) -> str:
    """enlarge str with 'z' until 8 characters"""
    return (s.ljust(8, 'Z'))

def str_manager(lst : list[str]) -> int:
    """manage strs"""
    if len(lst) == 1:
        print("None")
    for arg in lst[1:]:
        if len(arg) > 8:
            print(shrink(arg))
        if len(arg) == 8:
            print(arg)
        if len(arg) < 8:
            print(enlarge(arg))
    return (0)


if __name__ == "__main__":
    SystemExit(str_manager(sys.argv))