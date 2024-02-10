import pyautogui as py
from time import sleep
import random
import customtkinter
import threading
import unidecode
  
song = '''música...
aq...'''
  
def lyric():
  sleep(1)
  letra = letraTextbox.get("0.0", "end")
  letraTratada = unidecode.unidecode(letra)
  letraSplitada = letraTratada.split('...')
  
  for linha in letraSplitada:
    py.write(linha)

if __name__ == '__main__':
  executar_bot = False

  root = customtkinter.CTk()

  root.wm_minsize(350, 210)
  root.wm_maxsize(350, 210)

  root.wm_title('msc')

  customtkinter.set_appearance_mode('dark')
    
  mainFrame = customtkinter.CTkFrame(root, corner_radius=20, border_width=2)
  mainFrame.place(relx=0.5, rely=0.5, anchor='center')
    
  letraTextbox = customtkinter.CTkTextbox(mainFrame, height=90, width=300)
  letraTextbox.pack(padx=10, pady=10)

  startButton = customtkinter.CTkButton(mainFrame, text='Iniciar', command=lyric).pack(padx=20, pady=10)

  root.mainloop()