import sys


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

def printGameState():
    print "Current game state"
    print chessboard

def main():
    printGameState()
    moveRequest = raw_input("Next Move: ")
    while moveRequest != "q":
        print "Your move was " + moveRequest
        printGameState()
        moveRequest = raw_input("Next Move: ")
    
    print "Game Quitted"

if __name__ == "__main__":
    main()
