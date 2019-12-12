class Solution:
    def romanToInt(self, s: str) -> int:
        # Start by splitting the string into symbols
        # Group subtractions together, maybe loop through once and check for them?
        # E.g. look ahead to next letter and if it is greater then group
        # Sum up the resulting symbols

        symbols = [letter for letter in s]

        subtraction = False # Keep track of whether current loop is subtraction

        numeral_to_int = 0

        for idx, letter in enumerate(symbols):

            # Skip this loop if the previous loop was subtraction
            if subtraction:
                subtraction = False # Reset subtraction so we continue with the loop
                continue

            # first check to make sure we are not at the end of the list
            if (idx + 1) < len(symbols):
                next_letter = symbols[idx+1]

                # Check for all subtractions

                # check for CD and CM subtraction
                if letter == "C" and next_letter == "D":
                    numeral_to_int += 400
                    subtraction = True
                    continue
                if letter == "C" and next_letter == "M":
                    numeral_to_int += 900
                    subtraction = True
                    continue

                # Check for XL and XC subtraction
                if letter == "X" and next_letter == "L":
                    numeral_to_int += 40
                    subtraction = True
                    continue
                if letter == "X" and next_letter == "C":
                    numeral_to_int += 90
                    subtraction = True
                    continue

                # Check for IV and IX subtraction
                if letter == "I" and next_letter == "V":
                    numeral_to_int += 4
                    subtraction = True
                    continue
                if letter == "I" and next_letter == "X":
                    numeral_to_int += 9
                    subtraction = True
                    continue

            # If no subtractions, add the correct numeral value
            # Unindented bc this can be the last element of the list
            numeral_values = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
            }

            numeral_to_int +=  numeral_values[letter]

        return numeral_to_int

