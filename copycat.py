# mur
import main

# Начальная точка
azimut0 = 0
elev0 = 0

while True:
        print("Elevation and Azimut, kudasai...\n")
        try:
          elev, azimut = map(int, input().split())
          if elev == 91 and azimut == 361:
            print("Point zero (＾• ω •＾)!!!\n")
            main.PointZeroDown(azimut0)
            main.PointZeroMove(elev0)
          elif abs(elev) > 91 or abs(azimut) > 361:
            print("Error (〃＞＿＜;〃)\n")
          elif (elev<91 and azimut<361):
            print("mya-mya")
            main.where(elev - elev0, azimut - azimut0)
            elev0 = elev
            azimut0 = azimut
        except ValueError:
          print("Error! Need new numbers")
        except Exception as e:
          print("Error! Uncorrect")
