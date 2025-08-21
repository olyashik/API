from utils import in1, in2, in3, in4, in5, in6, in7,in8, stepSequenceCW, stepSequenceCCW
import time

# Функция для выполнения одного шага
def step_motor_move(step):
    in1.value(step[0])
    in2.value(step[1])
    in3.value(step[2])
    in4.value(step[3])
    time.sleep_ms(10)  # Задержка между шагами

# Функция для выполнения одного шага
def step_motor_down(step):
    in5.value(step[0])
    in6.value(step[1])
    in7.value(step[2])
    in8.value(step[3])
    time.sleep_ms(10)  # Задержка между шагами

# Остановка верхнего двигателя
def StopMove():
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    time.sleep_ms(5)  # Задержка

# Остановка нижнего двигателя
def StopDown():
    in5.value(0)
    in6.value(0)
    in7.value(0)
    in8.value(0)
    time.sleep_ms(5)  # Задержка

# Перевод из градусов в шаги
def Step(grad):
    return abs(grad * 2)

# Вращение нижнего двигателя по часовой стрелке
def PoChStrMove(steps1):
    j = 0
    while j < steps1:
        for i in range(4):
            step_motor_move(stepSequenceCW[i])
            step_motor_move(stepSequenceCCW[i])
        j += 1
        
# Вращение нижнего двигателя против часовой стрелки
def ProtivChStrMove(steps1):
    j = 0
    while j < steps1:
        for i in range(4):
            step_motor_move(stepSequenceCCW[i])
            step_motor_move(stepSequenceCW[i])
        j += 1

# Вращение нижнего двигателя по часовой стрелке
def PoChStrDown(steps1):
    j = 0
    while j < steps1:
        for i in range(4):
            step_motor_down(stepSequenceCW[i])
            step_motor_move(stepSequenceCCW[i])
        j += 1

# Вращение нижнего двигателя против часовой стрелки
def ProtivChStrDown(steps1):
    j = 0
    while j < steps1:
        for i in range(4):
            step_motor_down(stepSequenceCCW[i])
            step_motor_move(stepSequenceCW[i])
        j += 1

