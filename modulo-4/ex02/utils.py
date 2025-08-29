
def format_cents(cents: int) -> str:
    sign: str = "[+]" if cents >= 0 else "[-]"
    reais = abs(cents) / 100
    print(f"{sign} {reais}")
    


if __name__=="__main__":
    format_cents(100_01)
