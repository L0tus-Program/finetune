import tkinter as tk

# Cria uma janela como uma sobreposição
root = tk.Tk()
root.wm_attributes("-topmost", True) # Define a janela como a mais alta
root.overrideredirect(True) # Remove a barra de título e as bordas da janela

# Configura a tela cheia
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}+0+0")

# Adiciona um rótulo de exemplo
label = tk.Label(root, text="Programa sobreposto")
label.pack()

# Função para fechar a janela
def fechar():
    root.destroy()

# Cria um botão para fechar a janela
button = tk.Button(root, text="Fechar", command=fechar)
button.pack()

# Inicia o loop principal da janela
root.mainloop()