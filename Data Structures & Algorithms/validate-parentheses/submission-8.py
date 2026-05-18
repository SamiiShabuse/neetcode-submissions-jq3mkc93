class Solution:
    def isValid(self, s: str) -> bool:
        
        result = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []
        for char in s:
            if char not in result.keys():
                stack.append(char)
            elif char in result.keys():
                if len(stack) == 0:
                    return False
                cur = stack.pop()
                if cur != result[char]:
                    return False
        if len(stack) > 0:
            return False
        return True


