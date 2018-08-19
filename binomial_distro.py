
def factorial(x):
    if x==0 or x==1:
        return 1

    sum = 1
    for i in range(2, x+1):
        sum *= i

    return sum


def choose(a, b):

    return factorial(a) / (factorial(b) * factorial(a-b))


def f(x, n, p):
    """probability of x successes in a binomial distro"""
    return choose(n, x) * (p**x) * ((1-p)**(n-x))


def F_sum(start, end, n, p):
    """The sum of all probabilities f(x) where x in [start, end]"""

    sum = 0
    for x in range(start, end+1):
        sum += f(x, n, p)

    return sum

