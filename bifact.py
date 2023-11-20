#defining the natrual logarithm trough the bisect theorem, and the fact (coined by blackpenredpen)

largeLim = 2<<32
ln2 = 0.69314718055994530942
iterLim = 1000

def exp(n):
    return( (1+n/largeLim)**largeLim)

def ln(n):
    a = (int(n).bit_length()-1 )* ln2 -1
    b = a+1

    for _ in range(iterLim):
        m = (a+b)/2
        t = exp(m)-n
        if t == 0: return(m)
        elif t < 0: a = m
        else: b = m

    return(m)
