"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?


"""
import unittest

def part1(filename):
    with open(filename) as f:
        # build our map
        cave = []
        for line in f:
            cave.append(
                [int(x) for x in line.split()[0]]
            )
        heights = 0
        for y, row in enumerate(cave):
            for x, val in enumerate(row):
                if y > 0:
                    if cave[y-1][x] <= val:
                        continue
                if y < len(cave) - 1:
                    if cave[y+1][x] <= val:
                        continue
                if x > 0:
                    if cave[y][x-1] <= val:
                        continue
                if x < len(cave[y]) - 1:
                    if cave[y][x+1] <= val:
                        continue
                heights += val + 1

        return heights


def part2(filename):
    with open(filename) as f:
        # build our map
        cave = []
        for line in f:
            cave.append(
                [int(x) for x in line.split()[0]]
            )
        local_minimum_locations = []
        for y, row in enumerate(cave):
            for x, val in enumerate(row):
                if y > 0:
                    if cave[y-1][x] <= val:
                        continue
                if y < len(cave) - 1:
                    if cave[y+1][x] <= val:
                        continue
                if x > 0:
                    if cave[y][x-1] <= val:
                        continue
                if x < len(cave[y]) - 1:
                    if cave[y][x+1] <= val:
                        continue
                local_minimum_locations.append((x, y))

        # get_basin_values
        basin_values = []
        for minimum_location in local_minimum_locations:
            all_locations = [minimum_location]
            queue = [minimum_location]
            while queue:
                check_this = queue.pop()
                x = check_this[0]
                y = check_this[1]

                if y < 0 or y >= len(cave) or x < 0 or x >= len(cave[y]) or cave[y][x] == 9:
                    continue

                if check_this not in all_locations:
                    all_locations.append(check_this)

                next_to_check = [
                    (x-1, y),
                    (x+1, y),
                    (x, y-1),
                    (x, y+1),
                ]
                for coordinate in next_to_check:
                    if coordinate not in all_locations:
                        queue.append(coordinate)

            basin_values.append(len(all_locations))

        basin_values.sort()
        return basin_values[len(basin_values) - 1] * \
            basin_values[len(basin_values) - 2] * \
            basin_values[len(basin_values) - 3]

class Test(unittest.TestCase):
    def test_sample_input(self):
        output = part1('day9input-sample.txt')
        self.assertEqual(output, 15)

    def test_part1_final_input(self):
        output = part1('day9input.txt')
        self.assertEqual(output, 530)

    def test_part2_sample_input(self):
        output = part2('day9input-sample.txt')
        self.assertEqual(output, 1134)

    def test_part2_final_input(self):
        output = part2('day9input.txt')
        self.assertEqual(output, 1019494)

if __name__ == '__main__':
    unittest.main()
