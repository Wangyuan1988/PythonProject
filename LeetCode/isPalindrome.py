import math


class Solution:
    @classmethod
    def isPalindrome(cls, x: int) -> bool:
        return str(x)[::] == str(x)[::-1]

    @classmethod
    def isPalindromeInt(cls, x: int)->bool:
        r = list(map(lambda i: int(10**-i * x % 10),
                     range(int(math.log10(x)), -1, -1))) if x > 0 else [0, x]
        return r == r[::-1]


if __name__ == '__main__':
    print(Solution.isPalindromeInt(1221))
    