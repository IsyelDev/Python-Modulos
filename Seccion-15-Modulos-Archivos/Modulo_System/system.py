import sys
from datetime import datetime 


sys.stdout.write("Hola mundi desde std out")
sys.stderr.write("Hola mundi desde std out")
print("Hola mundo")

try:
    date_Event = datetime.strptime("2026-09-18","%Y-%m-%d")
    print(date_Event)
except ValueError:
    sys.stderr.write("Error con el formato fecha")
    sys.exit(1)

print("Otra tarea")
sys.exit(0)


