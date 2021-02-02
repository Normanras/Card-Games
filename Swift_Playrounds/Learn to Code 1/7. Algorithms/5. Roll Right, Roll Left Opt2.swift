func moveForFour() {
    moveForward()
    moveForward()
    moveForward()
    moveForward()
}

func GemSwitch() {
    moveForward()
    collectGem()
    turnRight()
    moveForward()
    collectGem()
    moveForFour()
    turnLeft()
    moveForward()
    toggleSwitch()
    turnLeft()
    moveForward()
    toggleSwitch()
    moveForFour()
    moveForward()
    turnRight()
}

func TwoGemsEnd() {
   moveForward()
    collectGem()
    turnRight()
    moveForward()
    collectGem()
    moveForward()
    moveForward()
    moveForward() 
}

for i in 1 ... 3 {
    GemSwitch
}
TwoGemsEnd()
