"""
--- Day 7: The Treachery of Whales ---
A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

For example, consider the following horizontal positions:

16,1,2,0,4,2,7,1,2,14
This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

Move from 16 to 2: 14 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 0 to 2: 2 fuel
Move from 4 to 2: 2 fuel
Move from 2 to 2: 0 fuel
Move from 7 to 2: 5 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 14 to 2: 12 fuel
This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

--- Part Two ---
The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

Move from 16 to 5: 66 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 0 to 5: 15 fuel
Move from 4 to 5: 1 fuel
Move from 2 to 5: 6 fuel
Move from 7 to 5: 3 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 14 to 5: 45 fuel
This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?

"""

import unittest


def fuel_those_crabs(filename):
    with open(filename) as f:
        crab_positions = [int(crab) for crab in f.readline().split(",")]
        crab_positions.sort()
        print(crab_positions)

        seen_crab_positions = []
        least_fuel_value = 10000000000
        least_fuel_position = 0
        for current_position in crab_positions:
            if current_position in seen_crab_positions:
                continue
            seen_crab_positions.append(current_position)
            current_fuel_spend = 0
            for crab_position in crab_positions:
                current_fuel_spend += abs(crab_position - current_position)
            if current_fuel_spend < least_fuel_value:
                least_fuel_value = current_fuel_spend
                least_fuel_position = current_position
        print(least_fuel_position, least_fuel_value)
        return least_fuel_value

def fancy_fuel_those_crabs(filename):
    with open(filename) as f:
        crab_positions = [int(crab) for crab in f.readline().split(",")]
        crab_positions.sort()
        min_crab = crab_positions[0]
        max_crab = crab_positions[len(crab_positions)-1]

        least_fuel_value = 100000000000000000
        least_fuel_position = 0
        for current_position in range(min_crab, max_crab):
            current_fuel_spend = 0
            for crab_position in crab_positions:
                # fancy fuel expressed as n(n+1)/2
                n = abs(crab_position - current_position)
                current_fuel_spend += n*(n + 1)/2
            if current_fuel_spend < least_fuel_value:
                least_fuel_value = current_fuel_spend
                least_fuel_position = current_position
        print(least_fuel_position, least_fuel_value)
        return least_fuel_value


class Test(unittest.TestCase):
    def test_part1_sample_input(self):
        output = fuel_those_crabs('day7input-sample.txt')
        self.assertEqual(output, 37)

    def test_part1_final_input(self):
        output = fuel_those_crabs('day7input.txt')
        self.assertEqual(output, 356179)

    def test_part2_sample_input(self):
        output = fancy_fuel_those_crabs('day7input-sample.txt')
        self.assertEqual(output, 168)

    def test_part2_final_input(self):
        output = fancy_fuel_those_crabs('day7input.txt')
        self.assertEqual(output, 99788435)

if __name__ == '__main__':
    unittest.main()
