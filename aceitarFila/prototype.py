import pyautogui as py
from time import sleep
import sys, subprocess

def clearTerminal():
  os = sys.platform
  
  if os == 'win32':
    subprocess.run('cls', shell=True)
  elif os == 'linux' or os == 'darwin':
    subprocess.run('clear', shell=True)

print(f'''\n·=======· Na fila ·=======· :)''')

while True:
  local = py.locateOnScreen('accept.png', confidence=0.65)
  
  if local != None:
    clearTerminal()
    print(f'''\n·=======· Partida encontrada ·=======· :)''')
    py.click(local)
    sleep(10)
    clearTerminal()
    print(f'''\n·=======· Na fila ·=======· :)''')

  else:
    sleep(.5)