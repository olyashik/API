import base_commands

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

