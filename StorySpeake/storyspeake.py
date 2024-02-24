import pyttsx3
import tkinter as tk
from tkinter import filedialog,simpledialog


def obter_nome():
    nome = simpledialog.askstring("Nome do usuário", "Digite o seu nome:")
    return nome


nome = obter_nome()
root = tk.Tk()
root.withdraw()


def ler_arquivo(arquivo,nome):
    try:

        with open(arquivo, "r") as f:
            texto = f.read()

    # Inicializar o motor de texto para fala com a biblioteca pyttsx3
        engine = pyttsx3.init()
        

    # Configurar a voz

        engine.setProperty("voice", "pt-br")
        engine.setProperty("rate", 190)
        engine.setProperty("volume", 3.00)

        # Falar o texto
        engine.say(f"Olá, {nome}. O arquivo selecionado por você contém o seguinte conteúdo:")
        engine.say(texto)
        engine.runAndWait()

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")

# Abrir a janela de seleção de arquivo
root = tk.Tk()
root.withdraw()
arquivo = filedialog.askopenfilename(title="Selecione um arquivo de texto", filetypes=[("Arquivos de texto", "*.txt")])

# Se um arquivo foi selecionado, chame a função para lê-lo
if arquivo:
    ler_arquivo(arquivo,nome)

# Fechar a janela principal
root.destroy()