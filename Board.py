#!/usr/bin/env python3.4
class Board:
    """Represents one board to a Tic-Tac-Toe game."""

    def __init__(self):
        """Initializes a new board.
        A board is a dictionary which the key is the position in the board
        and the value can be 'X', 'O' or ' ' (representing an empty position
        in the board.)"""
        self.board =[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def print_board(self):
        """Prints the board."""
        print(" %c | %c | %c " % (self.board[1],self.board[2],self.board[3]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[4],self.board[5],self.board[6]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[7],self.board[8],self.board[9]))
        print("   |   |   ")

    def _is_valid_move(self, position):
        if self.board[position] is " ":
            return True
        return False

    def change_board(self, position, type):
        """Receive a position and if the player is 'X' or 'O'.
        Checks if the position is valid, modifies the board and returns the modified board.
        Returns None if the move is not valid."""
        if self._is_valid_move(position):
            self.board[position] = type
            return self.board
        return None
