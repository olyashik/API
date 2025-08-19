# Тут могла бы быть реклама вашего кота, но вы так и не скинули его фото
import sys

if __name__ == "__main__":
    data = sys.argv[1] if len(sys.argv) > 1 else None
    if data:
        print(f"Получены данные: {data}")
