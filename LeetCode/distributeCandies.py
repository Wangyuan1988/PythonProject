from typing import List


class Solution:
    @classmethod
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        if candies < 1 or candies > 10**9:
            print('candies is wrong')
            return []
        if num_people < 1 or num_people > 1000:
            print('num_people is wrong')
            return []

        result = [0 for _ in range(num_people)]
        n = 0
        while candies > 0:
            for i in range(1, num_people+1):
                if candies >= i + n*num_people:
                    result[i-1] += i + n*num_people
                else:
                    result[i-1] += candies
                candies = candies - (i + n*num_people) if candies - (i+n*num_people) > 0 else 0
            n += 1
        return result

    @classmethod
    def distributeCandiesInternet(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 0
        while candies > i:
            result[i % num_people] += i + 1
            candies -= i + 1
            i += 1
        result[i % num_people] += candies
        return result


if __name__ == "__main__":
    print(Solution.distributeCandiesInternet(10, 3))
