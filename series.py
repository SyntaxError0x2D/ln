# cool series for integers inputs for ln(x), can be extended to decimals with a simple multiplication trick

ln2 = 0.69314718055994530942

def lnN(n : int, iters = 10000) -> float:
    s = 0
    for k in range(1, iters):
        s += sum([1/(n*k-j) for j in range(1, n)])
        s -= (n-1)/(n*k)
    return(s)

def ln(n : float, iters = 10000, ln2b = 10) -> float:
    if n <= 0:
        if n == 0: raise(Exception("ln(0) is undefined"))
        else: raise(Exception("ln(x), x<0 is undefined"))
    if n-int(n) < 0.00000001:
        return(lnN(int(n)))
    return( lnN( int((1<<ln2b)*n) ) -ln2b*ln2)
