#defining the natrual logarithm trough taylor series expansion of exp and then using newton iteration for the inv function.
#factorial divisors could be stored seperately
#initial guess from floor log_2+1

expLim = 20
lnLim = 50

def exp(n):
    fact = 1 ; s = 0 ; ni = 1
    for i in range(expLim):
        s += ni / fact
        fact *= i+1 
        ni *= n
    
    return(s)

def ln(n):
    if n <= 0:
        if n == 0: raise(Exception("ln(0) is undefined"))
        else: raise(Exception("ln(x), x<0 is undefined"))

    g = int(n).bit_length() 
    expn = exp(n)
    for _ in range(lnLim):
        g -= (expn-n)/expn
        expn = exp(g)
    return(g)

