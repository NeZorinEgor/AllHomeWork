for n in range(10000):
    s = sum(i for i in range(1, n) if n % i == 0)
    if s > n and sum(i for i in range(1, s) if s % i == 0) == n:
        print(n, s)
