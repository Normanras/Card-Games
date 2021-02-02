for i in 1 ... 15 {
    if !isBlocked {
        moveForward()
    } else {
        turnLeft()
        moveForward()
    }
    if isOnClosedSwitch {
        toggleSwitch()
    }
    
}
