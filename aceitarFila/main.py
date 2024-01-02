import pyautogui as py
from time import sleep

c = 0

while True:
  local = py.locateOnScreen('accept.png', confidence=0.6, grayscale=True)
  
  if local != None:
    print(f'Partida encontrada.')
    py.click(local, duration=0.2)
    # for i in range(16):
    #   print(f'Partida encontrada. Aguardando confirmação dos outros jogadores. ({i+1}/16)')
    #   sleep(1)
    # local = py.locateOnScreen('accept.png', confidence=0.6, grayscale=True)
    # if local != None:
    #   print(f'Partida recusada por outro jogador. Voltando para fila')
    # else:
    #   print(f'Partida confirmada. Tenha um bom jogo =)')
    #   break

  else:
    print(f'Na fila ({c})'); sleep(.5)
    c += 1

    