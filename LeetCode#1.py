class Solution:
    def TwoSum(self,x,y):
        for count, z in enumerate(x,1):
            for i in range(count, len(x)):
                n = x[i]
                if n + z == y:
                    return [z, n]
        return None  # If no such pair is found


if __name__=="__main__":
    print(Solution().TwoSum([3,2,3,1],6))