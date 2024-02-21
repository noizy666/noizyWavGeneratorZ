import random
import headerz
import shlex, subprocess

hexChars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]

# Generating random filename
filename = f'{"".join([random.choice(hexChars) for i in range(0,20)]).upper()}.wav'

# Rewriting xxd command with shlex to reverse hexdump to mp3
command = shlex.split(f"xxd -r -p {filename}.hex {filename}")

# Creating file
with open(f"{filename}.hex", "x") as f:
    f.close()

# Writing Header
with open(f"{filename}.hex", "a") as f:
    f.write(f"{headerz._wav_head}\n")

    for i in range(0,99991):
        randomHexString = f'{"".join([random.choice(hexChars) for i in range(0,60)]).upper()}\n'
        f.write(randomHexString)

# Transforming hexdata into wav
exitcode = subprocess.call(command)

print(exitcode)