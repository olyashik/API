from machine import Pin
import time

# Настройка пинов (Низ)
in1 = Pin(10, Pin.OUT)  # IN1
in2 = Pin(11, Pin.OUT)  # IN2
in3 = Pin(12, Pin.OUT)  # IN3
in4 = Pin(13, Pin.OUT)  # IN4

# Настройка пинов (Верх)
in5 = Pin(2, Pin.OUT)  # IN1
in6 = Pin(3, Pin.OUT)  # IN2
in7 = Pin(4, Pin.OUT)  # IN3
in8 = Pin(5, Pin.OUT)  # IN4

# Последовательность шагов для движения по часовой стрелке
stepSequenceCW = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1]
]
# Последовательность шагов для движения против часовой стрелки
stepSequenceCCW = [
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]

# Функция для выполнения одного шага
def step_motor_move(step, Time):
    in1.value(step[0])
    in2.value(step[1])
    in3.value(step[2])
    in4.value(step[3])
    time.sleep_ms(Time)  # Задержка между шагами

# Функция для выполнения одного шага
def step_motor_down(step, Time):
    in5.value(step[0])
    in6.value(step[1])
    in7.value(step[2])
    in8.value(step[3])
    time.sleep_ms(Time)  # Задержка между шагами

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
            step_motor_move(stepSequenceCW[i], 12)
        j += 1
        
# Вращение нижнего двигателя против часовой стрелки
def ProtivChStrMove(steps1):
    j = 0
    while j < steps1:
        for i in range(4):
            step_motor_move(stepSequenceCCW[i], 12)
        j += 1

# Вращение нижнего двигателя по часовой стрелке
def PoChStrDown(steps1):
    j = 0
    while j < steps1:
        for i in range(4):
            step_motor_down(stepSequenceCW[i], 12)
        j += 1

# Вращение нижнего двигателя против часовой стрелки
def ProtivChStrDown(steps1):
    j = 0
    while j < steps1:
        for i in range(4):
            step_motor_down(stepSequenceCCW[i], 12)
        j += 1

