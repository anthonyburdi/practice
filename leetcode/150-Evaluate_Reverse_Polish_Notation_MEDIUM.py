# 150-Evaluate_Reverse_Polish_Notation_MEDIUM.py

# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Note:

# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
# Example 1:

# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Evaluate arithmetic given in reverse polish notation."""
        # Assumptions
        # Input is only integers
        # only +, -, /, * operations given
        # division should truncate towards zero
        # RPN expression is always valid

        # Approach, complexity, tradeoffs, potential improvements
        # iterate through until we hit the first operator
        # replace operator and two items to it's left with the value of
        # the operation
        # Continue iterating from where the previous operator was (less 2)
        # due to the removal of the 3 items (and adding of result)
        # time complexity O(N) since we traverse the list once
        # where N is the number of tokens
        # space complexity O(1) since we do this in place

        # AHA - so integer division in the problem doesn't want to round down
        # to the nearest digit if that digit is negative. Strange.
        # e.g. 6/-132 should be -1, but the problem wants 0
        # Maybe it wants us to round towards zero (up if negative and down
        # if positive)

        # Edge cases
        # empty tokens
        # single token
        # three tokens incl one operator

        # Handle edge cases
        if len(tokens) == 1:
            return int(tokens[0])
        if len(tokens) == 0:
            return 0

        pointer = 0
        while len(tokens) > 1:
            if tokens[pointer] in ["+", "-", "*", "/"]:
                # process pointer
                a = int(tokens[pointer - 2])
                operator = tokens.pop(pointer) # TODO: CHECK THIS!
                b = int(tokens.pop(pointer - 1))

                if operator == "+":
                    tokens[pointer - 2] = a + b
                elif operator == "-":
                    tokens[pointer - 2] = a - b
                elif operator == "*":
                    tokens[pointer - 2] = a * b
                elif operator == "/":
                    # for this problem integer division means round down
                    # if positive and round up if negative
                    # so not the following:
                    # tokens[pointer - 2] = a // b # Integer division
                    # import math
                    temp = a / b
                    if temp < 0:
                        tokens[pointer - 2] = math.ceil(temp)
                    else:
                        tokens[pointer - 2] = math.floor(temp)

                # move pointer back to before we popped items
                pointer -= 2

            # move pointer forward if we are not processing anything
            pointer += 1

        return tokens[0]

        # Manual check

        # ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

        # pointer = 0
        # ...
        # pointer = 4 operator = "+"
        # a = 9 b = 3
        # ["10", "6", 12, "-11", "*", "/", "*", "17", "+", "5", "+"]
        # pointer = 2
        # ...
        # pointer = 4 operator = "*"
        # a = 12 b = -11
        # ["10", "6", -132, "/", "*", "17", "+", "5", "+"]
        # pointer = 2
        # pointer = 3  operator = "/"
        # a = 6 b = -132
        # ["10", 0, "*", "17", "+", "5", "+"]
        # pointer = 1
        # pointer = 2 operator = "*"
        # a = 10 b = 0
        # [0, "17", "+", "5", "+"]
        # pointer = 0
        # ...
        # pointer = 2 operator = "+"
        # a = 0 b = 17
        # [17, "5", "+"]
        # pointer = 0
        # ...
        # pointer = 2 operator = "+"
        # a = 17 b = 5
        # [22]
        # return 22 correct

