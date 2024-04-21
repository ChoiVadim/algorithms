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


class MatrixRecurrence:
    # Transformation matrix for the recurrence relation
    # Including the constant term in the matrix
    Q = [
        [1, 1, 1, 1],  # Corresponds to x_n = x_{n-1} + x_{n-2} + x_{n-3} + 1
        [1, 0, 0, 0],  # Corresponds to x_{n-1}
        [0, 1, 0, 0],  # Corresponds to x_{n-2}
        [0, 0, 0, 1],
    ]  # Accommodates the constant term

    def __init__(self):
        self.__memo = {}

    def __multiply_matrices(self, M1, M2):
        """Matrix multiplication (expects 4x4 matrices)."""
        result = [
            [sum(a * b for a, b in zip(M1_row, M2_col)) for M2_col in zip(*M2)]
            for M1_row in M1
        ]
        return result

    def __get_matrix_power(self, M, p):
        """Matrix exponentiation (expects p to be a power of two)."""
        if p == 1:
            return M
        if p in self.__memo:
            return self.__memo[p]
        K = self.__get_matrix_power(M, p // 2)
        R = self.__multiply_matrices(K, K)
        self.__memo[p] = R
        return R

    def get_number(self, n):
        """Get the nth term of the recurrence relation."""
        if n < 3:
            return 1  # Based on the initial conditions x_0 = x_1 = x_2 = 1
        # Adjusting the powers to account for the base case starting at n = 3
        powers = [
            int(pow(2, b)) for (b, d) in enumerate(reversed(bin(n - 3)[2:])) if d == "1"
        ]

        matrices = [self.__get_matrix_power(MatrixRecurrence.Q, p) for p in powers]
        # Initialize the vector for the state corresponding to n = 3
        vector = [
            1,
            1,
            1,
            1,
        ]  # This represents the initial state x_3, x_2, x_1, and the constant term

        for M in matrices:
            vector = [sum(a * b for a, b in zip(M_row, vector)) for M_row in M]

        # The first element of the resulting vector is x_n
        return vector[0]
