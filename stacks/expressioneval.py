# Expression trees: leaves are operands and non-leaves are operators

# Build expression tree from postfix expression
"""
1.  Process each symbol in the expression from left to right
2a. If symbol is operand, create a node of that operand and make its left and right
    pointers None. Push the new node onto the stack.
2b. If symbol is an operator, pop the top two pointers (say T1 then T2) from the
    stack. Create a new node of that operator and make its left pointer T2 and its
    right pointer T1. Push the new node onto the stack.
"""
