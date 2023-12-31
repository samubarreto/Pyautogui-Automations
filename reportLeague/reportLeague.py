import pyautogui as py
from time import sleep
import random

def selecionarJogador(jogadorX, jogadorY, últimos):
  if últimos:
    py.rightClick(jogadorX, jogadorY, duration=0.15)
    py.click(jogadorX+30, jogadorY-30, duration=0.15)
    fazerDenúncia()
  else:
    py.rightClick(jogadorX, jogadorY, duration=0.15)
    py.click(jogadorX+50, jogadorY+130, duration=0.15)
    fazerDenúncia()

def fazerDenúncia():
  py.click(760, 356, duration=0.1)
  py.click(760, 403, duration=0.1)
  py.click(760, 477, duration=0.1)
  py.click(760, 524, duration=0.1)
  py.click(760, 568, duration=0.1)
  py.click(760, 611, duration=0.1)
  py.click(760, 674, duration=0.1)
  py.press('tab')
  py.write('escreva aqui o report')
  sleep(1)
  py.click(965, 800, duration=0.1)

if __name__ == '__main__':
  #aliados
  selecionarJogador(586, 477, False) #1
  #selecionarJogador(586, 514, False) #2
  selecionarJogador(586, 551, False) #3
  selecionarJogador(586, 584, False) #4
  
  #inimigos
  selecionarJogador(586, 660, False) #1
  selecionarJogador(586, 694, False) #2
  selecionarJogador(586, 731, True) #3
  selecionarJogador(586, 763, True) #4
  selecionarJogador(586, 800, True) #5
  