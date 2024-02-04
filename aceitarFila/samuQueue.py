import pyautogui as py
from time import sleep
import customtkinter
import threading

executar_bot = False
bot_thread = None

root = customtkinter.CTk()

root.iconbitmap('favicon.ico')
root.wm_minsize(200, 100)
root.wm_maxsize(200, 100)
root.wm_title('')

customtkinter.set_appearance_mode('dark')

def matchFound(local):
  py.click(local)
  status.configure(text=f"partida encontrada 😎", text_color='white')
  butão.configure(fg_color='orange', hover_color='darkorange', text='Aguarde')
  root.update(); sleep(5)

def botLogic():
  while executar_bot:
    
    status.configure(text=f"na fila 😎", text_color='white')
    butão.configure(fg_color='red', hover_color='darkred', text='Sair da fila', command=stopBot)
    root.update()
    
    local = py.locateOnScreen('accept.png', confidence=0.65)
    if local != None:
      matchFound(local)

def startBot():
  global executar_bot
  global bot_thread

  executar_bot = True

  status.configure(text=f"na fila 😎", text_color='white')
  butão.configure(fg_color='red', hover_color='darkred', text='Sair da fila', command=stopBot)
  root.update()

  bot_thread = threading.Thread(target=botLogic)
  bot_thread.start()

def stopBot():
  global executar_bot
  global bot_thread

  executar_bot = False
  bot_thread.join()

  status.configure(text=f"idle 😎", font=('Roboto', 12, 'bold'), text_color='white')
  butão.configure(text='Entrar na fila', command=startBot, font=('Roboto', 16, 'bold'), fg_color='green', hover_color='darkgreen')

frame1 = customtkinter.CTkFrame(root, corner_radius=20, border_width=2)
frame1.place(relx=0.5, rely=0.65, anchor='center')

butão = customtkinter.CTkButton(frame1, text='Entrar na fila', command=startBot, font=('Roboto', 16, 'bold'), fg_color='green', hover_color='darkgreen')
butão.pack(padx=12, pady=8)

status = customtkinter.CTkLabel(root, text=f"idle 😎", font=('Roboto', 12, 'bold'), text_color='white')
status.pack(padx=10, pady=10)

root.mainloop()