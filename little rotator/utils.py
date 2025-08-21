from machine import Pin

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
