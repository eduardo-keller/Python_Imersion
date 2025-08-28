
def format_cents(cents: int) -> str:
    if cents < 0:
        sign: str = "[-]"
        cents = cents * -1
    else:
        sign: str = "[+]"
    cents = cents / 100
    

