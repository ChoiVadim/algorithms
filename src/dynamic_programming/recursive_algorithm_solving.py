def recursive_algo(n):
    # Time Complexity: O(3^n) Each call generates three additional calls.
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return recursive_algo(n - 1) + recursive_algo(n - 2) + recursive_algo(n - 3) + 1


def iterative_algo(n):
    # Time Complexity: O(n) This algorithm performs a
    # single loop from 3 to n, calculating each x[i] once.

    if n <= 2:
        return 1

    x = [1, 1, 1] + [0] * (n - 2)

    for i in range(3, n + 1):
        x[i] = x[i - 1] + x[i - 2] + x[i - 3] + 1

    return x[n]


def memoized_recursive_algo(n, memo):
    # Time Complexity: O(n) Each x[i] is computed once
    # and stored for future reference.
    if n in memo:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = (
            memoized_recursive_algo(n - 1, memo)
            + memoized_recursive_algo(n - 2, memo)
            + memoized_recursive_algo(n - 3, memo)
            + 1
        )
    return memo[n]
