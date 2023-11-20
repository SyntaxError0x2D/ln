#defining ln(x) trough the divided difference method, and approximate an infinidecimal.

lnLim = 15

sqrtLim = 50
sqrt2 = 1.4142135623730950488  #precomputed constant

def sqrt(n):
    #approx
    odd = 0
    a = int(n).bit_length()-1
    if a & 1: odd = 1
    a >>= 1 #div by 2 / cuts out odd
    lw = 2**a #lowerbound
    up = lw* [sqrt2, 2][odd] #syntax shenanigans

    for _ in range(sqrtLim):
        m = (up+lw)/2
        t = m**2 -n
        if t == 0: return(m)
        elif t < 0: lw = m
        else: up = m
    return(m)


def ln(n):
    if n <= 0:
        if n == 0: raise(Exception("ln(0) is undefined"))
        else: raise(Exception("ln(x), x<0 is undefined"))
    
    for _ in range(lnLim): n = sqrt(n)
    d = 1/2**lnLim
    return((n-1)/d)