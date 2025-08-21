import utils
from base_commands import ProtivChStrMove, PoChStrMove, PoChStrDown, ProtivChStrDown, Step, StopMove, StopDown, step_motor_down, step_motor_move
from machine import UART, Pin

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
                step_motor_down(utils.stepSequenceCW[i])
                step_motor_move(utils.stepSequenceCW[i])
            j += 1
        StopMove()
        PoChStrDown(SA - SE)

    elif SE > SA:
        while j < SA:
            for i in range(4):
                step_motor_down(utils.stepSequenceCW[i])
                step_motor_move(utils.stepSequenceCW[i])
            j += 1
        StopDown()
        PoChStrMove(SE - SA)


def ProtivDownProtivMove(SA, SE):
    j = 0
    if SA >= SE:
        while j < SE:
            for i in range(4):
                step_motor_down(utils.stepSequenceCCW[i])
                step_motor_move(utils.stepSequenceCCW[i])
            j += 1
        StopMove()
        ProtivChStrDown(SA - SE)
    elif SE > SA:
        while j < SA:
            for i in range(4):
                step_motor_down(utils.stepSequenceCCW[i])
                step_motor_move(utils.stepSequenceCCW[i])
            j += 1
        StopDown()
        ProtivChStrMove(SE - SA)


def PoDownProtivMove(SA, SE):
    j = 0
    if SA >= SE:
        while j < SE:
            for i in range(4):
                step_motor_down(utils.stepSequenceCW[i])
                step_motor_move(utils.stepSequenceCCW[i])
            j += 1
        StopMove()
        PoChStrDown(SA - SE)
    elif SE > SA:
        while j < SA:
            for i in range(4):
                step_motor_down(utils.stepSequenceCW[i])
                step_motor_move(utils.stepSequenceCCW[i])
            j += 1
        StopDown()
        ProtivChStrMove(SE - SA)


def ProtivDownPoMove(SA, SE):
    j = 0
    if SA >= SE:
        while j < SE:
            for i in range(4):
                step_motor_down(utils.stepSequenceCCW[i])
                step_motor_move(utils.stepSequenceCW[i])
            j += 1
        StopMove()
        ProtivChStrDown(SA - SE)
    elif SE > SA:
        while j < SA:
            for i in range(4):
                step_motor_down(utils.stepSequenceCCW[i])
                step_motor_move(utils.stepSequenceCW[i])
            j += 1
        StopDown()
        PoChStrMove(SE - SA)


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

def where(E, A):
    if (elev>0) and (azimut>0):
        PoDownPoMove(Step(A), Step(E))
    elif (elev<0) and (azimut<0):
        ProtivDownProtivMove(Step(A), Step(E))
    elif (elev>0) and (azimut<0):
        PoDownProtivMove(Step(A), Step(E))
    elif (elev<0) and (azimut>0):
        ProtivDownPoMove(Step(A), Step(E))
    StopMove()
    StopDown()

# mya-mya
uart = UART(0, 115200, tx=Pin(0), rx=Pin(1))

if uart.any():
    data =uart.readline()
    azimut, elev = data.split()
    if azimut == 361 and elev == 91:
        PointZeroDown(azimut)
        PointZeroMove(elev)
    else:
        where(elev, azimut)


