#!/usr/bin/python3
'''
function to solve a competitive game
'''


def isWinner(x, nums):
    """
    Determine the winner of a game played between Maria and Ben based on
    the rules of selecting and removing and their multiples from a range
    of integers.

    Args:
    x (int): The number of rounds played
    nums (list of int): List where each element represents the maximu
    number (n) in the range for a round.

    Returns:
    str or None: The name of the player who wins the most rounds ("Maria"
    or "Ben"), or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)

    # Precompute primes up to max_n using the Sieve of Eratosthenes
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 or 1 arenot primes

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute the number of primes up to each other
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[1] else 0)

    # Simulate the games and count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
