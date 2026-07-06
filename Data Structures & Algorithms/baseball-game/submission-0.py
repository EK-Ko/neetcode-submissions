class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == 'C':
                # invlidate previous score
                stack.pop()
            elif op == 'D':
                #new score that is double the previous
                stack.append(2 * stack[-1])
            elif op == '+':
                # + sum of the previous two
                stack.append(stack[-1] + stack[-2])
            else:
                #convert to number and push to stack
                stack.append(int(op))
        return sum(stack)