class Solution:
    def isValid(self, s: str) -> bool:
        '''
        given string s: with ( ), { }, [], order maddders
        open brackets closed in correct order
        '''
        
        stack = []
        brackets = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }

        for sym in s:
            if sym not in brackets.keys():
                stack.append(sym)
            else:
                if len(stack) == 0:
                    return False
                else:
                    last_value = stack.pop()
                if last_value != brackets[sym]:
                    return False
        if len(stack) > 0:
            return False
        return True

        