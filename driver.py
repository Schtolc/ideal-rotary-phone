import psutil
import subprocess
import random
import sys

subprocess.Popen(['pkill', 'SCREEN'])
subprocess.Popen(['screen', '-d', '-m', '/dev/cu.SLAB_USBtoUART'])

while True:
    try:
        cpu = int(psutil.cpu_percent(interval=5))
        ram = int(psutil.virtual_memory().percent)
        net = random.randrange(100, 126)
        output = '{} {} {}$'.format(cpu, ram, net)
        print(output)
        subprocess.Popen(['screen', '-p', '0', '-X', 'stuff', output])
    except KeyboardInterrupt:
        sys.exit(0)
