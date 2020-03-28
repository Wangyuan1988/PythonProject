class Solution:
    def reverse(self, x: int) -> int:
        y,res=abs(x),0
        offset=(1<<31)-1 if x>0 else 1<<31
        while y!=0:
            res =res*10+y%10
            if res>offset:return 0
            y//=10
        return res if x>0 else -res        

if __name__ == "__main__":
    solution= Solution()
    # print(solution.reverse(123456))
    for i in range(1,20):
        print(2**i== 2<<i)