#defining the natrual logarithm trough 1/x with integral area properties
#needs case for when n < 1 with some stuff flipped

iterLim = 2000

def ln(n : float):
    if n <= 0:
        if n == 0: raise(Exception("ln(0) is undefined"))
        else: raise(Exception("ln(x), x<0 is undefined"))

    elif n > 1:
        h = (n-1)/iterLim ; s = 0
        for i in range(iterLim):
            s+=h*(1/(1+h*i))
        return(s)
    
    elif n < 1:
        h = (1-n)/iterLim ; s = 0
        for i in range(iterLim):
            s-=h*(1/(n+h*i))
        return(s)
    
