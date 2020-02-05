# 22-Generate_Parentheses_MEDIUM.py

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


from typing import List

class Solution:

    def __init__(self):
        self.answer = []

    def generateParenthesis(self, n: int) -> List[str]:
        # Assumptions
        # n small enough that list can fit on a single computer
        # n small enough that we don't hit the recursion limit
        # only () type of parenthesis are used

        # Approach
        # create a function to check if parenthesis are well formed
        # create a recursion tree where left is ( and right is )
        # for each new node check if parens are well formed
        # if the len = n * 2 then stop recursing and add to the list of
        # solutions. Maybe solution should be stored as a set? then converted
        # to a list since that is the desired output. I don't think this is
        # necessary bc we won't try any duplicates, but maybe it is necessary.

        # I think maybe instead I have to make a tree structure with left
        # node = "(" and right node = ")"
        # then stop when we hit the leaves and check for well formed parens

        # Complexity
        # Time: O(n!) since we have many cases to check. Though with
        # backtracking this is reduced considerably.
        # Space: O(n!) since we will store each passing solution

        # Potential improvements
        # We can change the recursion to iteration so n can be arbitrarily
        # large (assuming we can store the data).

        # Edge cases
        # n = 0
        # n < 0
        # n not type(int)


        # take care of edge cases
        if type(n) is not int or n <= 0:
            return [""]

        subset = [None] * (n * 2)

        def helper(n: int, subset: List, i: int) -> None:

            if i == n * 2:
                subset_str = "".join(subset)

                if self.is_valid_parens(subset_str):
                    self.answer.append(subset_str)

            else:

                # include left paren
                subset[i] = "("
                helper(n, subset, i + 1)

                # include right paren
                subset[i] = ")"
                helper(n, subset, i + 1)


        helper(n, subset, 0)

        return self.answer


    def is_valid_parens(self, subset: str) -> bool:
            """Determine if a string has a valid arrangement of parens."""
            stack = []
            for char in subset:
                if char == "(":
                    stack.append(char)
                elif stack == []:
                    return False
                else:
                    stack.pop()

            return stack == []



    def check_if_well_formed_parens(self, s: str) -> bool:
        """Check a string to make sure the parenthesis are well formed."""

        if s == "":
            return True

        # use a stack, put on ( and take off when ), make sure is empty

        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            if char == ")":
                if stack == []:
                    return False
                stack.pop()

        if stack == []:
            return True
        else:
            return False


import unittest

class TestCheckIfWellFormedParens(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_true_examples(self):

        parens = [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]
        for item in parens:
            self.assertTrue(self.solution.check_if_well_formed_parens(item))
            self.assertTrue(self.solution.is_valid_parens(item))


    def test_false_examples(self):
        parens = [
            "(()(",
            "())()()",
            ")()()()(",
            "(()))()("
        ]
        for item in parens:
            self.assertFalse(self.solution.check_if_well_formed_parens(item))
            self.assertFalse(self.solution.is_valid_parens(item))


    def test_edge_cases(self):
        self.assertTrue(self.solution.check_if_well_formed_parens(""))
        self.assertTrue(self.solution.check_if_well_formed_parens("()"))
        self.assertFalse(self.solution.check_if_well_formed_parens(")"))
        self.assertFalse(self.solution.check_if_well_formed_parens("("))
        self.assertFalse(self.solution.check_if_well_formed_parens(")("))

        self.assertTrue(self.solution.is_valid_parens(""))
        self.assertTrue(self.solution.is_valid_parens("()"))
        self.assertFalse(self.solution.is_valid_parens(")"))
        self.assertFalse(self.solution.is_valid_parens("("))
        self.assertFalse(self.solution.is_valid_parens(")("))


class TestGenerateParenthesis(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_edge_cases(self):
        # Edge cases
        # n = 0
        # n < 0
        # n not type(int)
        n = 0
        self.assertEqual(self.solution.generateParenthesis(n), [""])
        n = -1
        self.assertEqual(self.solution.generateParenthesis(n), [""])
        n = "0"
        self.assertEqual(self.solution.generateParenthesis(n), [""])

    def test_example_1(self):

        n = 3
        output = set([
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ])

        function_output = set(self.solution.generateParenthesis(n))

        self.assertEqual(
            function_output,
            output
        )

    def test_n_is_2(self):

        n = 2
        output = set([
            "()()",
            "(())"
        ])

        function_output = set(self.solution.generateParenthesis(n))

        self.assertEqual(
            function_output,
            output
        )

    def test_n_is_1(self):

        n = 1
        output = set([
            "()"
        ])

        function_output = set(self.solution.generateParenthesis(n))

        self.assertEqual(
            function_output,
            output
        )

    def test_n_is_4(self):

        n = 4
        output = set([
            "(((())))",
            '((())())',
            '((()))()',
            '(()())()',
            '(()()())',
            '()(())()',
            '()()()()',
            '(()(()))',
            '((()()))',
            '()((()))',
            '()()(())',
            '()(()())',
            '(())()()',
            '(())(())'
        ])

        function_output = set(self.solution.generateParenthesis(n))

        self.assertEqual(
            function_output,
            output
        )

if __name__ == '__main__':
    unittest.main()


















