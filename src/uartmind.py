import serial
import biba

azimut0 = 0
elev0 = 0

ser = serial.Serial('/dev/ttuACM0', 115200, timeout=1)

while True:
        print("Elevation and Azimut, kudasai...\n")
        try:
          elev, azimut = biba.data.split()
          if (elev == 91 and azimut == 361):
            print("Point (＾• ω •＾)!!!\n")
            data_string = f"{azimut0},{elev0}\n"
            # Отправляем данные
            ser.write(data_string.encode('utf-8'))
          elif (abs(azimut)<361 and abs(elev)<91):
              data_string = f"{azimut0-azimut},{elev0-elev}\n"
              # Отправляем данные
              ser.write(data_string.encode('utf-8'))
        except ValueError:
          print("Error! Need new numbers")
        except Exception as e:
          print("Error! Uncorrect")
