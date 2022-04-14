import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'src'))
import main, fileparser


def compareCapturesCompleteLevel1():
    board = fileparser.fileParser("./resources/level1_complete.txt")
    return main.checkCaptures(board)

def compareCapturesIncompleteLevel1():
    board = fileparser.fileParser("./resources/level1_incomplete.txt")
    return main.checkCaptures(board)

def checkCompleteVisited():
    board = fileparser.fileParser("./resources/level1_complete.txt")
    return board[0][-1] == 1

def checkIncompleteVisited():
    board = fileparser.fileParser("./resources/level1_incomplete.txt")
    return board[0][-1] == 1

def testFinishComplete():
    return compareCapturesCompleteLevel1() and  checkCompleteVisited()

def testFinishIncomplete():
    return compareCapturesIncompleteLevel1() and checkIncompleteVisited()

def testFinish():
    assert testFinishComplete(), "Should be Finished"
    assert testFinishIncomplete() == False, "Should not be Finished"


if __name__ == "__main__":
    testFinish()
    print("Everything passed")
