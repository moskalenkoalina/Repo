def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


def is_prime_number(n, is_prime):
    return n < len(is_prime) and is_prime[n]


def reverse_number(n):
    return int(str(n)[::-1])


def find_kth_happy_prime(K):
    limit = 10 ** 6
    is_prime = sieve(limit)
    happy_primes = []

    for p in range(2, limit + 1):
        if is_prime[p]:
            p_reversed = reverse_number(p)
            if p != p_reversed and is_prime_number(p_reversed, is_prime):
                happy_primes.append(p)
                if len(happy_primes) == K:
                    return p

    return -1


K = int(input())
print(find_kth_happy_prime(K))