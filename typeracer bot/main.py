import pyautogui as py
from time import sleep
import random
import customtkinter
import threading
import unidecode
  
def oneWord():

  palavra = palavraTextbox.get("0.0", "end")
  sleep(1)

  while True:
    for letra in palavra:
      py.write(letra)
    py.press('space')

def numbersAndEngPhrase():
  
  palavra = palavraTextbox.get("0.0", "end")
  sleep(1)

  for letra in palavra:
    py.write(letra)

if __name__ == '__main__':
  executar_bot = False

  root = customtkinter.CTk()

  root.wm_minsize(350, 210)
  root.wm_maxsize(350, 210)

  root.wm_title('typeracer')

  customtkinter.set_appearance_mode('dark')
    
  mainFrame = customtkinter.CTkFrame(root, corner_radius=20, border_width=2)
  mainFrame.place(relx=0.5, rely=0.5, anchor='center')
    
  palavraTextbox = customtkinter.CTkTextbox(mainFrame, height=90, width=300, )
  palavraTextbox.pack(padx=10, pady=10)

  startButton = customtkinter.CTkButton(mainFrame, text='Iniciar', command=numbersAndEngPhrase).pack(padx=20, pady=10)

  root.mainloop()