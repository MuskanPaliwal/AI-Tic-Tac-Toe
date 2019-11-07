import random
class Human:
    ''' Class for Human player'''
    def __init__(self,marker):
        self.marker = marker
        self.type = 'H'
    
    def move(self, gameinstance):

        while True:
        
            m = input("Input position:")

            try:
                m = int(m)
            except:
                m = -1
        
            if m not in gameinstance.get_free_positions():
                print("Invalid move. Retry")
            else:
                break
    
        gameinstance.mark(self.marker,m)
         
class AI:
    '''Class for Computer Player'''

    def __init__(self, marker):
        self.marker = marker
        self.type = 'C'

        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'

    def move(self,gameinstance):
        move_position,score = self.maximized_move(gameinstance)
        gameinstance.mark(self.marker,move_position)



    def maximized_move(self,gameinstance):
        ''' Find maximized move'''    
        bestscore = None
        bestmove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.marker,m)
        
            if gameinstance.is_gameover():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.minimized_move(gameinstance)
        
            gameinstance.revert_last_move()
            
            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

    def minimized_move(self,gameinstance):
        ''' Find the minimized move'''

        bestscore = None
        bestmove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.opponentmarker,m)
        
            if gameinstance.is_gameover():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.maximized_move(gameinstance)
        
            gameinstance.revert_last_move()
            
            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

    def get_score(self,gameinstance):
        if gameinstance.is_gameover():
            if gameinstance.winner  == self.marker:
                return 1 # Won

            elif gameinstance.winner == self.opponentmarker:
                return -1 # Opponent won
            
        return 0 # Draw
class Dummy:
    
    def __init__(self, marker):
        self.marker = marker
        self.type = 'D'
        self.board = [ ' ' for i in range(0,9) ]
        
        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'

    def move(self, gameinstance):
        move = random.choice(gameinstance.get_free_positions())
        gameinstance.mark(self.marker,move)
