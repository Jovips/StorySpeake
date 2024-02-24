# StorySpeake
Este é um simples programa em Python que utiliza a biblioteca `pyttsx3` e a interface gráfica `tkinter` para ler em voz alta o conteúdo de um arquivo de texto.

## Requisitos

Certifique-se de ter Python instalado em seu sistema. Além disso, instale as seguintes bibliotecas:

```bash
pip install pyttsx3
```
## Utilização
### Clone o Repositorio

```
git clone https://github.com/Jovips/StorySpeake.git
```


Execute o programa executando o arquivo storyspeake.py Ele solicitará que você insira seu nome e selecione um arquivo de texto para ler. O conteúdo do arquivo selecionado será lido em voz alta usando a voz configurada.

#### Como funciona ?
- Após executado </br>
1 - O programa solicitará que você insira seu nome usando uma caixa de diálogo. </br>
2 - Em seguida, abrirá uma janela de seleção de arquivo para você escolher o arquivo de texto que deseja ouvir </br>
3 - Após selecionar o arquivo, o programa lerá seu conteúdo em voz alta usando a voz configurada.

### Funcionalidades Adicionais
Você pode ajustar a voz modificando as configurações dentro da função `ler_arquivo(arquivo,nome)`
```bash
def ler_arquivo(arquivo,nome):
    try:
        with open(arquivo, "r") as f:
            texto = f.read()
        engine = pyttsx3.init()
      
    # Configurar a voz (**AQUI**)
        engine.setProperty("voice", "pt-br")
        engine.setProperty("rate", 190)
        engine.setProperty("volume", 3.00)
```
### Autor
Este programa foi escrito por Jovips (João Vitor).
