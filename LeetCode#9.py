class Solution:
    def IsPalindrome(self,x:int)->bool:
        if x<0:
            return False
        reverse = []
        while x > 0:
            reverse.append(x % 10)
            x //= 10
        digits=reverse[::-1]
        return digits==reverse
    
if __name__=="__main__":
    print(Solution().IsPalindrome(3113))