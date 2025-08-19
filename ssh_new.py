import paramiko

def execute_command(hostname, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    client.close()
    return output

# Пример использования:
hostname = "192.168.1.100"  # Замените на IP адрес вашего Raspberry Pi
username = "superstation"   # Замените на имя пользователя Raspberry Pi
password = "your_password"  # Замените на пароль пользователя
command = "python3 /path/to/your/script.py" # Путь к Python скрипту на Raspberry Pi
result = execute_command(hostname, username, password, command)
print(result)