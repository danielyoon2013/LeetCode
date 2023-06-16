class Solution:
    def countAndSay(self, n: int) -> str:
        
        '''Suggested'''
        curr_ = "1"
        
        for _ in range(n-1):
            next_ = ""
            j, k = 0, 0
            
            while j < len(curr_):
                while k < len(curr_) and curr_[k] == curr_[j]:
                    k+=1
                next_ += str(k-j) + curr_[j]
                j = k
                
            curr_ = next_
            
        return curr_
        
        ''' My Solution
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
        '''
    
            
        