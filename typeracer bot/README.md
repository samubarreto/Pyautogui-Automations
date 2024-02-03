# Typeracer Cheat

Este é um pequeno projeto em Python desenvolvido para roubar no jogo [Typeracer](https://play.typeracer.com/?universe=play). Ele utiliza a biblioteca PyAutoGUI para automatizar a digitação, proporcionando vantagem nos modos de frase em inglês e de uma única palavra repetida.

## Requisitos

Certifique-se de ter o Python instalado em sua máquina. Além disso, você precisará instalar a biblioteca PyAutoGUI e a Customtkinter. Para fazer isso, execute os seguintes comandos:

```bash
pip install pyautogui
pip install customtkinter
```

## Como usar

### Modo de Apenas Uma Palavra Repetida

1. Abra o arquivo `oneword.py`
2. Execute o script.
3. Escreva a palavra desejada quando solicitado.
4. Aguarde o contador do site Typeracer chegar a 1 segundo.
5. Clique no botão "Iniciar" no Typeracer.
6. Volte para o navegador e aguarde o script realizar a automação.
7. Pronto. Para parar o bot facilmente aperte WIN + L.

### Modo de Frase em Inglês

1. Abra o arquivo `engPhrase.py`
2. Inicie a corrida no Typeracer.
3. Rapidamente inspecione a página e copie a frase da partida.
4. Cole a frase no programa.
5. Ajuste manualmente o início da frase no bot, pois ela não será copiada corretamente.
6. Espere o timer do Typeracer chegar a 1 segundo.
7. Inicie o script. Pronto.

**Importante:** Este modo deve ser usado apenas com frases em inglês, pois o PyAutoGUI pode ter problemas com acentuações. Além disso, frases com "?" ou "!" não funcionarão corretamente.

### Demonstração

https://youtu.be/_pX-P0CJsa0
