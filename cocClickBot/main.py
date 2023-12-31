#I recommend playing via an android emulator

import pyautogui as py
from random import randint
from time import sleep
  
def clickHere(file, cooldown):
  
  local = py.locateOnScreen(f'{file}.png', confidence=0.6, grayscale=True)

  while True:
    
    if local != None:
      if file == 'nextImg':
        py.click(local[0] + (local[2] +5), local[1] - 30, duration=0.2)
        sleep(cooldown)
        break
        
      else:
        py.click(local[0] + randint(1, local[2]), local[1] + randint(1, local[3]))
        sleep(cooldown)
        break
    
    else:
      py.alert(f'File "{file}" not found. Please, rerun the program and try again')
      exit()

if __name__ == '__main__':

  loopQuantity = int(input('How many times do you want the bot to run? R: '))
  
  for _ in range(loopQuantity):
  
    #1 attack
    clickHere('attackImg', randint(1, 3))
    
    # search opponent
    clickHere('searchImg', randint(7, 10))
      
    #2 select hero
    clickHere('queenImg', 0.5)

    #3 place hero
    clickHere('nextImg', 0.5)

    #4 surrender
    clickHere('surrenderImg', 0.5)

    #5 accept
    clickHere('okImg', 0.5)

    #6 confirm
    clickHere('backImg', 4)
    
  print('Bot loop ended.')
