# neko
## Поворотное устройство

Управление поворотным устройством состоит из 3-х уровней: нижний (rotator.py) - поворотное устройство с rpi pico 2, средний (manual control.py) - rpi 4, для принятия данных, верхний (biba.py) - ПК, для получения и обработки данных TLE

Диаграммка: 

<img width="692" height="508" alt="image" src="https://github.com/user-attachments/assets/9cfb959e-4a2d-4837-9d72-527a7f03fec0" />

1. Нижний уровень прошит в rpi pico
2. Для подключения к станции необходимо установить src на rpi4 и соединить rpi4 с rpi pico протоколом uart (rx-tx, tx-rx)
3. Дальнейшее управление производится с помощью подключения rpi4 к ПК по SSH.


Мем дня: 

<img width="736" height="696" alt="image" src="https://github.com/user-attachments/assets/b3324a6e-1960-4cf1-a75b-0061b8d8db6c" />


Мемы закончились...




