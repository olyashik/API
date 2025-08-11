import base_commands
from base_commands import ProtivChStrMove, PoChStrMove, PoChStrDown, ProtivChStrDown, Step, StopMove, StopDown, step_motor_down, step_motor_move, 

# Возвращение в исхоную точку
def PointZeroMove(Elev):
    k = 1
    while (k == 1):
        if Elev > 0:
            ProtivChStrMove(Step(Elev))
            k = 0
        elif Elev < 0:
            PoChStrMove(Step(Elev))
            k = 0
        else:
            k = 0
    StopMove()

# Совместное движение
def PoDownPoMove(SA, SE):
    j = 0
    if SA >= SE:
        while j < SE:
            for i in range(4):
                step_motor_down(stepSequenceCW[i], 8)
                step_motor_move(stepSequenceCW[i], 8)
            j += 1
        StopMove()
        PoChStrDown(SA - SE)
            
    elif SE > SA:
        while j < SA:
            for i in range(4):
                step_motor_down(stepSequenceCW[i], 8)
                step_motor_move(stepSequenceCW[i], 8)
            j += 1
        StopDown()
        PoChStrMove(SE - SA)
        
def ProtivDownProtivMove(SA, SE):
    j = 0
    if SA >= SE:
        while j < SE:
            for i in range(4):
                step_motor_down(stepSequenceCCW[i], 8)
                step_motor_move(stepSequenceCCW[i], 8)
            j += 1
        StopMove()
        ProtivChStrDown(SA-SE)
    elif SE > SA:
        while j < SA:
            for i in range(4):
                step_motor_down(stepSequenceCCW[i], 8)
                step_motor_move(stepSequenceCCW[i], 8)
            j += 1
        StopDown()
        ProtivChStrMove(SE-SA)


def PoDownProtivMove(SA, SE):
    j = 0
    if SA >= SE:
        while j < SE:
            for i in range(4):
                step_motor_down(stepSequenceCW[i], 8)
                step_motor_move(stepSequenceCCW[i], 8)
            j += 1
        StopMove()
        PoChStrDown(SA-SE)
    elif SE > SA:
        while j < SA:
            for i in range(4):
                step_motor_down(stepSequenceCW[i], 8)
                step_motor_move(stepSequenceCCW[i], 8)
            j += 1
        StopDown()
        ProtivChStrMove(SE-SA)


def ProtivDownPoMove(SA, SE):
    j = 0
    if SA >= SE:
        while j < SE:
            for i in range(4):
                step_motor_down(stepSequenceCCW[i], 8)
                step_motor_move(stepSequenceCW[i], 8)
            j += 1
        StopMove()
        ProtivChStrDown(SA-SE)
    elif SE > SA:
        while j < SA:
            for i in range(4):
                step_motor_down(stepSequenceCCW[i], 8)
                step_motor_move(stepSequenceCW[i], 8)
            j += 1
        StopDown()
        PoChStrMove(SE-SA)


# Возвращение в исхоную точку
def PointZeroDown(Azimut):
    k = 1
    while (k == 1):
        if Azimut > 0:
            ProtivChStrDown(Step(Azimut))
            k = 0
        elif Azimut < 0:
            PoChStrDown(Step(Azimut))
            k = 0
        else:
            StopDown() 
            k = 0
    StopDown()

# mya-mya


       
