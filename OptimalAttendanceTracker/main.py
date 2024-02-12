from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10**6)


class GraduationCeremony:
    MISS_THRESHOLD = 4
    def __init__(self, n, m=MISS_THRESHOLD):
        # n: number of academic days
        # m: cannot miss m or more classes consecutevly
        if n < m or n < 0 or m < 0:
            raise ValueError("Invalid Inputs")

        self.n = n
        self.m = m


    def solve(self):
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m)
        Dynamic Programing Tabulation with Space Optimization
        """

        n, m = self.n, self.m
        dp = [1] * (m + 1)
        dp[m] = 0

        for i in range(1, n + 1):
            temp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            temp, dp = dp, temp

        x1 = dp[0]  # total number of valid way to attend classes
        x2 = temp[1]  # total number of way to miss last day

        return f"{x2}/{x1}"

    def run(self):
        print('=' * 10, ' n:', n, ', miss_threshold:', self.m, ' ', '=' * 10)
        print('Solution:', self.solve())
        print('=' * 40,)


if __name__ == "__main__":
    inputs = [5, 10, 100]
    for n in inputs:
        obj = GraduationCeremony(n)
        obj.run()
