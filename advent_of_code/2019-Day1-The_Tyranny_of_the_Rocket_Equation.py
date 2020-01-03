# 2019-Day1-The_Tyranny_of_the_Rocket_Equation.py

# --- Day 1: The Tyranny of the Rocket Equation ---
# Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# The Elves quickly load you into a spacecraft and prepare to launch.

# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?

def fuel_required(mass: int) -> int:
    """Calculate the fuel required given mass of module to be launched."""

    # Take its mass, divide by three, round down, and subtract 2.

    return int(mass / 3) - 2


def fuel_counter_upper_part_1(filename: str) -> int:
    """Calculate the fuel needed for a text file containing module masses."""

    total_fuel_needed = 0

    with open(filename) as file:
        for module_weight in file:
            module_fuel_requirement = fuel_required(int(module_weight))
            total_fuel_needed += module_fuel_requirement

    return total_fuel_needed


def fuel_required_part_2(mass: int) -> int:
    """Calculate the fuel required for module and fuel given mass of module."""

    module_fuel = fuel_required(mass)
    fuel_fuel = module_fuel
    total_fuel_fuel = 0

    while fuel_fuel > 0:
        total_fuel_fuel += fuel_fuel
        fuel_fuel = fuel_required(fuel_fuel)

    return total_fuel_fuel


def fuel_counter_upper_part_2(filename: str) -> int:
    """Calculate the fuel needed for a text file containing module masses."""

    total_fuel_needed = 0

    with open(filename) as file:
        for module_weight in file:
            module_fuel_requirement = fuel_required_part_2(int(module_weight))
            total_fuel_needed += module_fuel_requirement

    return total_fuel_needed


import unittest

class TestFuelRequired(unittest.TestCase):

    def test_example_1(self):

        mass = 12
        fuel = 2
        self.assertEqual(fuel, fuel_required(mass))

    def test_example_2(self):

        mass = 14
        fuel = 2
        self.assertEqual(fuel, fuel_required(mass))

    def test_example_3(self):

        mass = 1969
        fuel = 654
        self.assertEqual(fuel, fuel_required(mass))

    def test_example_4(self):

        mass = 100756
        fuel = 33583
        self.assertEqual(fuel, fuel_required(mass))

class TestFuelCounterUpperPart1(unittest.TestCase):

    def setUp(self):
        self.filename = "2019-Day1-input.txt"

    def test_input(self):
        total_fuel_required = fuel_counter_upper_part_1(self.filename)
        print("Total Fuel Required Part 1:", total_fuel_required)
        self.assertEqual(
            total_fuel_required,
            3182375
        )

class TestFuelRequiredPart2(unittest.TestCase):

    def test_example_1(self):

        mass = 12
        fuel = 2
        self.assertEqual(fuel, fuel_required_part_2(mass))

    def test_example_2(self):

        mass = 14
        fuel = 2
        self.assertEqual(fuel, fuel_required_part_2(mass))

    def test_example_3(self):

        mass = 1969
        fuel = 966
        self.assertEqual(fuel, fuel_required_part_2(mass))

    def test_example_4(self):

        mass = 100756
        fuel = 50346
        self.assertEqual(fuel, fuel_required_part_2(mass))


class TestFuelCounterUpperPart2(unittest.TestCase):

    def setUp(self):
        self.filename = "2019-Day1-input.txt"

    def test_input(self):
        total_fuel_required = fuel_counter_upper_part_2(self.filename)
        print("Total Fuel Required Part 2:", total_fuel_required)
        self.assertEqual(
            total_fuel_required,
            4770725
        )


if __name__ == '__main__':
    unittest.main()

