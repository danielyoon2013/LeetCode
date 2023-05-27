from collections import Counter
from heapq import heappush, heappop

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count, h = Counter( tasks ), []
        
        for k, v in count.items():
            heappush(h, (-1*v,k))

        result = 0
        while h:
            temp, i = [], 0
            
            while i <= n:
                
                result +=1
                if h:
                    v,k = heappop(h)
                    if v != -1:
                        temp.append((v+1,k))

                if not temp and not h:
                    break
                i+=1

            for element in temp:
                heappush(h, element)
                
        return result