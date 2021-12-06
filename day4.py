"""
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
"""


import unittest

class BingoGame:
    def __init__(self):
        self.numbers_called = []
        self.boards = []

    def start(self):
        for number in self.numbers_called:
            for board in self.boards:
                board.call_number(number)
                if board.did_win():
                    print(self.__str__())
                    return board.get_score()


    def __str__(self):
        return f"numbers_called {self.numbers_called}, boards {[str(board) for board in self.boards]}"

class BingoBoard:
    def __init__(self, name):
        self.name = name
        self.board = [0] * 25
        self.has_been_called = [False] * 25
        self.last_called_number = -1

    def did_win(self):
        # column, row, or diagonal are all called
        winnable_indices = [
            # horizontal rows
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],
            # vertical columns
            [0, 5, 10, 15, 20],
            [1, 6, 11, 16, 21],
            [2, 7, 12, 17, 22],
            [3, 8, 13, 18, 23],
            [4, 9, 14, 19, 24],
            # diagonal rows
            # [0,6,12,18,24] diagonals dont count
            # [20,16,12,8,4] diagonals dont count
        ]

        for index_set in winnable_indices:
            if all([self.has_been_called[index] for index in index_set]):
                print("winning set", index_set, [self.has_been_called[index] for index in index_set], [self.board[index] for index in index_set], self.last_called_number)
                return True
        return False

    def get_score(self):
        score_board = []
        for i in range(24):
            score_value_multiplier = 0 if self.has_been_called[i] else 1
            score_board.append(self.board[i] * score_value_multiplier)
        print(f"score, {sum(score_board)} * {self.last_called_number}")
        return sum(score_board) * self.last_called_number

    def call_number(self, called_number):
        self.last_called_number = called_number
        try:
            index = self.board.index(called_number)
            self.has_been_called[index] = True
        except:
            pass

    def p(self, index):
        return f" {self.board[index]} " if not self.has_been_called[index] else f"*{self.board[index]}*"

    def __str__(self):
        string_board = ""
        print(f"b{self.name}{', winner' if self.did_win() else ''}")
        for i in range(25):
            if self.board[i] < 10:
                string_board += " "
            string_board += self.p(i)
            if i % 5 == 0:
                string_board += '\n'
        return string_board

def play_bingo(filename):
    bingo_game = BingoGame()
    with open(filename) as f:
        line =  f.readline()
        bingo_game.numbers_called = [
            int(i) for i in line.split(",")
        ]
        current_board = None
        board_index = 0
        board_name = 0
        for line in f:
            if len(line) < 2:
                current_board = BingoBoard(board_name)
                board_name = board_name+1
                board_index = 0
                bingo_game.boards.append(current_board)
            elif current_board:
                for i in line.split():
                    current_board.board[board_index] = int(i)
                    board_index = board_index + 1

        return bingo_game.start()

class Test(unittest.TestCase):
    def test_part1_sample_input(self):
        output = play_bingo('day4input-sample.txt')
        self.assertEqual(output, 4512)

    def test_part1_final_input(self):
        output = play_bingo('day4input.txt')
        self.assertEqual(output, 1)
    """
        def test_part2_sample_input(self):
            output = get_02_and_c02_rates('day3input-sample.txt')
            self.assertEqual(output, 230)

        def test_part2_final_input(self):
            output = get_02_and_c02_rates('day3input.txt')
            self.assertEqual(output, 6085575)
    """

if __name__ == '__main__':
    unittest.main()
