import pyautogui as py
from time import sleep
import customtkinter
import threading

executar_bot = False
bot_thread = None

root = customtkinter.CTk()

root.wm_minsize(300, 300)
root.wm_maxsize(300, 300)

root.wm_title('Autoclick 🫵')

customtkinter.set_appearance_mode('dark')

def startBot():
    global executar_bot
    global bot_thread

    executar_bot = True

    fraseAleatória.configure(text=f"bot tá funcionando 😎", text_color='green')
    butão.configure(fg_color='red', hover_color='darkred', text='Parar bot', command=stopBot)
    root.update()

    sleep(1)
    bot_thread = threading.Thread(target=bot_logic)
    bot_thread.start()

def bot_logic():
    while executar_bot:
        py.click()

def stopBot():
    global executar_bot
    global bot_thread

    executar_bot = False
    bot_thread.join()

    fraseAleatória.configure(text=f"eai amigo 😎", font=('Roboto', 12, 'bold'), text_color='white')
    butão.configure(text='Iniciar bot', command=startBot, font=('Roboto', 16, 'bold'), fg_color='green', hover_color='darkgreen')

mainFrame = customtkinter.CTkFrame(root, corner_radius=20, border_width=2)
mainFrame.place(relx=0.5, rely=0.5, anchor='center')

butão = customtkinter.CTkButton(mainFrame, text='Iniciar bot', command=startBot, font=('Roboto', 16, 'bold'), fg_color='green', hover_color='darkgreen')
butão.pack(padx=10, pady=10)

fraseAleatória = customtkinter.CTkLabel(mainFrame, text=f"eai amigo 😎", font=('Roboto', 12, 'bold'), text_color='white')
fraseAleatória.pack(padx=10, pady=10)

root.mainloop()
