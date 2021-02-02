while isBlockedRight {
    moveForward()
    if isOnClosedSwitch && !isBlocked {
        toggleSwitch()
        turnRight()
        moveForward()
    } else if isOnClosedSwitch && isBlocked {
        toggleSwitch()
        turnLeft()
        moveForward()
    } else {
        if isOnGem {
            collectGem()
            turnLeft()
        }
    }
    }