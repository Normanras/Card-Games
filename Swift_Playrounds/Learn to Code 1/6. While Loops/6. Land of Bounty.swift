while !isBlocked {
    moveForward()
    if isOnClosedSwitch {
        toggleSwitch()
    }
    }
if isBlocked {
    turnRight()
    moveForward()
    turnRight()
}
while !isBlocked {
    moveForward()
    if isOnGem {
        collectGem()
    }
}
if isBlocked {
    turnLeft()
    moveForward()
    turnLeft()
}
while !isBlocked {
    moveForward()
    if isOnClosedSwitch {
        toggleSwitch()
    }
}


    
    
    
    
