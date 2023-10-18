#!/usr/bin/python3
"""
Calculate the fewest number of copy and paste operations needed to achieve 'n' 'H' characters in a text file.

:param n: The desired number of 'H' characters to achieve in the file.
:type n: int
:return: The minimum number of copy and paste operations required to achieve 'n' 'H' characters. If 'n' is impossible to achieve, return 0.
:rtype: int
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly 'n' H characters in the file.

    :param n: The desired number of 'H' characters in the file.
    :type n: int
    :return: The minimum number of operations required to achieve 'n' 'H' characters.
    :rtype: int

    If 'n' is impossible to achieve, return 0.
    """

    if n <= 1:
        return 0  # It's impossible to have fewer than 2 'H' characters.

    # Initialize an array to store the minimum operations required for each number of 'H' characters.
    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        # Initialize operations[i] to a maximum value initially.
        operations[i] = float('inf')

        # Try to find a factor j such that we can copy-paste 'j' characters to reach 'i'.
        for j in range(1, i):
            if i % j == 0:
                # Copy 'j' characters and then paste (i // j - 1) times.
                operations[i] = min(operations[i], operations[j] + (i // j))

    return operations[n]

# Example usage:
n = 9
result = minOperations(n)
print(f"Minimum operations to achieve {n} 'H' characters: {result}")
