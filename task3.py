def fact(n):
    if n == 0:
        return 1
    else:
        summ = 1
        for i in range(1, n + 1):
            summ *= i
        return summ

def step(n, ro):
    return ((ro ** n) / fact(n))

def pi_zero (n, m, ro):
    result = (1-ro)/(1-(ro**(m+2)))
    return result

def pi_otk (n, m, ro):
    return (pi_zero(n, m, ro)*(ro**(m+1)))

def main():
    lambda_day = 1
    mu = 2
    m = 12
    n = 7

    ro = round(lambda_day/mu, 3)
    print ("pi_otk = ", pi_otk(n, m, ro))
    t_obs = 1/mu

if __name__ == "__main__":
    main()