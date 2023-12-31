import sys
import pyautogui as py
from time import sleep
import customtkinter
import random

class bot:
  
  def selecionarJogador(jogadorX, jogadorY, últimos, reportText):
    
    if últimos:
      py.rightClick(jogadorX, jogadorY, duration=0.1)
      py.click(jogadorX + 30, jogadorY - 30, duration=0.1)
      bot.fazerDenúncia(reportText)
    else:
      py.rightClick(jogadorX, jogadorY, duration=0.1)
      py.click(jogadorX + 30, jogadorY + 130, duration=0.1)
      bot.fazerDenúncia(reportText)

  def fazerDenúncia(reportText):
    
    py.click(760, 356, duration=0.1)
    py.click(760, 403, duration=0.1)
    py.click(760, 477, duration=0.1)
    py.click(760, 524, duration=0.1)
    py.click(760, 568, duration=0.1)
    py.click(760, 611, duration=0.1)
    py.click(760, 674, duration=0.1)
    if reportText:
      py.press('tab')
      py.write(reportText)
      sleep(0.3)
    py.click(965, 800, duration=0.1)
  
  def main(p1, p2, p3, p4, p5, p6, p7, p8, p9, reportText):
    
    global fraseAleatória
    fraseAleatória.destroy()
    fraseAleatória = customtkinter.CTkLabel(mainFrame, text=f"Bot tá pocando 😎\nSE DER PROBLEMA APERTE WIN+L", font=('Roboto', 12, 'bold'), text_color='yellow')
    fraseAleatória.grid(row=0, columnspan=2, padx=10, pady=15)
    root.update()
    
    py.click(1260, 830)
    #aliados
    if p1.get():
      bot.selecionarJogador(586, 477, False, reportText) #1
    if p2.get():
      bot.selecionarJogador(586, 514, False, reportText) #2
    if p3.get():
      bot.selecionarJogador(586, 551, False, reportText) #3
    if p4.get():
      bot.selecionarJogador(586, 584, False, reportText) #4
    
    #inimigos
    if p5.get():
      bot.selecionarJogador(586, 660, False, reportText) #1
    if p6.get():
      bot.selecionarJogador(586, 694, False, reportText) #2
    if p7.get():
      bot.selecionarJogador(586, 731, True, reportText) #3
    if p8.get():
      bot.selecionarJogador(586, 763, True, reportText) #4
    if p9.get():
      bot.selecionarJogador(586, 800, True, reportText) #5

    fraseAleatória.configure(text=f"Bot já cabo 😎", text_color='green')

class misc:
  
  def sair():
    sys.exit()
  
  def checkRes(largura, altura):
    if f'{largura/altura:.2f}' != '1.78' or (largura < 1366 and altura < 768):
      views.resError()
    else:      
      pass
      
  def checkFill(p1:bool, p2:bool, p3:bool, p4:bool, p5:bool, p6:bool, p7:bool, p8:bool, p9:bool, reportText:str):
    if (p1.get() or p2.get() or p3.get() or p4.get() or p5.get() or p6.get() or p7.get() or p8.get() or p9.get()):
      views.startBot(p1, p2, p3, p4, p5, p6, p7, p8, p9, reportText)
    else:
      views.fillError()
      
