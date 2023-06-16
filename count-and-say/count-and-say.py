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
            print(s)
            n -= 1
            
        return s
            
        
        '''
        if n == 1:
            return "1"
        
        curr = "11"
        
        for i in range(n-1):
            new_curr = ""
            multplier = 1
            for idx in range(1,len(curr)):
                if curr[idx] != curr[idx-1]:
                    new_curr += curr[idx] + str(multiplier)
                    multiplier = 1
                else:
                    multplier += 1 
                    
            curr = new_curr
                     
        return new_curr
        '''