import subprocess
import time

def run_adb_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return result.stderr.strip()
    except Exception as e:
        return str(e)

# Read adb commands from the text file
with open('adb_commands.txt', 'r') as file:
    adb_commands = file.read().splitlines()

delay_seconds = 3  # Adjust the delay time as needed

for command in adb_commands:
    output = run_adb_command(command)
    print(f"Command: {command}\nOutput:\n{output}\n{'='*30}")
    
    # Introduce a delay between commands
    time.sleep(delay_seconds)

