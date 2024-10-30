import tkinter as tk

janela = tk.Tk()

var_aviao = tk.StringVar()

botao_classeconomica = tk.Radiobutton(text="Classe Ecônomica", variable= var_aviao, value = "Classe Ecônomica")
botao_classexecutiva = tk.Radiobutton(text="Classe Executiva", variable= var_aviao, value = "Classe Executiva")
botao_primeiraclasse = tk.Radiobutton(text="Primeira Classe", variable= var_aviao, value = "Primeira Classe")
botao_classeconomica.grid(row=0, column = 0)
botao_classexecutiva.grid(row=0, column = 1)
botao_primeiraclasse.grid(row=0, column = 2)

def enviar():
    print(var_aviao.get())

botao_enviar = tk.Button(text = "Enviar", command=enviar)
botao_enviar.grid(row=1, column=0)

tk.mainloop()