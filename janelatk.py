import tkinter as tk

janela = tk.Tk()
janela.title("Promoções e Políticas")

# Variável para checkbox de promoções
var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(janela, text="Deseja receber e-mail promocionais", variable=var_promocoes)
checkbox_promocoes.grid(row=0, column=0, padx=10, pady=10)

# Variável para checkbox de políticas
var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(janela, text="Concordo com os Termos de Uso e Políticas de Privacidade", variable=var_politicas)
checkbox_politicas.grid(row=1, column=0, padx=10, pady=10)

def enviar():
    if var_promocoes.get():
        print('Usuário deseja receber promoções')
    else:
        print('Usuário NÃO deseja receber promoções')

    if var_politicas.get():
        print('Usuário concordou com Termos de Uso e Políticas de Privacidade')
    else:
        print("Usuário NÃO concordou")

botao_enviar = tk.Button(janela, text="Enviar", command=enviar)
botao_enviar.grid(row=2, column=0)

janela.mainloop()
