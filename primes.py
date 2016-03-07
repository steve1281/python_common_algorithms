from copy import deepcopy


class StrategyPrime():
    """ template for strategy.
        All strategies should descend from and override the the method n.
    """
    def primes(self,n):
        raise Exception("StrategyPrime class should not be used directly. Subclass and override primes method.")

class LessSquarePrimes(StrategyPrime):
    """ simple brute force example, testing up to sqr root """
    def _is_prime(self, n):
        """brute force"""
        if n < 2:
            return False
        max_test = int(n**0.5) + 1

        for x in xrange(2, max_test):
            if n % x == 0:
                return False
        return True

    def primes(self, n):
        """
        :param n: number of primes to return
        :return: list of primes
        """
        """Loop through and check for first n primes"""
        cnt=0
        x = []
        i = 2
        while 1:
            if self._is_prime(i):
                x.append(i)
                cnt += 1
                if cnt >= n:
                    break
            i += 1
        return x


class SievePrimes(StrategyPrime):
    def _gen_primes(self):
        """ Generate an infinite sequence of prime numbers.
            (uses E-sieve)
        """
        D = {}
        q = 2

        while True:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1

    def primes(self, n):
        """
        :param n: number of primes to return
        :return: first n primes
        """
        p = self._gen_primes()
        return [next(p) for _ in range(n)]



class PrimeRunner:
    """ Class to store ans execute the selected prime strategy """
    def __init__(self, strategy):
        assert issubclass(strategy, StrategyPrime)
        self.strategy = strategy()

    def primes(self, n):
        return self.strategy.primes(n)


def main():
    n = int(raw_input("Enter max number to test> "))
    print PrimeRunner(SievePrimes).primes(n)
    print PrimeRunner(LessSquarePrimes).primes(n)
    #print PrimeRunner(StrategyPrime).primes(n)
    #print PrimeRunner(None).primes(n)

if __name__ == "__main__":
    main()