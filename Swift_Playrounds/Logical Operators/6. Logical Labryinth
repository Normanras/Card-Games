func solveRight() {
    turnRight()
    moveForward()
    moveForward()
    collectGem()
    turnLeft()
    turnLeft()
    moveForward()
    moveForward()
    turnRight()
}


for i in 1 ... 8 {
    moveForward()
    if isOnGem && isOnClosedSwitch {
        solveRight()
        collectGem()
        toggleSwitch()
    } else if isOnGem {
        collectGem()
    }
    if !isOnOpenSwitch && isBlocked  {
        toggleSwitch()
        turnLeft()
    } else if isOnClosedSwitch {
        toggleSwitch() 
        turnLeft()
    }
}
