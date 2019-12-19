# 204-Count_Primes.py

# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:
    def countPrimes(self, n: int) -> int:

        # I'm sure there are better ways to do this but let's start here
        # Loop through all of the potential candidates starting with 2
        # for each potential candidate check whether the modulo of it and
        # any of the previous primes is 0, then add it as a prime if none are

        # Time complexity: O(N * k) since we hit each number (N) once
        # and check it against each prime (k)

        # Space complexity O(k) since we only store the primes and get
        # the digits of n in a generator


        # # Initialize for the first few cases.
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 0
        # elif n == 2:
        #     return 0
        # elif n == 3:
        #     return 1

        # primes = [2, 3]

        # # loop through the rest of the digits checking for prime-ness
        # for i in range(4, n):

        #     # see if i is divisible by any primes
        #     for prime in primes:
        #         # if so, break out of this loop and move onto the next i
        #         if i % prime == 0:
        #             break

        #     # make sure to not append if the number is not prime
        #     if i % prime == 0:
        #         continue

        #     primes.append(i)

        # return len(primes)

        # Let's try using the Sieve of Eratosthenes

        # initialize array of 1's through n, change index 0 and 1 to 0
        # in this array, if the index is 1 then index + 1 is prime

        # # Initialize for the first few cases.
        if n == 0:
            return 0
        elif n == 1:
            return 0
        # elif n == 2:
        #     return 0
        # elif n == 3:
        #     return 1

        primes = [1] * (n + 1)

        i = 2
        while (i * i <= n):

            # check all the primes
            if primes[i] == 1:

                # change all multiples to false
                for j in range(i * 2, n + 1, i):
                    primes[j] = 0

            i += 1
        primes[0] = 0
        primes[1] = 0

        # Chop off the last item. We had to add it to index correctly above.
        primes = primes[:-1]

        # Return the number of primes (sum all the 1's)
        return sum(primes)

        # Hmm my answer above takes a while but for 499979 gets the correct
        # answer of 41537. The faster one gives 41538 incorrectly
        # It was because of the last item not getting checked.
        # I'm not sure how to resolve this well, I just chopped it off for now.




if __name__ == '__main__':
    s = Solution()

    print("Example 1 input: 10 output should be 4:", s.countPrimes(10))
    print("Example 2 input: 0 output should be 0:", s.countPrimes(0))
    print(
        "Example 3 input: 499979 output should be 41537:",
        s.countPrimes(499979)
    )
    print("Example 4 input: 30 output should be 10:", s.countPrimes(30))
    print("Example 5 input: 100 output should be 25:", s.countPrimes(100))
