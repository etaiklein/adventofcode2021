"""
--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

Your puzzle answer was 2250414.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
Then, to determine the CO2 scrubber rating value from the same example above:

Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""

import unittest


def reverse_binary(bstring):
    return ''.join(['1' if bit == '0' else '0' for bit in bstring])


def count_bits(input):
    counts = [0] * (len(input[0]) - 1)
    for current_element in input:
        bits = current_element
        for index in range(len(bits)):
            if bits[index] == "1":
                counts[index] = counts[index] + 1
    return counts


def get_gamma_and_epsilon_rates(filename):
    with open(filename) as f:
        input = f.readlines()

        counts = count_bits(input)
        binstring = ""
        for count in counts:
            binstring = binstring + "1" if \
                count > (len(input) - 1)/2 else binstring + "0"

        gamma_int = int("0b" + binstring, 2)
        epsilon_int = int("0b" + reverse_binary(binstring), 2)
        return gamma_int * epsilon_int


def recursively_check_matches(
    bO2, bCO2, index, bO2_matches, bCO2_matches
):
    new_bO2 = bO2
    new_bO2_matches = bO2_matches
    if len(bO2_matches) > 1:
        bO2_counts = count_bits(bO2_matches)
        bO2_count = bO2_counts[index]
        new_bO2 = bO2 + "1" if \
            bO2_count >= len(bO2_matches)/2 else bO2 + "0"
        new_bO2_matches = [
                matchable for matchable in bO2_matches
                if matchable.startswith(new_bO2)
            ] if len(bO2_matches) > 1 else bO2_matches

    new_bCO2 = bCO2
    new_bCO2_matches = bCO2_matches
    if len(bCO2_matches) > 1:
        bCO2_counts = count_bits(bCO2_matches)
        bCO2_count = bCO2_counts[index]
        new_bCO2 = bCO2 + "1" if \
            bCO2_count < len(bCO2_matches)/2 else bCO2 + "0"
        new_bCO2_matches = [
            matchable for matchable in bCO2_matches
            if matchable.startswith(new_bCO2)
        ] if len(bCO2_matches) > 1 else bCO2_matches

    if len(new_bO2_matches) > 1 or len(new_bCO2_matches) > 1:
        return recursively_check_matches(
            bO2=new_bO2,
            bCO2=new_bCO2,
            index=index+1,
            bO2_matches=new_bO2_matches,
            bCO2_matches=new_bCO2_matches,
        )

    return (new_bO2_matches[0], new_bCO2_matches[0])


def get_02_and_c02_rates(filename):
    with open(filename) as f:
        input = f.readlines()

        (bO2, bCO2) = recursively_check_matches(
            bO2="",
            bCO2="",
            index=0,
            bO2_matches=input,
            bCO2_matches=input,
        )
        return int("0b" + bO2, 2) * int("0b" + bCO2, 2)


class Test(unittest.TestCase):
    def test_part1_sample_input(self):
        output = get_gamma_and_epsilon_rates('day3input-sample.txt')
        self.assertEqual(output, 198)

    def test_part1_final_input(self):
        output = get_gamma_and_epsilon_rates('day3input.txt')
        self.assertEqual(output, 2250414)

    def test_part2_sample_input(self):
        output = get_02_and_c02_rates('day3input-sample.txt')
        self.assertEqual(output, 230)

    def test_part2_final_input(self):
        output = get_02_and_c02_rates('day3input.txt')
        self.assertEqual(output, 6085575)


if __name__ == '__main__':
    unittest.main()
