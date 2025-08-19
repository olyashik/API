import subprocess

def send_data_to_pi(data):
    command = f'ssh superstation@superstation.local "python3 /path/to/script_on_pi.py {data}"'
    subprocess.run(command, shell=True, check=True)

sshmind(input())