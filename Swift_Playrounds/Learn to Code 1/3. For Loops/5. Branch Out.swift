func move3times() {
    moveForward()
    moveForward()
    moveForward()
}
func turnAround() {
    turnLeft()
    turnLeft()
}

func StairSequence() {
    turnRight()
    move3times()
    move3times()
    moveForward()
    toggleSwitch()
    turnAround()
    moveForward()
    move3times()
    move3times()
}

moveForward()
for i in 1 ... 3 {
    moveForward()
    StairSequence()
    turnRight()
    moveForward()
}
