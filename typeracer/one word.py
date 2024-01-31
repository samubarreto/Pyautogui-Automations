import pyautogui as py
import customtkinter
from time import sleep

def startBot():
  sleep(1)
  palavra = palavraVar.get()
  
  while True:
    for letra in palavra:
      py.write(letra)
    py.press('space')

root = customtkinter.CTk()

root.wm_title('one word typeracer')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

mainFrame = customtkinter.CTkFrame(root, corner_radius=20, border_width=2)
mainFrame.place(relx=0.5, rely=0.5, anchor='center')

palavraVar = customtkinter.StringVar()

customtkinter.CTkEntry(mainFrame, textvariable=palavraVar).pack(padx=10, pady=10)

customtkinter.CTkButton(mainFrame, text="Começar", font=('Roboto', 16, 'bold'), cursor='hand2', command=startBot).pack(pady=10)

fraseAleatória = customtkinter.CTkLabel(mainFrame, text=f"eai 😎", font=('Roboto', 12, 'bold'), text_color='green')
fraseAleatória.pack(pady=5, padx=20)

root.mainloop()