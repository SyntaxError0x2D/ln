#defining the natrual logarithm trough 1/x with integral area properties

iterLim = 2000

def ln(n : float):
    if n <= 0:
        if n == 0: raise(Exception("ln(0) is undefined"))
        else: raise(Exception("ln(x), x<0 is undefined"))

    h = (n-1)/iterLim ; s = 0
    for i in range(iterLim):
        s+=h*(1/(1+h*i))
    return(s)
