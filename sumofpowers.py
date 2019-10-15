def powers(n):
    return [1<<x for x,bit in enumerate(bin(n)[:1:-1]) if bit == "1"]