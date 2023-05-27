class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        
        for token in tokens:
            
            if token not in "+-*/":
                stack.append(int(token))
                
            else:
                r, l = stack.pop(), stack.pop()
                
                if token == "+":
                    stack.append( l+r )
                elif token == "-":
                    stack.append( l-r )
                elif token == "*":
                    stack.append( l*r )
                else:
                    stack.append(int(float(l)/r))
        
        return stack[0]