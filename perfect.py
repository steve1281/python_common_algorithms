

def perf1(n):
    sum = 0
    for i in xrange(1, n):
        if n % i == 0:
            sum += i
    return sum == n

perf2 = lambda n: n == sum(i for i in xrange(1, n) if n % i == 0)

def main():


    #print perf2(6)
    #print perf1(6)

    for i in xrange(1, 10000):
        if perf1(i):
            print i

    for i in xrange(1, 10000):
        if perf2(i):
            print i


if __name__ == "__main__":
    main()
