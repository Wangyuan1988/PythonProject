from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        
        for i in range(0,len(strs[0])):
            result=str(strs[0][0:i+1])
            for item in strs:
                if not item.startswith(result) :
                    result=strs[0][0:i]
                    return result
                else:
                    continue
        return result

if __name__ =="__main__":
    solution=Solution()
    
    print(solution.longestCommonPrefix(["dog","dacecar","dar"]))