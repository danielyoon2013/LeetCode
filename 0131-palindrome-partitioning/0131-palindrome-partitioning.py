class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        def check( start, end ):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
        
            return True
        
        def dfs( result, start, curr_list ):
            if start >= len(s):
                result.append(list(curr_list))
                
            for end in range( start, len(s) ):
                if check( start, end ):
                    curr_list.append( s[start:end+1] )
                    dfs( result, end+1, curr_list )
                    curr_list.pop()
                    
        final_result = []
        dfs( final_result, 0, [])
        
        return final_result
                    
                    
            
            
        