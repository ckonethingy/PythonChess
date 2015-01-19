import sys
import re

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

def parseRequest(request):
    # get the piece in request
    if !re.match(r"^[KRQBN]?[a-h][1-8]"):
        print "Get more legit pleb."
        return

    loc = request[-2:]
    piece = request[0] if len(request) == 3 else "P"


if __name__ == "__main__":
    main()
