class Solution:
    def romanToInt(self,x:str)->int:
        all=0
        for count,char in enumerate(x):
            y=self.romanCharToInt(char)
            z=y
            if count>0:
                oldChar=x[count-1]
                oldInt=self.romanCharToInt(oldChar)
                if oldInt<y:
                    z=y-oldInt 
                    all-=oldInt
            all+=z
        return all
    
    def isBigger(self,x,y)->bool:
        return x>y
    
    def romanCharToInt(self,x)->int:
        if x=="M":
            return 1000
        elif x=="D":
            return 500
        elif x=="C":
            return 100
        elif x=="L":
            return 50
        elif x=="X":
            return 10
        elif x=="V":
            return 5
        elif x=="I":
            return 1

if __name__=="__main__":
    print(Solution().romanToInt("CDM"))