class views:
  
  def startBot(p1, p2, p3, p4, p5, p6, p7, p8, p9, reportText):
    
    root.wm_minsize(300, 200)
    root.wm_maxsize(300, 200)
    
    global mainFrame
    mainFrame.destroy()
    
    mainFrame = customtkinter.CTkFrame(root, corner_radius=20, border_width=2)
    mainFrame.place(relx=0.5, rely=0.5, anchor='center')
    
    global fraseAleatória
    fraseAleatória = customtkinter.CTkLabel(mainFrame, text=f"eai 😎\nSE DER PROBLEMA APERTE WIN+L", font=('Roboto', 12, 'bold'), text_color='white')
    fraseAleatória.grid(row=0, columnspan=2, padx=10, pady=15)
    
    customtkinter.CTkButton(mainFrame, text="Voltar", font=('Roboto', 14, 'bold'), cursor='hand2', command=views.configureBot, width=60).grid(row=1, column=0, padx=10, pady=15)
    customtkinter.CTkButton(mainFrame, text="Iniciar bot 🤖", font=('Roboto', 14, 'bold'), cursor='hand2', command=lambda:bot.main(p1, p2, p3, p4, p5, p6, p7, p8, p9, reportText), width=60).grid(row=1, column=1, padx=10, pady=15)
  
  def fillError():
    global fraseAleatória
    fraseAleatória.destroy()
    fraseAleatória = customtkinter.CTkLabel(mainFrame, text=f"Preencha os campos corretamente 😎", font=('Roboto', 12, 'bold'), text_color='red')
    fraseAleatória.grid(row=11, columnspan=2, pady=5)
  
  def resError():
    global fraseAleatória
    customtkinter.CTkLabel(mainFrame, text='Ocorreu um erro ⚠️', text_color='white', font=('Roboto', 40, 'bold')).pack(padx=20, pady=20)
    customtkinter.CTkLabel(mainFrame, text=f'A resolução do seu monitor: {largura}x{altura} não é suportada.\nVocê pode entrar em contato comigo pra ver se da pra dar um jeito pelo email abaixo:\nsamu.barreto2004@gmail.com', text_color='red', font=('Roboto', 16, 'bold')).pack(padx=20, pady=20)
    
    customtkinter.CTkButton(mainFrame, text="Tendi man :/", font=('Roboto', 16, 'bold'), cursor='hand2', command=misc.sair).pack(pady=20)
    fraseAleatória = customtkinter.CTkLabel(mainFrame, text=f"eai 😎", font=('Roboto', 12, 'bold'), text_color='red')
    fraseAleatória.pack(pady=5, padx=20)
  
  def configureBot():
    
    global mainFrame
    mainFrame.destroy()
    
    root.wm_minsize(800, 700)
    root.wm_maxsize(800, 700)
    
    mainFrame = customtkinter.CTkFrame(root, corner_radius=20, border_width=2)
    mainFrame.place(relx=0.5, rely=0.5, anchor='center')
    
    global altura, largura
    largura = root.winfo_screenwidth()
    altura = root.winfo_screenheight()
    misc.checkRes(largura, altura)
    
    player1 = customtkinter.BooleanVar()
    player2 = customtkinter.BooleanVar()
    player3 = customtkinter.BooleanVar()
    player4 = customtkinter.BooleanVar()
    player5 = customtkinter.BooleanVar()
    player6 = customtkinter.BooleanVar()
    player7 = customtkinter.BooleanVar()
    player8 = customtkinter.BooleanVar()
    player9 = customtkinter.BooleanVar()

    player1.set(True)
    player2.set(True)
    player3.set(True)
    player4.set(True)
    player5.set(True)
    player6.set(True)
    player7.set(True)
    player8.set(True)
    player9.set(True)

    customtkinter.CTkLabel(mainFrame, text='Configurar bot 🤖', text_color='white', font=('Roboto', 40, 'bold')).grid(row=0, columnspan=2, padx=20, pady=15)
    
    customtkinter.CTkLabel(mainFrame, text='Reportar jogadores:', text_color='white',font=('Roboto', 18, 'bold')).grid(row=1, columnspan=2)
    
    customtkinter.CTkCheckBox(mainFrame, text='Aliado 1', text_color='white', font=('Roboto', 16, 'bold'), variable=player1).grid(row=2, column=0, pady=10)
    customtkinter.CTkCheckBox(mainFrame, text='Aliado 2', text_color='white', font=('Roboto', 16, 'bold'), variable=player2).grid(row=3, column=0, pady=10)
    customtkinter.CTkCheckBox(mainFrame, text='Aliado 3', text_color='white', font=('Roboto', 16, 'bold'), variable=player3).grid(row=4, column=0, pady=10)
    customtkinter.CTkCheckBox(mainFrame, text='Aliado 4', text_color='white', font=('Roboto', 16, 'bold'), variable=player4).grid(row=5, column=0, pady=10)
    customtkinter.CTkCheckBox(mainFrame, text='Oponente 1', text_color='white', font=('Roboto', 16, 'bold'), variable=player5).grid(row=2, column=1, pady=10)
    customtkinter.CTkCheckBox(mainFrame, text='Oponente 2', text_color='white', font=('Roboto', 16, 'bold'), variable=player6).grid(row=3, column=1, pady=10)
    customtkinter.CTkCheckBox(mainFrame, text='Oponente 3', text_color='white', font=('Roboto', 16, 'bold'), variable=player7).grid(row=4, column=1, pady=10)
    customtkinter.CTkCheckBox(mainFrame, text='Oponente 4', text_color='white', font=('Roboto', 16, 'bold'), variable=player8).grid(row=5, column=1, pady=10)
    customtkinter.CTkCheckBox(mainFrame, text='Oponente 5', text_color='white', font=('Roboto', 16, 'bold'), variable=player9).grid(row=6, column=1, pady=10)

    customtkinter.CTkLabel(mainFrame, text='Texto do report, deixe vazio para\nnão escrever nada:', text_color='white', font=('Roboto', 18, 'bold')).grid(row=7, columnspan=2)
    
    reportText = customtkinter.StringVar()
    customtkinter.CTkEntry(mainFrame, text_color='white', font=('Roboto', 16, 'bold'), width=320, height=50, textvariable=reportText).grid(row=8, pady=10, columnspan=2)
    
    customtkinter.CTkButton(mainFrame, text="Finalizar configuração", font=('Roboto', 16, 'bold' ), cursor='hand2', width=320, height=45, command=lambda: misc.checkFill(player1, player2, player3, player4, player5, player6, player7, player8, player9, reportText.get())).grid(row=10, columnspan=2, pady=10)

    global fraseAleatória
    fraseAleatória = customtkinter.CTkLabel(mainFrame, text=f"eai 😎", font=('Roboto', 12, 'bold'), text_color='green')
    fraseAleatória.grid(row=11, columnspan=2, pady=5)

