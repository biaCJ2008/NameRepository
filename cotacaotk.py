import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Cotação de Moedas")

mensagem = tk.Label(janela, text="Sistemas de busca de Cotação de Moedas", fg='white', bg='#7E40C8')
mensagem.grid(row=0, column=0, columnspan=2)

mensagem2 = tk.Label(janela, text="Selecione a moeda desejada", height=15, width=70)
mensagem2.grid(row=1, column=0)

def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    
    if cotacao_moeda:
        mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'
    else:
        mensagem_cotacao["text"] = "Cotação não encontrada"

mensagem_cotacao = tk.Label(janela, text="")
mensagem_cotacao.grid(row=3, column=0, columnspan=2)

botao = tk.Button(janela, text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

dicionario_cotacoes = {
    'Dolar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000
}

moedas = list(dicionario_cotacoes.keys())
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

mensagem3 = tk.Label(janela, text="Caso você queira pegar mais de 1 cotação ao mesmo tempo, digite uma moeda em cada linha")
mensagem3.grid(row=4, column=0, columnspan=2)

caixa_texto = tk.Text(janela, width=30, height=5)
caixa_texto.grid(row=5, column=0, sticky='nswe')

def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.strip().split('\n')
    mensagem_cotacoes = []

    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item.strip())
        if cotacao:
            mensagem_cotacoes.append(f'{item.strip()}: {cotacao}')

    mensagem4["text"] = '\n'.join(mensagem_cotacoes) if mensagem_cotacoes else "Nenhuma cotação encontrada."

mensagem4 = tk.Label(janela, text="")
mensagem4.grid(row=6, column=0, columnspan=2)

botao_multiplacotacoes = tk.Button(janela, text="Buscar Cotações", command=buscar_cotacoes)
botao_multiplacotacoes.grid(row=5, column=1)

janela.mainloop()
