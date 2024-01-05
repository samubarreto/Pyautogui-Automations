import pyautogui as py
from time import sleep

c = 0

while True:
  local = py.locateOnScreen('accept.png', confidence=0.6, grayscale=True)
  
  if local != None:
    print(f'Partida encontrada.')
    py.click(local, duration=0.2)
    sleep(14); print('Voltando pra fila.'); print(1)

  else:
    print(f'Na fila ({c})'); sleep(.5)
    c += 1
