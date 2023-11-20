#defining the natrual logarithm trough a log2 approximation
#do note this means this will just be an approximation, and only works for ints

ln2 = 0.69314718055994530942 #precomputed constant

def binLeng(bin : int):
    size = bin.__sizeof__() - 24
    maxE = (size >> 1) * 15 # same as size // 4 * 30
    
    for val in reversed(range(maxE)): 
        if bin & (1 << val): return(val+1)

def log2a(n : int):
    l = binLeng(n) #n.bit_length()
    if n == 0: return(0)
    r = (n & (1 << (l-1))-1 ) / (1<<l) *2 
    return( float(l - 1) + r)

def ln(n):
    if n <= 0:
        if n == 0: raise(Exception("ln(0) is undefined"))
        else: raise(Exception("ln(x), x<0 is undefined"))
        
    return(log2a(n) * ln2)
