import re
class Solution:
    @classmethod
    def defangIPaddr(cls, address: str) -> str:
      return address.replace('.','[.]')

if __name__ == "__main__":
    print(Solution.defangIPaddr("1.1.1.1"))
