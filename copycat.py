# mur
import biba # убрать данную строчку, если нет biba.py
# Начальная точка
azimut0 = 0
elev0 = 0

while True:
        print("Elevation and Azimut, kudasai...\n")
        try:
          elev, azimut = map(int, input().split())
          if elev == 91 and azimut == 361:
            print("Point zero (＾• ω •＾)!!!\n")
            tx = "Point zero"
          elif abs(elev) > 91 or abs(azimut) > 361:
            print("Error (〃＞＿＜;〃)\n")
            tx = "error"
          elif (elev<91 and azimut<361):
            print("mya-mya")
            tx = "Go"
            if (elev>0) and (azimut>0):
                ttx = "PoPo"
            elif (elev<0) and (azimut<0):
                ttx = "ProtivProtiv"
            elif (elev>0) and (azimut<0):
                ttx = "PoProtiv"
            elif (elev<0) and (azimut>0):
                ttx = "ProtivPo"
            elev0 = elev
            azimut0 = azimut
        except ValueError:
          print("Error! Need new numbers")
        except Exception as e:
          print("Error! Uncorrect")
