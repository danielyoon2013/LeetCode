class Solution:
    def countAndSay(self, n: int) -> str:
        
        def createMap(s):
            if len(s) == 1:
                return [[s,"1"]]
            
            arr, count, curr = [], 1, s[0]
            
            for idx in range(len(s)):
                if idx+1 == len(s):
                    arr.append([curr,str(count)])
                
                elif s[idx] != s[idx+1]:
                    arr.append([curr,str(count)])
                    curr = s[idx+1]
                    count = 1
                else:
                    count += 1
            return arr
        
        def mergeMap(arr):
            s = ""
            for ele in arr:
                print(ele)
                s += ele[1]+ele[0]
                
            return s
       
        if n == 1:
            return "1"
        
        s = "1"
        while n-1:
            s = mergeMap( createMap( s ) ) 
            n -= 1
            
        return s
            
        