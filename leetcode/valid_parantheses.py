class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}

        for char in s:
            if char in pairs.keys():
                stack.append(char)

            else:   
                if not stack:
                    return False

                if char != pairs[stack[-1]]:
                    return False
                    
                stack.pop()
            
        return len(stack) == 0
            
        

            
           
