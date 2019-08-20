#!/usr/bin/env python3.4
import random
import Player
class GAME:

    def __init__(self):
        '''Initialize parameters - the game board, moves stack and winner'''

        self.board = [ ' ' for i in range(0,9) ]
        self.lastmoves = []
        self.winner = None

    def print_board(self):
        """Prints the board."""
        print(" %c | %c | %c " % (self.board[0],self.board[1],self.board[2]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[3],self.board[4],self.board[5]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[6],self.board[7],self.board[8]))
        print("   |   |   ")


    def get_free_positions(self):
        '''Get the list of available positions'''

        moves = []
        for i,v in enumerate(self.board):
            if v==' ':
                moves.append(i)
        return moves

    def mark(self,marker,pos):
        '''Mark a position with marker X or O'''
        self.board[pos] = marker
        self.lastmoves.append(pos)

    def revert_last_move(self):
        '''Reset the last move'''

        self.board[self.lastmoves.pop()] = ' '
        self.winner = None

    def is_gameover(self):
        '''Test whether game has ended'''

        win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8), (2,4,6)]

        for i,j,k in win_positions:
            if self.board[i] == self.board[j] == self.board[k] and self.board[i] != ' ':
                self.winner = self.board[i]
                return True

        if ' ' not in self.board:
            self.winner = ' '
            return True
        return False

    def play(self,player1,player2):
        '''Execute the game play with players'''

        self.p1 = player1
        self.p2 = player2
    
        for i in range(9):

            self.print_board()

            if i%2==0:
                if self.p1.type =='H':
                    print("\t\t[Player1's Move]")
                else:
                    print("\t\t[Player2's Move]")
                self.p1.move(self)
            else:
                if self.p2.type =='H':
                    print("\t\t[Player1's Move]")
                else:
                    print("\t\t[Player2's Move]")

                self.p2.move(self)

            if self.is_gameover():
                self.print_board()
                if self.winner == ' ':
                    print("\nGame over with Draw")
                else:
                    print("\nWinner : %s" %self.winner)
                return

if __name__ == '__main__':
    game=GAME()
    '''player1 =Player.AI("X")'''
    player1 =Player.Human("O")
    player2 =Player.Dummy("X") 
    game.play( player1, player2)
