import pyautogui as py
from time import sleep

c = 1; x = 1
while True:
  
  local = py.locateOnScreen('x.png', confidence=0.6, grayscale=True)
  
  if local != None:
    x = 1
    print(f'{c} comments were deleted.')
    py.click(837, local[1]+25, duration=0.2)
    sleep(0.2)
    c += 1
    if c % 2 == 0:
      py.press('down')

  else:
    print(f'X button not found. ({x})'); x += 1
    py.press('down')
  