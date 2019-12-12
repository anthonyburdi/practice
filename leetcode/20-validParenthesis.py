# 20-validParenthesis.py

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:

        # Loop through the string. Add each open paren complement to a list
        # if the current element is a closed paren, check the last element
        # in the list for it's open paren pair
        # if it is there, remove it from the list and continue
        # if it is not there, halt and return False since it's an invalid paren

        # first return True if given empty list (per instructions)
        if not s:
            return True

        open_parens = ['(', '{', '[']
        close_parens = [')', '}', ']']
        pairs = {'(': ')', '{': '}', '[': ']'}

        close_paren_stack = []

        for item in s:
            # Add pair of open paren to stack
            if item in open_parens:
                close_paren_stack.append(pairs[item])

            # If closed paren, make sure it is at end
            # of close_paren_stack
            if item in close_parens:
                # make sure there are items to check
                if not close_paren_stack:
                    return False
                elif not item == close_paren_stack.pop():
                    return False

        # if there are any leftover close parens
        # in close_paren_stack return False
        if close_paren_stack:
            return False

        # if all parens are valid return True
        return True




if __name__ == "__main__":
    solution = Solution()

    answers = [True, True, False, False, True, True, False, False, False, False]
    print("answers: {}".format(answers))

    test_items = ["()", "()[]{}", "(]", "([)]", "{[]}", "", "[", "]", "[[()", "]]{}"]

    test_answers = list(map(solution.isValid, test_items))

    print("test_items: ", test_items)
    print("test_answers: ", test_answers)

    for item in test_items:
        print(item, ":", solution.isValid(item))

    if answers == test_answers:
        print("Passed Test, Hooray!")
    else:
        print("Failed Test :(")
