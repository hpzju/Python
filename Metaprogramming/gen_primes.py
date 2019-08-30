def gen_primes():
    primes = set()
    candidate = 2
    while True:
        if all(candidate % prime != 0 for prime in primes):
            primes.add(candidate)
            yield candidate
        candidate += 1


def gen_primesN(num):
    primes = set()
    candidate = 2
    while candidate < num:
        if all(candidate % prime != 0 for prime in primes):
            primes.add(candidate)
            yield candidate
        candidate += 1


if __name__ == '__main__':
    for i in gen_primes():
        print(i)
        if i >= 100:
            break
