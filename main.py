import requests
import tkinter as tk

janela = tk.Tk()
janela.title("Busca de Livro")
janela.geometry("600x600")

entrada = tk.Entry(janela, width=60,)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Buscar")
botao.pack(pady=5)

resultado = tk.Label(janela, text="", wraplength=350, justify="left")
resultado.pack(pady=10)

# Código direto no clique (sem função externa)
def clique():
    livro_buscado = entrada.get()
    url = f"https://www.googleapis.com/books/v1/volumes?q={livro_buscado}&langRestrict=pt"
    response = requests.get(url)
    dados = response.json()

    info = dados["items"][0]["volumeInfo"]

    title = info.get("title", "Título não encontrado")
    subtitle = info.get("subtitle", "Subtítulo não encontrado")
    authors = info.get("authors", ["Autor não encontrado"])
    description = info.get("description", "Descrição não encontrada")

    texto = f"Título: {title}\nSubtítulo: {subtitle}\nAutor: {authors}\n\nDescrição:\n{description}"
    resultado.config(text=texto)

botao.config(command=clique)

janela.mainloop()
