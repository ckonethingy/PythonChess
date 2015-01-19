import sys
WHITE = 0
BLACK = 1
chessboard = (
    '         \n'  #   0 -  9
    '         \n'  #  10 - 19
    ' rnbqkbnr\n'  #  20 - 29
    ' pppppppp\n'  #  30 - 39
    ' ........\n'  #  40 - 49
    ' ........\n'  #  50 - 59
    ' ........\n'  #  60 - 69
    ' ........\n'  #  70 - 79
    ' PPPPPPPP\n'  #  80 - 89
    ' RNBQKBNR\n'  #  90 - 99
    '         \n'  # 100 -109
    '          '   # 110 -119
)
#thanks thomasahle/sunfish/blob/master/sunfish.py

class gameState:
    currBoard = (
        '         \n'  #   0 -  9
        '         \n'  #  10 - 19
        ' rnbqkbnr\n'  #  20 - 29
        ' pppppppp\n'  #  30 - 39
        ' ........\n'  #  40 - 49
        ' ........\n'  #  50 - 59
        ' ........\n'  #  60 - 69
        ' ........\n'  #  70 - 79
        ' PPPPPPPP\n'  #  80 - 89
        ' RNBQKBNR\n'  #  90 - 99
        '         \n'  # 100 -109
        '          '   # 110 -119
    )


    def __init__(self, board):
        self.currBoard = board
        self.blackPts = 0
        self.whitePts = 0
        self.moves = 0
        # 0  for white, 1 for black
        self.turn = 0

    def show(self):
        print "____________"
        if self.turn == 0:
            print "White's move"
        else:
            print "Black's move"
        print self.currBoard
        print "White: " + str(self.whitePts)
        print "Black: " + str(self.blackPts)


    def nextTurn(self, nextMove):
        self.turn = (self.turn+1)%2
        self.moves += 1


#accepts a gameState and outputs it visually
def printGameState( gameState ):
    gameState.show()

#gives the move to the gameState
def nextMove( gameState, move ):
    gameState.nextTurn(move)

def main():
    Game = gameState(chessboard)
    printGameState(Game)
    moveRequest = raw_input("Next Move: ")
    while moveRequest != "q":
        nextMove(Game, moveRequest)
        printGameState(Game)
        moveRequest = raw_input("Next Move: ")
    
    print "Game Quitted"

if __name__ == "__main__":
    main()
