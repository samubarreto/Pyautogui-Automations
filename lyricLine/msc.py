import pyautogui as py
from time import sleep
import random
import customtkinter
import threading
import unidecode

'''I'm at a payphone trying to call home
All of my change I spent on you
Where have the times gone? Baby, it's all wrong
Where are the plans we made for two?

Yeah, I, I know it's hard to remember
The people we used to be
It's even harder to picture
That you're not here next to me
You say it's too late to make it
But is it too late to try?
And in or time that you wasted
All of our bridges burned down

I've wasted my nights
You turned out the lights
Now I'm paralyzed
Still stuck in that time when we called it love
But even the Sun sets in paradise

I'm at a payphone trying to call home
All of my change I spent on you
Where have the times gone? Baby, it's all wrong
Where are the plans we made for two?

If happy ever after did exist
I would still be holding you like this
All those fairy tales are full of shit
One more fucking love song, I'll be sick
Oh

You turned your back on tomorrow
'Cause you forgot yesterday
I gave you my love to borrow
But you just gave it away
You can't expect me to be fine
I don't expect you to care
I know I've said it before
But all of our bridges burned down

I've wasted my nights
You turned out the lights
Now I'm paralyzed
Still stuck in that time when we called it love
But even the Sun sets in paradise

I'm at a payphone trying to call home
All of my change I spent on you
Where have the times gone? Baby, it's all wrong
Where are the plans we made for two?

If happy ever after did exist
I would still be holding you like this
All those fairy tales are full of shit
One more fucking love song, I'll be sick
Now I'm at a payphone

Man, fuck that shit
I'll be out spending all this money while you sitting round
Wondering why it wasn't you who came up from nothing
Made it from the bottom
Now when you see me I'm stunning
And all of my cars start with a push of a button
Telling me the chances I blew up
Or whatever you call it
Switch the number to my phone
So you never could call it
Don't need my name on my shirt
You can tell it I'm ballin'

Swish, what a shame, could have got picked
Had a really good game, but you missed your last shot
So you talk about who you see at the top
Or what you could have saw
But, sad to say, it's over for
Phantom pulled valet open doors
Wiz, like go away got what you was looking for
Now it's me who they want
So you can go and take that little piece of shit with you

I'm at a payphone trying to call home
All of my change I spent on you
Where have the times gone? Baby, it's all wrong
Where are the plans we made for two?

If happy ever after did exist
I would still be holding you like this
All those fairy tales are full of shit
One more fucking love song, I'll be sick
Now I'm at a payphone'''

def printLyric():
  sleep(1)
  letra = letraTextbox.get("0.0", "end")
  letraTratada = unidecode.unidecode(letra)
  letraSplitada = letraTratada.splitlines()
  
  for linha in letraSplitada:
    py.write(linha)
    py.press('enter')
  py.write("Da uma estrela no repo pra dar uma moral, essa é uma das parafernalhas feitas por mim >> https://github.com/samubarreto/Pyautogui-Automations/tree/main/lyricLine")
  py.press('enter')

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

  startButton = customtkinter.CTkButton(mainFrame, text='Iniciar', command=printLyric).pack(padx=20, pady=10)

  root.mainloop()