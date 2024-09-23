from os import system
system("cls")

def argBall(studentBalls : dict) -> dict:
    studentNames = list(studentBalls.keys())
    studentBallsList = list(studentBalls.values()) 
    m = len(studentBallsList)
    for i in range(m):
        yigindiBall = sum(studentBallsList[i])
        studentBalls[studentNames[i]] = yigindiBall / len(studentBallsList[i])
    
    return studentBalls

studentBalls = {
    'ali' : [85, 90, 78],
    'bobur' : [80, 88, 92],
    'Charli' : [90, 95, 87]
}

print(argBall(studentBalls))


