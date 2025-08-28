import cowsay

def greeting(name : str = "bob") -> None:
    '''receives a name and prints a greeting'''
    cowsay.cow(f"Hello {name}!")