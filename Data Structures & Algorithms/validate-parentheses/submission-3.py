class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False # empty stack
                popped = stack.pop()
                if (char == ')' and popped != '(') or \
                   (char == ']' and popped != '[') or \
                   (char == '}' and popped != '{'):
                    return False
        return not stack
