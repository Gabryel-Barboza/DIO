import webbrowser
from tkinter import *

# Programa para abrir o navegador através de interface gráfica

# Utiliza o módulo para abrir o navegador e ir até o link
def google():
    webbrowser.open("www.google.com")


# Instancia uma janela sem definição
root = Tk( )
# Título e tamanho da janela
root.title("Abrir Browser")
root.geometry("300x200")
# Botão de ação para executar a função
mygoogle = Button(root, text="Abrir o Google", command=google).pack(pady=20)

# Executando a janela
root.mainloop()
