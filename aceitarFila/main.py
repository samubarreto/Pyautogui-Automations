import pyautogui as py
from time import sleep
from random import randint

print(f'Na fila')

while True:
  local = py.locateOnScreen('accept.png', confidence=0.6  )
  
  if local != None:
    print(f'Partida encontrada')
    py.click(local)
    sleep(10); print('Na fila')

  else:
    sleep(.5)
    