func gemswitch() {
    if isOnClosedSwitch {
        toggleSwitch()
    } else if isOnGem {
        collectGem()
    } else {
        moveForward()
        if isBlocked {
            turnLeft()
        }
    }
}

for i in 1 ...  15 {
    gemswitch()
}