if __name__ == '__main__':
  
  root = customtkinter.CTk()

  root.wm_title('reportLeague')

  customtkinter.set_appearance_mode('dark')
  customtkinter.set_default_color_theme('green')
  root.wm_minsize(800, 700)
  root.wm_maxsize(800, 700)
  
  mainFrame = customtkinter.CTkFrame(root, corner_radius=20, border_width=2)
  mainFrame.place(relx=0.5, rely=0.5, anchor='center')
  
  h1 = customtkinter.CTkLabel(mainFrame, text='Avisos importantes ⚠️', text_color='white', font=('Roboto', 40, 'bold')).pack(padx=20, pady=10)

  customtkinter.CTkLabel(mainFrame, text_color='white', font=('Roboto', 16, 'bold'), text='1. Não use seu mouse nem teclado durante a ação do bot.').pack(padx=20, pady=10)
  customtkinter.CTkLabel(mainFrame, text_color='white', font=('Roboto', 16, 'bold'), text='2. Nas configurações do cliente do lol selecione a resolução 1280x720.').pack(padx=20, pady=10)
  customtkinter.CTkLabel(mainFrame, text_color='white', font=('Roboto', 16, 'bold'), text='3. Não use o bot na tela de fim de jogo, use pelo seu histórico de partidas.').pack(padx=20, pady=10)
  customtkinter.CTkLabel(mainFrame, text_color='white', font=('Roboto', 16, 'bold'), text='4. Se der QUALQUER problema, use o atalho: WIN+L pra parar o bot.').pack(padx=20, pady=10)
  customtkinter.CTkLabel(mainFrame, text_color='white', font=('Roboto', 16, 'bold'), text='5. O programa NÃO da suporte para monitores com proporções diferentes de 16:9.').pack(padx=20, pady=10)
  customtkinter.CTkLabel(mainFrame, text_color='white', font=('Roboto', 16, 'bold'), text='6. O programa NÃO da suporte para resoluções menores que 1366x768.').pack(padx=20, pady=10)
  customtkinter.CTkLabel(mainFrame, text_color='white', font=('Roboto', 16, 'bold'), text='7. Não mova a janela do cliente do jogo, deixe ele centralizado, como padrão.').pack(padx=20, pady=10)
  customtkinter.CTkLabel(mainFrame, text_color='white', font=('Roboto', 16, 'bold'), text='8. Caso você tenha mais de um monitor, eu não sei o que vai acontecer, tente por sua conta e risco.\nQualquer coisa aperte WIN+L pra parar o bot').pack(padx=20, pady=10)
  
  customtkinter.CTkButton(mainFrame, text="Vambora", font=('Roboto', 16, 'bold'), cursor='hand2', command=views.configureBot).pack(pady=10)
  
  fraseAleatória = customtkinter.CTkLabel(mainFrame, text=f"eai 😎", font=('Roboto', 12, 'bold'), text_color='green')
  fraseAleatória.pack(pady=5, padx=20)

  root.mainloop()
