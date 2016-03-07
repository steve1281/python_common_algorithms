__author__ = 'Steve'



def fib1(n):
    """ Return first n fib numbers, simple approach """
    if n ==1 or n==2 :
        return 1
    return fib1(n-1) + fib1(n-2)


def fib2(n):
    """slightly more compact approach """
    return 1 if n <= 2 else fib2(n-1) + fib2(n-2)


def fib3():
    """ Generate infinite number of fib values
    """
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


def main():

    while 1:
        n = int(raw_input("enter number of fibs to generate> "))
        s = int(raw_input("Enter testcase> "))
        if s == 0:
            break
        if s == 1:
            x = [fib1(x) for x in range(1, n+1)]
        elif s ==2:
            x = [fib2(x) for x in range(1, n+1)]
        else:
            b = fib3()
            x = [next(b) for _ in range(1, n+1)]
        print x, "\n\n"


if __name__ == "__main__":
    main()