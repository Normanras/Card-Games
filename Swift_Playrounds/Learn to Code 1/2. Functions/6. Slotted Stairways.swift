func collectGemTurnAroound() {
    moveForward()
    moveForward()
    collectGem()
    turnLeft()
    turnLeft()
    moveForward()
    moveForward()
}

func solveRow() {
    collectGemTurnAroound()
    collectGemTurnAroound()
}

solveRow()
turnRight()
moveForward()
turnLeft()
solveRow()
turnRight()
moveForward()
turnLeft()
solveRow()