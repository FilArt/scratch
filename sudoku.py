from typing import List

from helpers import split_by_chunks


class Sudoku:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        return '\n'.join(self.board)

    def get_rows(self):
        return self.board

    def get_cols(self):
        return [row[i] for row in self.board for i in range(9)]

    def get_cells(self):
        return [[row[x:x + 3] for row in self.board[y:y + 3]] for x in (0, 3, 6) for y in (0, 3, 6)]


def boards_from_file(path: str) -> List[Sudoku]:
    with open(path) as file:
        data = file.readlines()
        correct_lines = [line.strip() for line in data if len(line) in (9, 10)]
        boards = split_by_chunks(correct_lines, chunk_size=9)
    return [Sudoku(board) for board in boards]


def main():
    path = 'xxx'
    boards = boards_from_file(path)
