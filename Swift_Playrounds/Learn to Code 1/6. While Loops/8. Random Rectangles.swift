while !isBlocked {
    while isOnClosedSwitch {
        toggleSwitch()
    }
    moveForward()
    if isBlocked {
        turnRight()
    }
}
toggleSwitch()