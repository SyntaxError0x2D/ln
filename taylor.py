#defining the natrual logarithm trough a taylor series expansion, this is the worst algorithm of them all

def ln(n):
    if n <= 0:
        if n == 0: raise(Exception("ln(0) is undefined"))
        else: raise(Exception("ln(x), x<0 is undefined"))

    s = 0 ; sgn = 1 ; ni = n-1
    for i in range(1, 1000):
        s += sgn*(1/i)*ni
        sgn *= -1 ; ni *= ni

    return(s)

