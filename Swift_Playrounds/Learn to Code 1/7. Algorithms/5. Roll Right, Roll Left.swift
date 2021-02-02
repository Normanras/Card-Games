for i in 1 ... 38 {
    if !isOnGem && !isOnClosedSwitch && !isBlocked {
        moveForward()
        } else if isOnClosedSwitch {
            toggleSwitch()
            turnLeft()
            moveForward()
            toggleSwitch()
            moveForward()
        } else if isOnGem {
            collectGem()
            turnRight()
            moveForward()
            collectGem()
            moveForward()
        } else if isBlocked && isBlockedRight {
            turnLeft()
            moveForward()
        } else if isBlocked && isBlockedLeft {
            turnRight()
            moveForward()
        }
    }

