# Auto Accept para League of Legends 🎮

Este projetinho simples faz o trabalho de aceitar a fila no League of Legends automaticamente. Nada mais que isso! Ele fica de olho na tela do usuário, buscando pela imagem "accept.png" a cada meio segundo. Toda vez que a imagem é encontrada (ou seja, `local != None`), o programa para aceitar a partida.

Além disso, o código está preparado para lidar com a possibilidade de algum outro jogador recusar a partida. Nesse caso, o programa volta para a fila e continua aguardando a próxima tela de confirmação.

Recomendo utilizar esta ferramenta para partidas rápidas, daquelas que não envolvem a seleção de campeões.

## Como usar

1. Clone o repositório.
2. Certifique-se de ter as dependências instaladas.
   ```bash
   pip install pyautogui
   ```
3. Inicie a fila no jogo e execute o arquivo main.py
4. Pronto!
