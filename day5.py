"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

"""

import unittest


def add(coordinates_map, coordinate):
    if coordinate in coordinates_map:
        coordinates_map[coordinate] += 1
    else:
        coordinates_map[coordinate] = 1
    return coordinates_map


def map_vents(filename, include_diagonals):
    with open(filename) as f:
        coordinates_map = {}
        for line in f:
            start, end = line.split(" -> ")

            # get start and end coordinates
            start_x, start_y = start.split(",")
            end_x, end_y = end.split(",")

            # add coordinates to map
            if int(start_y) == int(end_y):
                y = int(start_y)
                for x in range(int(start_x), int(end_x) + 1):
                    coordinates_map = add(coordinates_map, f"{x},{y}")
                for x in range(int(end_x), int(start_x) + 1):
                    coordinates_map = add(coordinates_map, f"{x},{y}")
            elif int(start_x) == int(end_x):
                x = int(start_x)
                for y in range(int(start_y), int(end_y) + 1):
                    coordinates_map = add(coordinates_map, f"{x},{y}")
                for y in range(int(end_y), int(start_y) + 1):
                    coordinates_map = add(coordinates_map, f"{x},{y}")
            elif include_diagonals:
                y = int(start_y)
                x = int(start_x)
                y_dir = 1 if int(end_y) > int(start_y) else -1
                x_dir = 1 if int(end_x) > int(start_x) else -1
                while y != int(end_y) + y_dir and x != int(end_x) + x_dir:
                    coordinates_map = \
                        add(coordinates_map, f"{x},{y}")
                    y = y + y_dir
                    x = x + x_dir

        return sum(1 if val > 1 else 0 for val in coordinates_map.values())



class Test(unittest.TestCase):
    def test_part1_sample_input(self):
        output = map_vents('day5input-sample.txt', include_diagonals=False)
        self.assertEqual(output, 5)

    def test_part1_final_input(self):
        output = map_vents('day5input.txt', include_diagonals=False)
        self.assertEqual(output, 7436)

    def test_part2_sample_input(self):
        output = map_vents('day5input-sample.txt', include_diagonals=True)
        self.assertEqual(output, 12)

    def test_part2_final_input(self):
        output = map_vents('day5input.txt', include_diagonals=True)
        self.assertEqual(output, 21104)

if __name__ == '__main__':
    unittest.main()
